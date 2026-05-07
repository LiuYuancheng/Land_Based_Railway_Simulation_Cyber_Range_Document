# Fast Way to Setup an ERP(IT) System For the Critical Infra Cyber Range [ Land Based Railway System ]

[us English](1_Fast_Setup_IT_ERP_System.md) | **cn 中文**

**项目设计目的**：在用于攻防网络演习的网络靶场/数字孪生系统（如电网、机场跑道、交通信号灯）中，红/蓝/黄队通常更侧重于运营技术（OT）系统，但有时也需要构建一个简单的公司IT系统（如内部ERP和HR服务），以模拟通过企业IT网络中的弱点进行初始攻击访问，然后转向OT网络，例如IT到OT的攻击链、凭据泄露、横向移动以及对配置错误的企业服务的利用。

![](img/s_01.png)

如ISA-95/IEC62264系统架构的6个层级（level0-5）所示，IT层（level4-5）代表管理业务运营的企业网络。本项目旨在通过使用开源Dolibarr ERP和CRM软件包，为陆基铁路网络靶场系统在数小时内提供一种快速实用的方法来构建基于ERP的IT环境。本文分为三个主要部分：

- **系统架构**：介绍整体网络靶场架构、网络演习网络拓扑，并解释ERP系统在铁路环境中的作用和定位。
- **ERP软件设置**：提供在网络靶场中安装和部署Dolibarr ERP软件包的分步说明，包括与其他系统组件的集成。
- **ERP功能配置**：配置主要功能特性，如人力资源管理、请假申请、协作工作流和工资核算。然后使用人工智能创建一些信息，使ERP系统看起来像真实的系统。

