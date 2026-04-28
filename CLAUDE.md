# CLAUDE.md

本文件为 Claude Code（claude.ai/code）在此仓库中工作时提供指导。仓库内可能有多个 Agent 协作，通过此文件共享项目规范。

## 项目概述

**《Kubernetes in Action, Second Edition》**（作者：Marko Lukša 和 Kevin Conner）的中文翻译项目。

- 源文件：`source/k8s-in-action-2e.pdf`（690 页，4.1 MB）
- 目标读者：中文世界的 Kubernetes 初学者
- 部署方式：`translation/` 是标准的 Zensical 静态站点项目，可通过 `uv run zensical build` / `uv run zensical serve` 构建和本地预览

## 目录结构

```
/
├── CLAUDE.md
├── .gitignore
├── README.md
├── .github/workflows/                # CI/CD 部署
│   └── docs.yml
├── source/                           # 原始资料
│   ├── k8s-in-action-2e.pdf
│   ├── catalog.md                    # 全书书签树（三级标题 + 页码映射）
│   └── zensical-admonitions.md       # Zensical admonition 语法参考
├── scripts/
│   └── extract_chapter.py            # Marker 包装脚本
├── extracted/                        # 中间产物：Marker 提取的英文 Markdown
│   ├── front-matter/                 # 前言、致谢、关于本书等
│   ├── ch01-introducing-kubernetes/   # 每章一个独立目录，含 .md + 图片
│   ├── ch02-containers/
│   ├── ...（共 18 章）
│   └── ch18-jobs-cronjobs/
└── translation/                      # Zensical 静态站点项目（最终成品）
    ├── zensical.toml                 # Zensical 配置文件
    ├── pyproject.toml
    ├── uv.lock
    ├── .venv/                        # Python 虚拟环境（含 zensical CLI）
    ├── site/                         # 构建产物
    └── docs/                         # 文档内容（翻译产物所在）
        ├── index.md                    # 前言（站点首页）
        ├── 01-acknowledgments.md     # 致谢
        ├── 02-about-this-book.md     # 关于本书
        ├── 03-about-the-authors.md   # 关于作者
        ├── 04-about-the-cover-illustration.md  # 关于封面插图
        ├── 05-glossary.md            # 术语表
        ├── overrides/                # Zensical 模板覆写
        │   └── partials/
        │       └── footer.html
        ├── images/                   # 各章节图片
        │   ├── authors/              # 作者照片
        │   │   ├── marko-luksa.jpg
        │   │   └── kevin-conner.jpg
        │   ├── icon/                 # 站点图标
        │   │   └── book.png
        │   ├── ch01/
        │   │   ├── figure-1.1.jpg
        │   │   └── ...
        │   └── ...
        ├── part1-getting-started/
        │   ├── index.md              # Part 1 介绍文字
        │   ├── ch01-introducing-kubernetes.md
        │   ├── ch02-containers.md
        │   ├── ch03-first-app.md
        │   └── ch04-api-object-model.md
        ├── part2-running-apps/
        │   ├── index.md
        │   ├── ch05-pods.md
        │   ├── ch06-pod-lifecycle.md
        │   └── ch07-namespaces-labels.md
        ├── part3-config-storage/
        │   ├── index.md
        │   ├── ch08-configmaps-secrets.md
        │   ├── ch09-volumes.md
        │   └── ch10-persistentvolumes.md
        ├── part4-connecting-exposing/
        │   ├── index.md
        │   ├── ch11-services.md
        │   ├── ch12-ingress.md
        │   └── ch13-gateway-api.md
        └── part5-managing-at-scale/
            ├── index.md
            ├── ch14-replicasets.md
            ├── ch15-deployments.md
            ├── ch16-statefulsets.md
            ├── ch17-daemonsets.md
            └── ch18-jobs-cronjobs.md
```

四层职责：**source（输入端）→ scripts（工具）→ extracted（中间态）→ translation/docs（成品）**。

## 翻译规范

