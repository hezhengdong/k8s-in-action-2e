# 关于本书

《Kubernetes in Action, Second Edition》为在 Kubernetes 上高效开发与运行应用奠定了基础。本书聚焦于**开发**层面——构建、配置、部署和管理应用——而非运维生产集群。

本书从容器基础开始（使用 Docker 或 Podman），适合初学者，随后按照逻辑递进的顺序，逐步引导读者深入核心和高级 Kubernetes 概念。无论您是刚接触 Kubernetes 还是已有一定经验，都能从中获得如何在实际应用开发中有效使用该平台的实践性理解。

## 谁应该读这本书

《Kubernetes in Action, Second Edition》主要面向想要构建、容器化并在 Kubernetes 上运行应用的开发者和系统管理员。本书同时适合初学者和有经验的工程师——不需要具备容器或 Kubernetes 的预备知识。

概念由浅入深地逐步介绍，通过不要求深厚专业知识的简单示例展开。读者应具备基本的编程、计算机网络、Linux 命令行使用以及 HTTP 等常见协议的基础知识。

## 本书结构：阅读路线图

本书分为五个部分，涵盖 18 章。

**Part 1** 介绍 Kubernetes 及其所基于的容器技术：

- 第 1 章概览 Kubernetes——它是什么、解决了什么问题、如何变革应用部署和运维，以及它是否适合您和您的组织。
- 第 2 章讲解容器基础知识——容器与虚拟机的区别、底层技术、构建第一个容器镜像并使用 Docker 或 Podman 运行。
- 第 3 章将该容器镜像在 Kubernetes 中运行（本地或云端），展示如何将应用暴露到外部，并演示简单的水平扩缩容。
- 第 4 章探索 Kubernetes API 和基本对象类型（如 Node 和 Event），理解 Kubernetes 如何表示和管理集群状态。

**Part 2** 深入运行、组织和保持应用健康的核心概念：

- 第 5 章介绍 Pod——Kubernetes 的基本构建块——包括应用如何在 Pod 内的容器中运行，以及边车/辅助容器如何增强功能。
- 第 6 章讲解 Pod 生命周期——启动/关闭动作、存活探针/就绪探针/启动探针，以及如何保持容器健康。
- 第 7 章解释如何使用标签、命名空间及相关机制组织大量 Pod 和其他对象，以保持清晰和可维护性。

**Part 3** 聚焦通过 Kubernetes API 配置应用和挂载存储：

- 第 8 章展示如何通过命令行参数、环境变量、ConfigMap（用于非敏感数据）和 Secret（用于密钥、令牌、密码等敏感值）传递配置。
- 第 9 章讲解向 Pod 添加卷、将其挂载到容器、跨重启持久化数据、在容器间共享文件、访问节点文件系统，以及注入来自 ConfigMap、Secret 或 Pod 元数据的数据。
- 第 10 章介绍基于 PersistentVolume（PV）和 PersistentVolumeClaim（PVC）的持久化存储，静态与动态供应，节点本地存储与网络存储，临时卷与持久卷，以及卷快照。

**Part 4** 解释集群内部和外部的通信：

- 第 11 章讲解 Pod 间通信、使用 Service 为 Pod 组提供稳定端点、服务发现、外部暴露和就绪信号。
- 第 12 章描述如何通过单个公共 IP 使用 Ingress 对外暴露多个 Service。
- 第 13 章介绍 Gateway API 作为 Ingress 的现代替代方案，涵盖 Gateway、HTTPRoute、TLSRoute、TCPRoute、UDPRoute 等用于内部和外部流量的资源。

**Part 5** 聚焦管理各种工作负载的高级控制器（您很少直接创建 Pod）：

- 第 14 章解释 ReplicaSet 及其如何维护期望数量的 Pod 副本以实现高可用。
- 第 15 章讲解 Deployment，它能自动管理 ReplicaSet 并支持受控的滚动更新、回滚和更新。
- 第 16 章介绍用于有状态应用的 StatefulSet，提供稳定的网络标识、有序扩缩容和其他有状态行为。
- 第 17 章描述 DaemonSet，为每个节点创建和管理一个 Pod，适用于节点级代理、监控等场景。
- 第 18 章以批处理结束全书。您将学习如何使用 Job 对象运行一次性任务，或使用 CronJob 在特定时间调度周期性任务。

初次接触容器或 Kubernetes 的读者，以及希望获得扎实、循序渐进理解的读者，应从头到尾按顺序阅读各章。每一章都直接建立在前面章节介绍的概念和示例之上，因此按序阅读能确保在前进之前具备必要的基础。

已有 Kubernetes 工作经验、更多将本书用作参考或深入研读的读者，可以直接跳到解决当前需求或兴趣的特定章节。

### 关于代码

虽然本书不包含大量实际源代码，但包含许多 Kubernetes 资源的 YAML 清单以及 Shell 命令及其输出。这些内容使用等宽字体显示，以与普通文本区分。

shell 命令大多以**粗体**显示，以便与输出清楚区分，但有时仅对命令或输出中最关键的部分加粗以突出重点。在大多数情况下，命令输出已重新格式化以适应本书有限的空间。此外，由于 Kubernetes CLI 工具 kubectl 在持续演进，较新版本可能会打印出比书中所示更多的信息，因此如果输出不完全匹配，不必困惑。

清单有时包含续行标记（➥），表示一行文本换行到下一行。它们还包含注释，高亮并解释最重要的部分。

本书中的所有示例均已在 Google Kubernetes Engine（GKE）中运行的 Kubernetes 1.35 版本和使用 kind 运行的本地集群上测试。完整的源代码和 YAML 清单可从出版社网站下载：[www.manning.com/books/kubernetes-in-action-second-edition](http://www.manning.com/books/kubernetes-in-action-second-edition)。

### liveBook 讨论论坛

购买《Kubernetes in Action, Second Edition》可免费访问 Manning 的在线阅读平台 liveBook。通过 liveBook 独有的讨论功能，您可以将评论附加到整本书或特定章节、段落。方便您为自己做笔记、提出和回答技术问题，并从作者和其他用户那里获得帮助。要访问论坛，请访问 [https://livebook.manning.com/book/kubernetes-in-action-second-edition/discussion](https://livebook.manning.com/book/kubernetes-in-action-second-edition/discussion)。

Manning 对读者的承诺是提供一个场所，让读者之间以及读者与作者之间能够进行有意义的对话。这并非对作者参与程度的任何具体承诺，作者在论坛中的贡献完全是自愿的（且无偿的）。我们建议您尝试向作者提出一些有挑战性的问题，以免他们的关注点跑偏！只要本书仍在出版，该论坛及历史讨论的存档将始终可通过出版社网站访问。

### 其他在线资源

您可以在以下地址找到大量额外的 Kubernetes 资源：

- Kubernetes 网站（<https://kubernetes.io>）
- Kubernetes 博客，定期发布有趣的信息（<http://blog.kubernetes.io/>）
- Kubernetes 社区的 Slack 频道（<http://slack.k8s.io/>）
- Kubernetes YouTube 频道（<https://www.youtube.com/channel/UCZ2bu0qutTOM0tHYa_jkIwg>）

由于 Kubernetes 是开源的，其源代码本身也包含大量信息。您可以在 <https://github.com/kubernetes/kubernetes> 及相关仓库找到。
