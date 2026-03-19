# Fast Way to Setup a ERP(IT) System For a Critical Infra Cyber Range [ Land Based Railway System ]

**Project Design Purpose** : For the cyber range/twin (such as Power Grid, Airport Runway, Traffic Lights) used in the attack and defense cyber exercise, most of time the Red/Blue/Yellow Team will focus more on the Operational Technology (OT) system, but some times there are also requirements for building a simple company IT system (such as the internal ERP & HR service) to simulate the attack initial access through weaknesses in the corporate IT environment before pivoting into OT networks such as  IT-to-OT attack chains, credential compromise, lateral movement, and exploitation of misconfigured enterprise services.

As shown in the 6 layers (lvl0-5) of ISA-95/IEC62264 System architecture, the IT layer (level4-5) represents the corporate network where business operations are managed. This project aims to provide a fast and practical approach to build such an ERP-based IT environment for OT cyber twin system in several hours by using the opensource DOLIBARR ERP & CRM package for the Land Based Railway Cyber Range System. This article is structured into three main sections:

- **System Architecture**: Introduces the overall cyber range architecture, cyber exercise network topology and explains the role and positioning of the ERP system within the railway environment.
- **ERP Software Setup**: Provides step-by-step instructions to install and deploy Dolibarr within the cyber range, including integration with other system components.
- **ERP Function Configuration**: The step to configure main function features such as HR management, leave application and approval workflows, and payroll. Then use AI to create some information so the ERP system looks similar as a real one.

**Acknowledgement**: The ERP system used in this project is built with the unmodified version of Dolibarr ERP & CRM. All usage strictly follows the licensing terms and branding guidelines defined by the   [DOLIBARR License Doc]( https://wiki.dolibarr.org/index.php/FAQ_What_is_Dolibarr_licence_%3F) and [[DOLIBARR Copy Right Rules](https://wiki.dolibarr.org/index.php/Rules_to_use_the_brand_name_%22Dolibarr%22). 

```python
# Author:      Yuancheng Liu
# Created:     2026/03/16
# Version:     v_0.0.1
# License:     GNU/GPL v3+ (Same as the DOLIBARR license)
```

**Table of Contents**

[TOC]

------

### 1. Introduction

The objective of this project is integrate the opensource Dolibarr Enterprise Resource Planning (ERP) system into the  Level 5 (enterprise IT) layer defined in the ISA-95 architecture for the Land Based Railway Cyber Range System which developed for Critical infra cyber excise. So the cyber range can provide the core business operations simulation function for a railway company such as human resources, finance, and internal administration, thereby enabling more comprehensive attack-and-defense scenarios that span both IT and OT domains. The system structure overview diagram is shown below:

![](img/s_02.png)

#### **1.1 Abstract **

In modern cyber range and digital twin environments for critical infrastructure—such as power grids, airports, and land-based railway systems—the primary focus of cyber attack and defense exercises often centers on Operational Technology (OT) layers. These include industrial control systems, SCADA networks, and field devices where real-time operations are managed. However, real-world cyber incidents increasingly demonstrate that initial access vectors frequently originate not from OT systems directly, but from vulnerabilities within the corporate IT environment. 

As for most of the company, the IT system are nearly same, such as the HR system, no matter whether it is a power grid company or a railway company, there will be no deferent, so unlike building the OT system which needs a lot domain knowledge a IT system for most of the cyber range can use a general one.  So that's why I use the opensource ERP(enterprise resource planning) software Dolibarr to build the IT environment for the Land Based Railway Cyber Range System I developed. 

#### **1.2 Background Information**

**1.2.1 Background of the Land Based Railway Cyber Range System**

The Railway [land-based] IT/OT System Cyber Security Test Platform is a simplified and straightforward digital twin-style Cyber Range, purpose-built for research, cyber exercises, red-blue confrontations, professional security training, threat detection, and cyber honeypot activities. What sets our system apart is its unique capability to not just emulate the IT and OT network environment of a railway company but also to virtualize real-world scenarios and showcasing the effects of cyber attacks. Moreover, our simulation system integrates automated robotic human activities generation feature, adding a dynamic layer that brings the range closer to mirroring the operations of a "live" railway company. It is used in several international cyber execise. For the detail introduction, please refer to the project document wiki repo: https://github.com/LiuYuancheng/Land_Based_Railway_Simulation_Cyber_Range_Document

**1.2.2 Background of the Dolibarr ERP**

Dolibarr ERP & CRM is a modern software package that helps manage your organization's activities (contacts, quotes, invoices, orders, stocks, agenda, human resources, ecm, manufacturing…).

It's an Open-Source Software suite (written in PHP with JavaScript enhancements) designed for small, medium or large companies, foundations and freelancers. For the detail introduction please refer to the Dolibarr official repo: https://github.com/Dolibarr/dolibarr



------

### 2. System Architecture

#### 2.1 Architecture and Functions Overview

The Land Based Railway Cyber Range System Follows the  ISA-95/IEC62264 System architecture as shown below, and the Dolibarr  ERP system in configured in the `Level 4 Enterprise Zone` which provide the service for the company's staffs.  

![](img/s_03.png)

With some auto user simulation scripts provide by the Cluster User Simulator (Script) This IT-network cyber range project will simulate the normal corporate network of the railway company with several different kinds of staff's daily work such as IT-Support-Engineer, Officer Staff, Railway HQ operator, Train driver / safety checker. The main components includes: 

- Railway company corporate network environment (virtualize the railway company infrastructure: network, computer, node, firewall, router, switches)
- Railway company staff activities auto generator (virtual the railway company staff: IT-Support-Engineer, Officer Staff, Railway HQ operator, Train driver / safety checker, maintenance engineer)



#### 2.2 System Network Configuration 

As shown in the introduction section Figure1, the Dolibarr will be set in the forth subnet corporation network (light blue section) in the cyber range. Dolibarr recommends to set all the components in one server or cloud to increase the stability. But to make it be easily attacked during the cyber exercise, I will split configure the system in 3 VM (one application front end VM, one database backend VM and one File storage VM). The network configure is shown below:

![](img/s_04.png)







