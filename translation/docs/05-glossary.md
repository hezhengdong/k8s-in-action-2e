# 术语表

翻译过程中持续更新，各章节严格沿用。

| 英文 | 中文 | 说明 |
|------|------|------|
| Kubernetes | Kubernetes | 不翻译，可缩写为 K8s |
| kubelet | kubelet | K8s 组件名，不翻译 |
| kube-proxy | kube-proxy | K8s 组件名，不翻译 |
| etcd | etcd | 分布式键值存储，不翻译 |
| kubectl | kubectl | K8s 命令行工具，不翻译 |
| pod | Pod | K8s 核心资源类型，不翻译 |
| container | 容器 | |
| control plane | 控制平面 | |
| control plane node | 控制平面节点 | |
| worker node | 工作节点 | |
| workload plane | 工作负载平面 | 亦称数据平面（data plane） |
| microservice | 微服务 | |
| monolith | 单体应用 | |
| deployment | 部署 / Deployment | 动词译为"部署"，作为 K8s 资源名保留 Deployment |
| service | 服务 / Service | 通用概念译为"服务"，作为 K8s 资源名保留 Service |
| scheduler | 调度器 | |
| controller | 控制器 | |
| manifest | 清单 | YAML/JSON 格式的对象定义文件 |
| load balancer | 负载均衡器 | |
| scaling | 扩缩容 | horizontal scaling → 水平扩缩容 |
| replica | 副本 | |
| self-healing | 自愈 | |
| service discovery | 服务发现 | |
| leader election | 领导者选举 | |
| cloud-native | 云原生 | |
| on-premises | 本地部署 | 部署在自有数据中心 |
| namespace | 命名空间 | |
| ConfigMap | ConfigMap | K8s 资源类型，不翻译 |
| Secret | Secret | K8s 资源类型，不翻译 |
| PersistentVolume | PersistentVolume | K8s 资源类型，不翻译 |
| PersistentVolumeClaim | PersistentVolumeClaim | K8s 资源类型，不翻译 |
| StorageClass | StorageClass | K8s 资源类型，不翻译 |
| CSI (Container Storage Interface) | CSI | 容器存储接口，不翻译 |
| CSIDriver | CSIDriver | K8s 资源类型，不翻译 |
| VolumeSnapshot | VolumeSnapshot | K8s 资源类型，不翻译 |
| VolumeSnapshotClass | VolumeSnapshotClass | K8s 资源类型，不翻译 |
| VolumeSnapshotContent | VolumeSnapshotContent | K8s 资源类型，不翻译 |
| provisioner | 供应器 | 负责供应存储卷的组件 |
| dynamic provisioning | 动态供应 | 按需自动创建存储卷 |
| static provisioning | 静态供应 | 预先手动供应存储卷 |
| reclaim policy | 回收策略 | PersistentVolume 释放后的处理策略 |
| access mode | 访问模式 | 卷的挂载与读写权限模式 |
| volume snapshot | 卷快照 | 持久卷的快照 |
| snapshot | 快照 | |
| ephemeral volume | 临时卷 | 生命周期与 Pod 绑定的 PersistentVolume |
| volume binding mode | 卷绑定模式 | PersistentVolume 何时与声明绑定的策略 |
| volume mode | 卷模式 | 卷的文件系统或块设备模式 |
| API server | API 服务器 | |
| container runtime | 容器运行时 | |
| ReplicaSet | ReplicaSet | K8s 资源类型，确保指定数量的 Pod 副本运行，不翻译 |
| ReplicationController | ReplicationController | 已弃用的 K8s 资源类型，功能与 ReplicaSet 相同，不翻译 |
| reconciliation | 协调 | 控制器将实际状态与期望状态保持一致的过程 |
| reconciliation loop | 协调循环 | 控制器持续运行的实际状态与期望状态比较循环 |
| garbage collector | 垃圾收集器 | Kubernetes 中自动删除无主从属对象的组件 |
| owner reference | 所有者引用 | 对象 metadata 中指向其所有者对象的引用 |
| dependent | 从属对象 | 由 owner reference 关联的、属于某个所有者的对象 |
| orphan | 孤儿 | 失去所有者的从属对象 |
| label selector | 标签选择器 | 通过匹配标签来选择一组资源的字段 |
| deletion cost | 删除成本 | Pod 注解，影响缩容时删除 Pod 的优先级 |
| exponential backoff | 指数退避 | 容器持续崩溃时重启延迟逐步增加的机制 |
| Gateway API | Gateway API | K8s 流量路由 API，不翻译 |
| Gateway | Gateway | Gateway API 中的网关资源，不翻译 |
| GatewayClass | GatewayClass | Gateway 的类别资源，不翻译 |
| HTTPRoute | HTTPRoute | Gateway API 中的 HTTP 路由资源，不翻译 |
| TLSRoute | TLSRoute | Gateway API 中的 TLS 路由资源，不翻译 |
| TCPRoute | TCPRoute | Gateway API 中的 TCP 路由资源，不翻译 |
| UDPRoute | UDPRoute | Gateway API 中的 UDP 路由资源，不翻译 |
| GRPCRoute | GRPCRoute | Gateway API 中的 gRPC 路由资源，不翻译 |
| ReferenceGrant | ReferenceGrant | Gateway API 中的跨命名空间引用授权资源，不翻译 |
| Ingress | Ingress | K8s 流量入口资源，不翻译 |
| IngressClass | IngressClass | Ingress 的类别资源，不翻译 |
| Ingress 控制器 | Ingress 控制器 | 实现 Ingress 功能的控制器组件 |
| CRD (Custom Resource Definition) | 自定义资源定义（CRD） | |
| Kustomize | Kustomize | K8s 清单自定义工具，不翻译 |
| Istio | Istio | 服务网格和 Gateway API 实现，不翻译 |
| Envoy | Envoy | 高性能代理，不翻译 |
| service mesh | 服务网格 | 服务间通信基础设施层 |
| TLS termination | TLS 终止 | 在代理端解密 TLS 流量 |
| TLS passthrough | TLS 透传 | TLS 流量原样穿透代理 |
| SNI (Server Name Identification) | 服务器名称指示（SNI） | TLS 协议的扩展 |
| north/south traffic | 南北向流量 | 集群外部与内部服务之间的流量 |
| east/west traffic | 东西向流量 | 集群内部服务之间的流量 |
| canary | 金丝雀 | 用于测试新版本的少量流量部署 |
| gRPC | gRPC | 高性能 RPC 框架，不翻译 |
| listener | 监听器 | Gateway 接受网络连接的逻辑端点 |
| proxy | 代理 | 泛指反向代理或负载均衡器 |
| SMI (Service Mesh Interface) | 服务网格接口（SMI） | |
| GAMMA | GAMMA | Gateway API Mesh Management and Administration 倡议，不翻译 |
| backend | 后端 | 路由流量目标，通常为 Service |
| filter | 过滤器 | 用于修改/增强流量 Route 中的规则 |
| Job | Job | K8s 资源类型，运行有限任务至完成，不翻译 |
| CronJob | CronJob | K8s 资源类型，按调度计划运行 Job，不翻译 |
| batch processing | 批处理 | 非持续运行的任务处理模式 |
| completions | 完成数 | Job spec 字段，指定必须成功完成的 Pod 数量 |
| parallelism | 并行度 | Job spec 字段，指定可并行运行的 Pod 数量 |
| completionMode | 完成模式 | Job spec 字段，支持 Indexed 和 NonIndexed |
| Indexed | Indexed | 完成模式之一，每个 Pod 获得唯一索引号，不翻译 |
| NonIndexed | NonIndexed | 完成模式之一，所有 Pod 完全相同（默认），不翻译 |
| work queue | 工作队列 | 用于动态分配任务的数据结构 |
| backoff limit | 回退限制 | Job 失败重试的最大次数 |
| activeDeadlineSeconds | 活跃截止时间 | Job 允许运行的最长时间（秒） |
| restartPolicy | 重启策略 | Pod spec 字段，控制容器终止后的重启行为 |
| concurrencyPolicy | 并发策略 | CronJob spec 字段，控制多个 Job 的重叠行为 |
| DaemonSet | DaemonSet | K8s 资源类型，确保每个节点恰好运行一个 Pod，不翻译 |
| node selector | 节点选择器 | 通过节点标签限制 Pod 可调度的节点集合 |
| node agent | 节点代理 | 运行在节点上的守护进程，提供系统级服务 |
| daemon Pod | 守护 Pod | 由 DaemonSet 部署的 Pod 实例 |
| host port | 主机端口 | 将 Pod 容器的端口映射到主机节点的端口 |
| host network | 主机网络 | Pod 直接使用节点网络命名空间的模式 |
| taint | 污点 | 节点上排斥 Pod 调度的标记 |
| toleration | 容忍 | Pod 允许被调度到有特定污点的节点的声明 |
| priority class | 优先级类 | 定义 Pod 相对重要性和抢占行为的对象 |
| internal traffic policy | 内部流量策略 | Service 字段，控制到后端的流量是否仅在本地节点转发 |
| privileged container | 特权容器 | 具有主机内核完全访问权限的容器 |
| capability | 能力 | Linux 内核权限的细粒度集合，可赋予容器 |
| rolling update | 滚动更新 | 逐个替换 Pod 的更新策略，在 DaemonSet 中也适用 |
| startingDeadlineSeconds | 启动截止时间 | CronJob spec 字段，Job 允许延迟启动的最长时间 |
| ttlSecondsAfterFinished | 完成后的 TTL 秒数 | Job spec 字段，完成后自动删除的等待时间 |
| podFailurePolicy | Pod 失败策略 | Job spec 字段，自定义的失败处理规则 |
| successPolicy | 成功策略 | Job spec 字段，自定义的成功判定规则 |
| sidecar | 边车容器 | 辅助主容器工作的附加容器 |
| init container | 初始化容器 | 在应用容器启动前运行的专用容器 |
| subdomain | 子域名 | Pod spec 字段，指定 Pod 所属的子域 |
| headless Service | 无头 Service | clusterIP 为 None 的 Service |
| schedule | 调度计划 | CronJob spec 字段，定义 Job 何时运行 |
| crontab | crontab | 定时任务调度格式，保留不翻译 |
| StatefulSet | StatefulSet | K8s 资源类型，管理有状态应用，不翻译 |
| liveness probe | 存活探针 | 检测容器是否仍在正常运行 |
| readiness probe | 就绪探针 | 检测容器是否已准备好接收流量 |
| startup probe | 启动探针 | 检测容器内的应用是否已完成启动 |
| rollback | 回滚 | 将 Deployment 或 StatefulSet 恢复到之前的版本 |
