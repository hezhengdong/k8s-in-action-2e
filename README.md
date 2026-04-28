# Kubernetes in Action, Second Edition —— 中文翻译

[![License: CC0](https://img.shields.io/badge/License-CC0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

本书为 *Kubernetes in Action, Second Edition*（作者 Marko Lukša & Kevin Conner，Manning Publications 出版）的中文翻译版。

> **免责声明：本项目为个人学习项目，翻译内容仅供个人学习使用，不得用于商业用途。如需商业使用，请购买正版书籍。**

## 背景

Kubernetes 一直在演进，网上的教程要么过时，要么不够系统。本书第一版口碑很好，第二版于 2026 年 3 月底正式发行。苦于英语水平有限，尝试了多种翻译工具后体验都不理想，恰逢 Coding Agent 技术火热，于是借助 AI 完成了这版翻译。

## 技术栈

| 环节 | 工具 |
|------|------|
| PDF → Markdown | [Marker](https://github.com/VikParuchuri/marker) |
| 翻译 + 校对 | Claude Code + DeepSeek-V4-Pro-Max |
| 站点生成 | [Zensical](https://zensical.org) |
| 站点部署 | GitHub Pages / Cloudflare Pages |

## 在线访问

- [k8s-in-action-2e.pages.dev](https://k8s-in-action-2e.pages.dev/)（Cloudflare Pages，推荐）
- [hezhengdong.github.io/k8s-in-action-2e](https://hezhengdong.github.io/k8s-in-action-2e/)（GitHub Pages，备用）

## 项目结构

```
/
├── source/         原始 PDF 及书签目录
├── scripts/        PDF 提取脚本（基于 Marker）
├── extracted/      Marker 提取的英文中间产物（含图片）
├── translation/    Zensical 静态站点（翻译成品）
│   └── docs/       各章节 Markdown 文件
└── CLAUDE.md       AI 协作规范（Agent 共享指南）
```

## 本地预览

```bash
cd translation
uv run zensical serve   # 启动本地服务器，支持热重载
uv run zensical build   # 构建静态站点到 site/ 目录
```

## 进度

- [x] 第 1 章  初识 Kubernetes
- [x] 第 2 章  容器
- [x] 第 3 章  部署第一个应用
- [x] 第 4 章  API 对象模型
- [x] 第 5 章  Pod
- [x] 第 6 章  Pod 生命周期
- [x] 第 7 章  命名空间与标签
- [x] 第 8 章  ConfigMap 与 Secret
- [x] 第 9 章  卷
- [x] 第 10 章 持久卷
- [x] 第 11 章 Service
- [x] 第 12 章 Ingress
- [x] 第 13 章 Gateway API
- [x] 第 14 章 ReplicaSet
- [x] 第 15 章 Deployment
- [x] 第 16 章 StatefulSet
- [x] 第 17 章 DaemonSet
- [x] 第 18 章 Job 与 CronJob

全书 18 章翻译及校对已全部完成。

## 许可证

中文翻译内容采用 [CC0](https://creativecommons.org/publicdomain/zero/1.0/) 许可，你可自由使用、修改、分发，无需署名。英文原版版权归 Manning Publications 所有。