- **代码块**：YAML 清单和 shell 命令保持原文不动，只翻译周边说明文字。代码块必须标注类型，常用类型如下：
  - 终端命令（包括 kubectl、docker、curl、gcloud、minikube 等命令及其输出）→ ` ```bash `
  - YAML 清单（Deployment、Pod、Service、kind 配置等）→ ` ```yaml `
  - JSON 输出 → ` ```json `
  - Dockerfile 内容 → ` ```dockerfile `
  - 纯文本/应用输出 → ` ```text `
  - 代码片段（JS、Go 等）→ ` ```js ` / ` ```go ` 等
  - 表格/纯文本日志 → ` ``` `（无类型标注）
- **术语一致性**：首次遇到 K8s 术语时，确定中文译法并记录到 `translation/docs/05-glossary.md`，后续章节严格沿用。每次翻译前先查阅 `glossary.md`
- **标注框**：书中 callout/sidebar（如 "This chapter covers"、"NOTE"、"DEFINITION"）使用 Zensical admonition 语法。语法格式见 `source/zensical-admonitions.md`。基本格式为 `!!! type "标题"` 后接四空格缩进内容。常用类型：`note`、`info`、`tip`、`warning`。不可使用 `:::` 语法（非 Zensical 支持）
- **图表**：Marker 已自动提取图片。将图片从 `extracted/<chapter>/` 拷贝到 `translation/docs/images/<chapter>/`，重命名为 `figure-X.X.jpg`。由于 markdown 文件位于 `translation/docs/` 下，图片引用路径为 `../images/chXX/figure-X.X.jpg`（相对于当前 markdown 文件的路径）。图表标题（Figure X.X）翻译为"图 X.X 描述"

## PDF 提取方案

主力工具为 **[Marker](https://github.com/VikParuchuri/marker)**，经与 pymupdf、unstructured 对比测试后选定。

优势：页眉页脚自动移除、软连字符自动修复、代码块自动 fence、图片自动提取并嵌入 markdown。

运行方式：
```bash
uv run --with "marker-pdf[full]" --with "pymupdf" python scripts/extract_chapter.py \
    --start-page 33 --end-page 53 \
    --chapter-tag ch01-introducing-kubernetes
```

参数说明：
- `--start-page` / `--end-page`：章节在 PDF 中的页码范围（1-indexed，从 `source/catalog.md` 获取）
- `--chapter-tag`：产物目录名，对应 `extracted/<chapter-tag>/`

Marker 首次运行需下载模型（~80s/章，Apple Silicon 使用 MPS 加速）。输出包含 `*.md` + `*_meta.json` + 图片文件。

## Zensical 本地预览

在 `translation/` 目录下通过 uv 运行：

```bash
cd translation
uv run zensical serve    # 启动本地开发服务器，支持热重载
uv run zensical build    # 构建静态站点到 site/ 目录
```

## 工作流

1. 选定要翻译的章节，根据 `source/catalog.md` 确定页码范围
2. 运行 `scripts/extract_chapter.py` 提取，产物写入 `extracted/<chapter-tag>/`
3. 将提取的 markdown 作为底稿，逐段翻译写入 `translation/docs/` 对应位置，代码块保持不动
4. 若章节内容较长（>400 行），按原文章节的小节（如 3.1、3.1.1、3.2）为单位分段翻译，每个小节完成后追加到文件末尾。不可盲目按字数或行数切分
5. 将章节图片拷贝到 `translation/docs/images/<chapter>/`，更新 markdown 中的图片引用路径（相对路径格式：`../images/chXX/figure-X.X.jpg`）
6. 遇到新术语时确定译法并写入 `translation/docs/05-glossary.md`
7. 翻译完成后更新术语表（如有新增术语）
8. 运行 `cd translation && uv run zensical serve` 预览效果

### 任务粒度

翻译任务以**章节**为基本单位，不以 Part 为粒度。每个章节作为一个独立任务（如 `Part3-Ch8`），而不是 `翻译 Part 3`。这样可以保证每个章节的翻译质量，避免在大量文字中丢失上下文。

### Part 介绍文字

书中每个 Part 的开头都有一段介绍文字（位于该 Part 标题页），概述该部分各章节的内容。翻译每个 Part 时，**必须**将这部分文字翻译并写入对应 `translation/docs/<part-dir>/index.md`。参考 `part1-getting-started/index.md` 的格式。

### Marker 提取并发限制

**最多同时运行 1 个 Marker 提取进程**。本机只有 16GB 内存，2 个 Marker 进程也会导致内存压力过大。提取多章节时，严格逐个执行。
