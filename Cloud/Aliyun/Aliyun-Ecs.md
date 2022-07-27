# 云服务器ECS

云服务器 ECS（Elastic Compute Service）是一种弹性可伸缩的云计算服务。

[云服务ECS主页](https://www.aliyun.com/product/ecs)

[云服务器ECS视频](http://cloud.video.taobao.com/play/u/3897629815/p/1/e/6/t/1/301659704826.mp4)

## 应用场景

### 通用Web应用

大部分Web应用使用的架构，阿里云推荐C/G/R系列服务器，兼顾高效搭建使用及高性能处理能力

* CDN网络为Web应用提供内容分发服务，保证最优用户体验与成本节约
* 内容缓存在OSS存储中，提供高可靠性、低成本的存储容量
* 负载均衡处理HTTP请求，并将流量分发到主业务可用区
* 前端和应用服务器部署在ECS 实例上，SLB可以做到负载均衡
* ESS弹性伸缩按需业务创建或释放资源，使您能够获得最优的业务性能和成本支出
* 部署在多可用区RDS上的数据库保证业务的容灾性能

![通用Web应用](https://img.alicdn.com/imgextra/i2/O1CN01FSrA5F1y9XLjVtMhl_!!6000000006536-2-tps-1360-1520.png)

### 在线游戏

高并发、瞬时计算量大的场景，阿里云推荐高主频及GPU服务器实现高计算性能与高图像渲染性能的需求

* 负载均衡处理HTTP请求，并将流量分发到指定的游戏服集群
* 连接服、游戏服、缓存服等通过ESS弹性伸缩按需创建或释放资源
* 部署在多可用区RDS上的数据库保证业务的容灾性能

![在线游戏](https://img.alicdn.com/imgextra/i3/O1CN01G4Mtt91QTVgkjvX55_!!6000000001977-2-tps-1520-1360.png)

### 大数据分析

对于频繁对存储读取的大数据应用场景，阿里云推荐大数据实例及本地盘实例，主从节点皆有性能优异表现

* 业务系统产生日志等数据传输到Hadoop大数据存储进行分析；或用户大数据存在OSS对象存储，并加载到Hadoop大数据系统中进行分析
* 基于ECS大数据实例构建高性价比、海量可扩展的云端Hadoop系统
* 分析结果可以存放在MySQL或NoSQL(HBase/MongoDB/Redis)等数据库，便于用户查询
* 大数据 Bi 及展示

![大数据分析](https://img.alicdn.com/imgextra/i1/O1CN01qvouya1QC6dgl7vKB_!!6000000001939-2-tps-1360-1520.png)

### 深度学习

对于持续且大量的人工神经网络计算的深度学习场景，阿里云推荐GPU实例及AMD实例，不但性能表现卓越，同时大量节省成本

* 在数据层面可以与OSS对象存储、NAS文件存储、云盘等打通，满足深度学习海量训练数据的低成本存储和访问要求
* 通过EMR服务进行数据的预处理
* 通过云监控服务进行GPU资源的监控与告警
* 通过ECS、负载均衡、弹性伸缩、资源编排等快速在云端搭建完整AI深度学习业务系统

![深度学习](https://img.alicdn.com/imgextra/i2/O1CN01bYlY2i1JqgPqaKgOB_!!6000000001080-2-tps-1360-1360.png)

## 产品简介

### 为什么选择云服务器ECS
* 无需自建机房，无需采购以及配置硬件设施。
* 分钟级交付，快速部署，缩短应用上线周期。
* 快速接入部署在全球范围内的数据中心和边界网关协议BGP（Border Gateway Protocol）机房。
* 成本透明，按需使用，支持根据业务波动随时扩展和释放资源。
* 提供GPU和FPGA等异构计算服务器、弹性裸金属服务器以及通用的x86架构服务器。
* 支持通过内网访问其他阿里云服务，形成丰富的行业解决方案，降低公网流量成本。
* 提供虚拟防火墙、角色权限控制、内网隔离、防病毒攻击及流量监控等多重安全方案。
* 提供性能监控框架和主动运维体系。
* 提供行业通用标准API，提高易用性和适用性。 

### 产品架构

云服务器ECS主要包含以下功能组件：

- [实例](https://help.aliyun.com/document_detail/25374.htm#concept-i1k-fv2-5db)：等同于一台虚拟服务器，内含CPU、内存、操作系统、网络配置、磁盘等基础的组件。实例的计算性能、内存性能和适用业务场景由实例规格决定，其具体性能指标包括实例vCPU核数、内存大小、网络性能等。

- [镜像](https://help.aliyun.com/document_detail/25389.htm#concept-qql-3zb-wdb)：提供实例的操作系统、初始化应用数据及预装的软件。操作系统支持多种Linux发行版和多种Windows Server版本。

- [块存储](https://help.aliyun.com/document_detail/63136.htm#concept-pl4-tzb-wdb)：块设备类型产品，具备高性能和低时延的特性。提供基于分布式存储架构的云盘以及基于物理机本地存储的本地盘。

- [快照](https://help.aliyun.com/document_detail/25391.htm#concept-qft-2zw-ydb)：某一时间点云盘的数据状态文件。常用于数据备份、数据恢复和制作自定义镜像等。

- [安全组](https://help.aliyun.com/document_detail/25387.htm#concept-o2y-mqw-ydb)：由同一地域内具有相同保护需求并相互信任的实例组成，是一种虚拟防火墙，用于设置实例的网络访问控制。

- [网络](https://help.aliyun.com/document_detail/61651.htm#concept-nfj-dz2-5db)

  - [专有网络（Virtual Private Cloud）](https://help.aliyun.com/document_detail/34217.htm#concept-kbk-cpz-ndb)：逻辑上彻底隔离的云上私有网络。您可以自行分配私网IP地址范围、配置路由表和网关等。
  - 经典网络：所有经典网络类型实例都建立在一个共用的基础网络上。由阿里云统一规划和管理网络配置。

![云服务器ECS的产品组件架构图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2144684161/p85840.png)

### 产品计费

云服务器ECS的资源中，计算资源（vCPU和内存）、镜像、块存储、公网带宽、快照等资源涉及计费。

- 包年包月：按一定时长购买资源，先付费后使用。
- 按量付费：按需开通和释放资源，先使用后付费。
- 抢占式实例：通过竞价模式抢占库存充足的计算资源，相对按量付费实例有一定的折扣，但是存在回收机制。
- 预留实例券：搭配按量付费实例使用的抵扣券，承诺使用指定配置的实例（包括实例规格、地域可用区等），以折扣价抵扣计算资源的账单。
- 节省计划：搭配按量付费实例使用的折扣权益计划，承诺使用稳定数量的资源（以元/小时为单位衡量），以折扣价抵扣计算资源、系统盘等资源的账单。
- 存储容量单位包：搭配按量付费存储产品使用的资源包，承诺使用指定容量的存储资源，以折扣价抵扣块存储、NAS、OSS等资源的账单。

### 管理工具

通过注册阿里云账号，您可以在任何地域下，通过阿里云提供的以下途径创建、使用或者释放云服务器ECS：

- ECS管理控制台：具有交互式操作的Web服务页面。关于管理控制台的操作，请参见[常用操作导航](https://help.aliyun.com/document_detail/25429.htm#concept-q3w-45w-wdb)。

- ECS API：支持GET和POST请求的RPC风格API。关于API说明，请参见[API参考](https://help.aliyun.com/document_detail/25484.htm#EcsApiWelcome)。以下为调用云服务器ECS API的常用开发者工具：

  - [命令行工具CLI](https://help.aliyun.com/document_detail/110244.htm#concept-rc3-qrc-bhb)：基于阿里云API建立的灵活且易于扩展的管理工具。您可基于命令行工具封装阿里云的原生API，扩展出您需要的功能。
  - [OpenAPI开发者门户](https://next.api.aliyun.com/api/Ecs/2014-05-26)：提供快速检索接口、在线调用API和动态生成SDK示例代码等服务。
  - [阿里云SDK](https://next.api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26)：提供Java、Python、PHP等多种编程语言的SDK。

- [资源编排（Resource Orchestration Service）](https://help.aliyun.com/document_detail/28852.htm#concept-28852-zh)：通过创建一个描述您所需的所有阿里云资源的模板，然后资源编排将根据模板，自动创建和配置资源。

- [运维编排服务（Operation Orchestration Service）](https://help.aliyun.com/document_detail/125604.htm#concept-1181174)：自动化管理和执行运维任务。您可以在执行模板中定义执行任务、执行顺序、执行输入和输出等，通过执行模板达到自动化完成运维任务的目的。

- [Terraform](https://help.aliyun.com/document_detail/91285.htm#concept-twc-3dz-dfb)：能够通过配置文件在阿里云以及其他支持Terraform的云商平台调用计算资源，并对其进行版本控制的开源工具。

- 阿里云App：移动端类型的管理工具。

- [Alibaba Cloud Toolkit](https://help.aliyun.com/product/29966.html)：阿里云针对IDE平台为开发者提供的一款插件，用于帮助您高效开发并部署适合在云端运行的应用。



## 实例

[实例](https://help.aliyun.com/document_detail/108375.html)

### 实例概述

一台ECS实例等同于一台虚拟服务器，内含CPU、内存、操作系统、网络配置、磁盘等基础的组件。您可以使用阿里云提供的控制台、API等管理工具创建和管理ECS实例，像使用本地服务器一样管理ECS实例的状态、应用等，还可以灵活地升级计算、存储等能力。





----



## 专业术语

| 术语                                       | 说明                                       |
| ---------------------------------------- | ---------------------------------------- |
| [ECS实例](https://help.aliyun.com/document_detail/25374.htm#concept-i1k-fv2-5db) | 等同于一台虚拟服务器，内含CPU、内存、操作系统、网络配置、磁盘等基础的组件。  |
| [ECS实例规格](https://help.aliyun.com/document_detail/25378.htm#concept-sx4-lxv-tdb) | 定义了ECS实例在计算性能、存储性能、网络性能等方面的基本属性，但需要同时配合镜像、块存储、网络等配置才能确定一台ECS实例的具体服务形态。 |
| [镜像](https://help.aliyun.com/document_detail/25389.htm#concept-qql-3zb-wdb) | 提供了运行实例所需的信息，包括操作系统、初始化应用数据等。            |
| [公共镜像](https://help.aliyun.com/document_detail/108393.htm#concept-x4k-22r-wgb) | 阿里云官方提供的基础镜像，均已获得正版授权，涵盖Windows Server系统镜像和主流的Linux系统镜像。 |
| [Alibaba Cloud Linux 3](https://help.aliyun.com/document_detail/212631.htm#concept-2068992)  [Alibaba Cloud Linux 2](https://help.aliyun.com/document_detail/111881.htm#concept-rgv-rvd-2hb) | 阿里云官方操作系统，为云上应用程序提供安全、稳定、高性能的定制化运行环境，并进行了针对性深度优化，更加适合阿里云基础设施。 |
| [自定义镜像](https://help.aliyun.com/document_detail/172789.htm#concept-2553000) | 您自行创建或导入的镜像，包含了初始系统环境、应用环境、软件配置等信息，可以节省重复配置的时间。 |
| [块存储](https://help.aliyun.com/document_detail/63136.htm#concept-pl4-tzb-wdb) | 高性能、低时延的块设备，像物理硬盘一样分区格式化并创建文件系统后使用，满足大部分通用业务场景下的数据存储需求。 |
| [云盘](https://help.aliyun.com/document_detail/25383.htm#concept-n1s-rzb-wdb) | 数据块级别的块存储产品，采用分布式三副本机制，为ECS实例提供99.9999999%的数据可靠性保证。 |
| [本地盘](https://help.aliyun.com/document_detail/63138.htm#concept-g3w-qzv-tdb) | ECS实例所在物理机上的本地硬盘设备，存储I/O性能、海量存储的性价比极高，但数据可靠性取决于物理机的可靠性，存在单点故障风险。 |
| [快照](https://help.aliyun.com/document_detail/25391.htm#concept-qft-2zw-ydb) | 某一时间点云盘数据状态的备份文件，用于备份或者恢复整个云盘。           |
| [安全组](https://help.aliyun.com/document_detail/25387.htm#concept-o2y-mqw-ydb) | 一种虚拟防火墙，您可以基于安全组控制实例的入流量和出流量。            |
| [SSH密钥对](https://help.aliyun.com/document_detail/51792.htm#concept-j33-vqw-ydb) | 一种安全便捷的登录认证方式，由公钥和私钥组成，仅支持Linux实例。       |
| [实例RAM角色](https://help.aliyun.com/document_detail/54235.htm#concept-kbp-r1t-xdb) | ECS实例通过实例RAM角色获得该角色拥有的权限，可以基于临时安全令牌STS（Security Token Service）访问指定云服务的API和操作指定的云资源，安全性更高。 |
| [专有网络](https://help.aliyun.com/document_detail/34217.htm#concept-kbk-cpz-ndb) | 您基于阿里云创建的自定义私有网络，不同专有网络之间通过隧道在逻辑上彻底隔离。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等。 |
| [弹性网卡](https://help.aliyun.com/document_detail/58496.htm#concept-xzg-mgt-xdb) | 一种独立的虚拟网卡，可以绑定到ECS实例或从ECS实例解绑，实现业务的灵活扩展和迁移。 |
| [实例启动模板](https://help.aliyun.com/document_detail/73916.htm#concept-fbp-sy5-xdb) | 包含了ECS实例的配置信息，使用实例启动模板创建ECS实例可以免去重复配置的操作。 |
| [部署集](https://help.aliyun.com/document_detail/91258.htm#concept-1846521) | 部署集支持高可用策略，部署集内实例会严格分散在不同的物理服务器上，保证业务的高可用性和底层容灾能力。 |
| [专有宿主机](https://help.aliyun.com/document_detail/68563.htm#concept-yqx-czm-tdb) | 一台由单租户独享物理资源的云主机，具有满足严格的安全合规要求、允许自带许可证（BYOL）上云等优势。 |
| [弹性供应组](https://help.aliyun.com/document_detail/120020.htm#concept-287169) | 用于快速部署多可用区、多实例规格的ECS实例集群，通过多种供应策略组合使用抢占式实例和按量付费实例，满足对低成本和高稳定性的要求。 |
| [标签](https://help.aliyun.com/document_detail/25477.htm#concept-jzp-qtd-zdb) | 由一对键值（Key-Value）组成。使用标签标识具有相同特征的资源后，例如所属组织或用途相同的资源，您可以基于标签方便地检索和管理资源。 |
| [资源组](https://help.aliyun.com/document_detail/100034.htm#concept-fdn-wtm-cgb) | 供您从业务角度管理跨地域、跨产品的资源，并支持针对资源组的权限管理。       |
| [云助手](https://help.aliyun.com/document_detail/64601.htm#concept-qg3-5dx-ydb) | 阿里云提供的自动化运维工具，无需登录即可完成在ECS实例上执行命令、向ECS实例发送文件等操作。 |
| [系统事件](https://help.aliyun.com/document_detail/66574.htm#concept-gdc-tyz-xdb) | 影响ECS实例运行状态的计划底层运维事件或非预期维修事件，需要进行重启、停止或释放ECS实例等操作。系统事件会及时发送通知、应对措施和事件周期等信息，方便您提前完成备份数据等准备工作。 |

## 学习进度

| Date     | Progress                                                     |      |
| -------- | ------------------------------------------------------------ | ---- |
| 2022/4/2 | [快速入门](https://help.aliyun.com/document_detail/163467.html?spm=a2c4g.11186623.0.0.1d46a665VNCwWZ) |      |
| 2022/4/9 | [实例](https://help.aliyun.com/document_detail/108375.html)  |      |
|          |                                                              |      |