**致谢**：本项目中使用的ERP系统是基于未经修改的Dolibarr ERP和CRM版本构建的。所有使用均严格遵守[Dolibarr许可文档](https://wiki.dolibarr.org/index.php/FAQ_What_is_Dolibarr_licence_%3F)和[Dolibarr版权规则](https://wiki.dolibarr.org/index.php/Rules_to_use_the_brand_name_"Dolibarr")中定义的许可条款和品牌指南。

```python
# Author:      Yuancheng Liu
# Created:     2026/03/16
# Version:     v_0.0.1
# Copyright:   Copyright (c) 2026 LiuYuancheng
# License:     GNU/GPL v3+ (Same as the DOLIBARR license)
```

**Table of Contents**

[TOC]

- [Fast Way to Setup an ERP(IT) System For the Critical Infra Cyber Range [ Land Based Railway System ]](#fast-way-to-setup-an-erp-it--system-for-the-critical-infra-cyber-range---land-based-railway-system--)
    + [1. 項目簡介](#1-----)
      - [1.1 摘要](#11---)
      - [1.2 背景信息](#12-----)
    + [2. 系统架构](#2-----)
      - [2.1 架构与功能概述](#21--------)
      - [2.2 系统网络配置](#22-------)
    + [3. 在Ubuntu虚拟机上安装Dolibarr](#3--ubuntu------dolibarr)
    + [4. 配置Dolibarr功能模块](#4---dolibarr----)
      - [4.1 配置公司信息](#41-------)
      - [4.2 配置人力资源（HR）模块](#42--------hr---)
      - [4.3 配置客户关系管理 (CRM)](#43-----------crm-)
      - [4.4 配置财务模块](#44-------)
      - [4.5 配置多模块工具和集成](#45-----------)
      - [4.6 配置高级/自定义模块](#46-----------)

------

### 1. 項目簡介

本项目的目标是将企业资源规划（ERP）系统集成到陆基铁路网络靶场系统的企业IT层，以模拟真实世界的企业运营以及工业公司。开源Dolibarr ERP和CRM平台将设置在铁路系统ISA-95架构的level4企业IT层，届时该平台能够模拟铁路公司的基本业务功能，如人力资源、财务和内部行政管理。特别是，它允许模拟真实世界的攻击路径，即攻击者最初通过入侵企业IT系统，然后转向运营网络。

整体系统架构，包括ERP系统在网络靶场中的定位，如下图所示：

![](img/s_02.png)

#### 1.1 摘要

在用于关键基础设施（如电网、机场和铁路系统）的现代网络靶场和数字孪生环境中，网络安全演习通常侧重于运营技术（OT）工业控制系统，如SCADA网络和OT现场设备。但在许多真实世界的网络事件中，由于OT环境与互联网隔离，攻击者通常需要通过企业IT环境中的一些漏洞或错误配置获得初始访问权限，然后才能接触OT系统。因此，在公司外部网络和OT网络之间建立一个IT系统对于用于网络演习的网络靶场是必要的。

从系统设计的角度来看，不同行业和公司的大多数企业IT环境都非常相似。人力资源、财务和行政平台等核心系统遵循标准化工作流，无论组织是在能源、交通还是制造业运营。与构建需要深厚领域特定知识的OT系统不同，通过使用通用解决方案实现的IT系统几乎可以在不牺牲真实性的情况下满足网络演习的要求。这就是我直接使用开源ERP（企业资源规划）软件Dolibarr来构建IT环境的原因。这种方法能够快速部署功能齐全且真实的企业环境，支持集成IT/OT网络安全场景，而无需进行大量的定制或开发工作。

#### 1.2 背景信息

**1.2.1 陆基铁路网络靶场系统背景**

陆基铁路IT/OT网络安全测试平台是按照ISA-95/IEC62264标准设计和开发的数字孪生式系统，专为网络安全研究、红蓝队演习、专业培训、威胁检测和蜜罐实验而构建。该系统旨在模拟铁路公司的IT和OT环境，同时还能在受控环境中可视化网络攻击影响。

该网络靶场能够模拟真实的运营场景，包括自动生成系统中类似人类的活动。这种动态行为显著增强了网络靶场的真实性，使其与真实的铁路企业环境非常相似。该平台已在多次国际网络安全演习中得到应用。欲了解更多详细信息，请参阅项目文档库：https://github.com/LiuYuancheng/Land_Based_Railway_Simulation_Cyber_Range_Document

**1.2.2 Dolibarr ERP和CRM软件背景**

Dolibarr ERP和CRM是一个现代化的模块化开源ERP和CRM解决方案，旨在管理广泛的组织活动，包括联系人、发票、订单、库存、日程安排和人力资源。

Dolibarr主要使用PHP开发并增强了JavaScript，适用于各种规模的组织——从小企业到大型企业，以及基金会和自由职业者。其模块化架构、易于部署和活跃的开源社区使其成为在网络靶场中快速构建真实企业IT环境的理想选择。欲了解更多详情，请参阅官方仓库：https://github.com/Dolibarr/dolibarr



------

### 2. 系统架构

#### 2.1 架构与功能概述

陆基铁路网络靶场系统按照ISA-95 / IEC 62264架构设计，如下图所示的六层ISA-95结构图。在此架构中，Dolibarr ERP和CRM系统部署在第4级企业区，作为公司内部业务运营平台，包括为员工提供人力资源管理、行政工作流和财务运营等服务。网络演习可以配置不同的漏洞和攻击入口点，这些漏洞和入口点可能会传播到较低的OT层。

![](img/s_03.png)

为了增强真实性，网络靶场通过集群用户模拟器（基于脚本的引擎）集成了自动化用户行为。这些模拟脚本在IT网络中生成动态和持续的活动，模仿各种铁路公司角色（如IT支持工程师、办公室职员、铁路总部操作员、列车司机/安全检查员）的日常操作。此架构的主要组件包括：

- **铁路企业网络环境**：一个虚拟化基础设施，复制企业级网络元素，包括服务器、终端、防火墙、路由器和交换机。
- **铁路公司员工ERP系统**：具有前端应用程序和后端数据库的ERP软件，提供人力资源管理、客户关系、财务、票务和公司活动等主要功能。
- **员工活动模拟引擎**：一个自动化用户活动生成器，模拟真实用户行为，在不同角色之间产生网络流量和系统交互。

#### 2.2 系统网络配置

如第1节（图1）所示，Dolibarr ERP和CRM系统部署在网络靶场的企业IT子网（第4级 – 企业区）中，在架构中以浅蓝色部分突出显示。尽管Dolibarr建议将所有组件部署在单个服务器（或云实例）上以简化管理并提高稳定性，但本项目有意采用分布式三虚拟机（一个应用程序前端虚拟机、一个数据库后端虚拟机和一个文件存储虚拟机）架构，以便在网络演习期间通过以下攻击向量轻松受到攻击：

- 针对前端服务器的Web应用程序攻击
- 数据库利用和数据泄露场景
- 凭据收集和虚拟机之间的横向移动
- 配置错误的文件服务和不安全的数据传输通道

详细的网络配置如下图所示：

![](img/s_04.png)

每个虚拟机的主要功能包括：

- **ERP前端服务器**：此虚拟机托管Dolibarr应用程序和Web界面，提供对所有ERP功能模块（人力资源、财务、行政等）的访问。它通过内部网络或Web门户作为用户的主要入口点。
- **ERP后端服务器（数据库服务器）**：此虚拟机使用MySQL运行数据库服务，存储所有ERP相关数据，包括用户信息、交易和系统配置。将数据库与应用层分离反映了常见的企业实践，并支持以数据库为中心的攻击场景。
- **ERP文件服务器**：此虚拟机负责文件存储和处理用户上传内容。由于原生的Dolibarr FTP模块不是免费提供的，因此使用了一个轻量级基于Python的FTP服务。

所有三个虚拟机通过企业网络路由器/交换机连接，允许内部铁路员工无缝访问ERP服务。网络通过DMZ防火墙进一步保护和分段，该防火墙控制内部网络与外部访问点（如ERP Web门户）之间的流量。对于邮件服务器，我们使用一个也设置在子网内的Postfix邮件服务器。由于Dolibarr推荐Gmail，因此目前Dolibarr的员工账户我使用普通的Gmail账户。



------

### 3. 在Ubuntu虚拟机上安装Dolibarr

要在Ubuntu系统上安装Dolibarr，官方网站在下载链接中提供了安装`*.deb`软件包：https://www.dolibarr.org/downloads.php。但是当您下载并安装它时，在安装后的第一步可能会看到“连接数据库失败”错误，如下图所示：

![](img/s_05.png)

本节提供了一种结构化方法，用于在多个虚拟机（前端、数据库和文件服务器）上安装和配置Dolibarr，以及解决此问题的故障排除步骤。

**3.1 安装LAMP Stack（前端虚拟机）**

在安装Dolibarr之前，请确保前端虚拟机具有完整的LAMP Stack（Apache、PHP和数据库客户端库）：

```
sudo apt update
sudo apt install apache2 mariadb-server php libapache2-mod-php php-mysql php-curl php-intl php-gd php-json php-mbstring -y
```

**3.2 下载并安装Dolibarr**

从SourceForge网站下载最新的`.deb`软件包：[https://sourceforge.net/projects/dolibarr/files/Dolibarr%20installer%20for%20Debian-Ubuntu%20%28DoliDeb%29/](https://sourceforge.net/projects/dolibarr/files/Dolibarr installer for Debian-Ubuntu (DoliDeb)/)，然后使用以下命令安装软件包：

```bash
sudo dpkg -i dolibarr_x.y.z-w.w_all.deb
```

如果出现依赖问题，请使用以下命令解决：

```bash
sudo apt-get install -f
```

**3.3 配置数据库服务器（后端虚拟机）**

在数据库虚拟机上，安装并保护MySQL（或MariaDB）：

```bash
sudo mysql_secure_installation
```

登录到数据库：

```bash
sudo mysql -u root -p
```

创建Dolibarr数据库和用户：

```sql
CREATE DATABASE dolibarr;
CREATE USER 'dolibarruser'@'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON dolibarr.* TO 'dolibarruser'@'%';
FLUSH PRIVILEGES;
EXIT;
```

使用`'%'`而不是`'localhost'`以允许前端虚拟机进行远程连接。

通过编辑`/etc/mysql/mariadb.conf.d/50-server.cnf`并设置以下内容，确保数据库服务器配置为接受远程连接：

```bash
bind-address = 0.0.0.0
```

重启数据库服务`sudo systemctl restart mysql`，并确保虚拟机之间（防火墙/安全组）的3306端口已打开。

**3.4 配置Dolibarr使用远程数据库**

默认情况下，Dolibarr假定数据库托管在本地。在多虚拟机设置中，您必须手动更新配置。在前端虚拟机上编辑Dolibarr配置文件：

```bash
sudo vim /etc/dolibarr/conf.php
```

找到数据库主机设置，并将`localhost`替换为**数据库虚拟机的IP地址**，如下图所示：

![](img/s_06.png)

**3.5 通过Web界面完成安装**

配置完成后，打开浏览器并导航到`http://localhost/dolibarr`或`http:///dolibarr`，重新执行第一步填写信息，然后您会看到错误已清除，如下图所示：

![](img/s_08.png)

现在Dolibarr已准备好在网络靶场中使用。我们需要填写一些员工信息并启用人力资源管理系统和请假系统等功能模块，以便它能胜任铁路公司中ERP系统的角色。



------

### 4. 配置Dolibarr功能模块

本节主要涉及通过管理仪表板添加信息和启用铁路公司中使用的Dolibarr ERP和CRM系统的功能模块。有关详细使用指南，您可以参考官方文档和教程：

- https://wiki.dolibarr.org/index.php/User_documentation
- https://www.dolibarr.org/dolibarr-tutorial-videos.php

使用上一节中创建的**管理员账户**登录以访问设置仪表板。我配置的主要功能如下图所示：

![](img/s_07.png)

#### 4.1 配置公司信息

导航到**设置 → 公司/组织**，然后填写基本信息，如铁路公司名称、地址和联系方式、官方电子邮件和网站、电话和传真，并上传公司标志，如下图所示：

![](img/s_09.png)

接下来，转到**显示设置**以调整UI外观，自定义主题、布局和CSS样式，如下图所示：

![](img/s_10.png)

出于网络安全培训和演习目的，您可以通过导航到**安全设置**有意削弱某些安全控制，如下图所示：

![](img/s_11.png)

这允许使用弱凭据（例如，`123456`），这些凭据可以在演习期间作为**攻击入口点**。

设置公司信息后，主门户登录页面将显示公司名称、标志和概览图片，如下图所示：

![](img/s_12.png)

#### 4.2 配置人力资源（HR）模块

导航到**设置 → 模块/应用程序**

以激活以下模块：

- **请假申请管理** – 管理员工请假申请和审批
- **费用报销** – 模拟报销工作流程
- **招聘管理** – 管理职位发布和招聘流程
- **人力资源管理** – 核心员工管理工具

![](img/s_14.png)

接下来，创建用户并为员工账户分配角色（例如，`staff_alice` 作为 OCC 操作员），并根据职位角色分配权限，如下所示：

![](img/s_15.png)

现在我们登录 Alice 账户，模拟她提交请假申请并为管理组设置审批：

![](img/s_16.png)

然后以管理员/经理身份重新登录，审查并批准我们刚才创建的 Alice 的请假申请：

![](img/s_17.png)

#### 4.3 配置客户关系管理 (CRM)

为了模拟乘客互动和服务反馈，请启用与 CRM 相关的模块“第三方（客户）”和“工单系统”，以便客户报告异常情况并反馈服务，如下所示：

![](img/s_18.png)

在工单系统中，我们需要配置公共服务接口，以便乘客可以使用，如下所示：

![](img/s_19.png)

之后，乘客可以访问工单系统页面，如下所示：

![](img/s_20.png)

此模块对于模拟外部攻击面、输入验证漏洞和社会工程场景特别有用。

#### 4.4 配置财务模块

出于模拟目的，只需要基本的财务功能。我启用了薪资管理部分：

![](img/s_21.png)

之后，我们可以登录财务组下的管理员或用户账户，为员工分配薪资并模拟工资发放，如下所示：

![](img/s_22.png)

#### 4.5 配置多模块工具和集成

为了提高可扩展性和真实性，请启用支持工具：

- **数据导入/导出** ：允许在多个 cyber range 部署中重用 ERP 数据集
- **AI 集成**：连接到本地 AI 服务（例如，通过 Ollama）
- **电子邮件配置** ：使用 Gmail 或 Outlook 等服务配置 SMTP https://wiki.dolibarr.org/index.php/Setup_EMails。
- **协作工具** ：启用事件/日历模块

![](img/s_23.png)

要启用带有自定义 AI 服务的 AI，我们可以将该功能与使用 Ollama 服务的本地 GPU 连接起来。

![](img/s_24.png)

对于协作工作，我只激活了事件协作，如下所示：

![](img/s_25.png)

然后作为管理员，我们可以创建一个事件，例如简报会议，并通过将其添加到日历事件中来为不同的铁路员工分配出席人员：

 ![](img/s_28.png)

现在我们几乎拥有一个简单铁路公司所需的所有模块，下一步是填写员工信息，我们可以使用 AI 生成员工信息。要使用 Python 脚本在 ERP 系统中生成操作，例如在 HR 系统中申请请假，我们需要使用库 https://pypi.org/project/dolibarr/

```python
 from dolibarr import Dolibarr
 api_url = 'http://your-url/dolibarr/htdocs/api/index.php/'
 api_key = 'custom_API-Key'
 # Connection to dolibarr
 dolibarr_inst = Dolibarr(api_url, api_key)
```

然后我们按照此链接中的示例 https://wiki.dolibarr.org/index.php/Module_Web_Services_API_REST_(developer)#PHP 调用相关 API 来生成事件或操作。

#### 4.6 配置高级/自定义模块

为了扩展功能（例如，**双因素认证 (2FA)**），您需要购买额外的模块，然后下载 zip 文件并从 Dolibarr 市场安装：https://www.dolistore.com/index.php?l=en。

购买并下载所需模块，然后按照以下说明安装：https://wiki.dolibarr.org/index.php/Module_TwoFactorAuth

![](img/s_27.png)

在此阶段之后，ERP 系统已完全配置，可以模拟铁路公司的企业 IT 环境。它包括：

- 真实的组织结构和用户角色
- HR、CRM 和财务工作流程
- 外部交互接口
- 自动化和 AI 生成的数据

这完成了网络靶场的 ERP 设置，将其转变为一个**动态、交互式且可攻击的 IT 环境**，适用于高级网络安全演练。



Thanks for spending time to check the article detail, if you have any question and suggestion or find any program bug, please feel free to message me. Many thanks if you can give some comments and share any of the improvement advice so we can make our work better ~



------

>  最后编辑者：LiuYuancheng (liu_yuan_cheng@hotmail.com)，日期：2026/03/20。如有任何问题，请给我留言。