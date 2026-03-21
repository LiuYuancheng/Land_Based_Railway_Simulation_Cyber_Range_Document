# Fast Way to Setup a ERP(IT) System For a Critical Infra Cyber Range [ Land Based Railway System ]

**Project Design Purpose** : For the cyber range/twin (such as Power Grid, Airport Runway, Traffic Lights) used in the attack and defense cyber exercise, most of time the Red/Blue/Yellow Team will focus more on the Operational Technology (OT) system, but some times there are also requirements for building a simple company IT system (such as the internal ERP & HR service) to simulate the attack initial access through weaknesses in the corporate IT environment before pivoting into OT networks such as  IT-to-OT attack chains, credential compromise, lateral movement, and exploitation of misconfigured enterprise services.

![](img/s_01.png)

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

The objective of this project is to integrate a Enterprise Resource Planning (ERP) system into the enterprise IT layer of the Land Based Railway Cyber Range System to simulate the real-world corporate operations alongside industrial processes. The open-source Dolibarr ERP & CRM platform used to setup in the level4 enterprise IT layer of the railway system's ISA-95 architecture, then the platform is able to simulate essential business functions of a railway company—such as human resources, finance, and internal administration.  This addition significantly enhances the realism of the environment and enables more comprehensive cyber attack-and-defense scenarios that span both IT and OT domains. In particular, it allows simulation of real-world attack paths where adversaries initially compromise enterprise IT systems before pivoting into operational networks.

The overall system architecture, including the positioning of the ERP system within the cyber range is shown below :

![](img/s_02.png)

#### **1.1 Abstract **

In the modern cyber range and digital twin environments for critical infrastructure—such as power grids, airports, and railway systems—cybersecurity exercises have normally focused on Operational Technology (OT) industrial control system such as SCADA networks and field devices. But in many real-world cyber incidents, as the OT environment is isolated from the internet, the attackers often need to gain initial access through some vulnerabilities or misconfiguration in the corporate IT environment then can touch the OT systems. So have a IT system between the company outside network and OT network is necessary for a cyber range used for cyber exercise.

From a system design view, most enterprise IT environments across different industries and companies are very similar. The core systems such as HR, finance, and administrative platforms follow standardized workflows regardless of whether the organization operates in energy, transportation, or manufacturing. Unlike OT systems, which require deep domain-specific knowledge, the IT systems implemented by using the generalized solutions without sacrificing realism can almost full fill the requirement of cyber exercise. That's why I use the opensource ERP(enterprise resource planning) software Dolibarr to build the IT environment directly. And this approach enables rapid deployment of a functional and realistic enterprise environment, supporting integrated IT/OT cybersecurity scenarios without the need for extensive customization or development effort.

#### 1.2 Background Information

**1.2.1 Background of the Land-Based Railway Cyber Range System**

The Land-Based Railway IT/OT Cyber Security Test Platform is a cyber twin-style design and developed under the ISA-95/IEC62264 standard, purpose-built for cybersecurity research, red-blue team exercises, professional training, threat detection, and honeypot experimentation. The system is designed to emulate both IT and OT environments of a railway company, while also enabling the visualization of cyber attack impacts in a controlled setting.

The cyber is able to simulate realistic operational scenarios, including automated generation of human-like activities within the system. This dynamic behavior significantly enhances the fidelity of the cyber range, making it closely resemble a live railway enterprise environment. The platform has been utilized in multiple international cybersecurity exercises. For more detailed information, refer to the project documentation repository: https://github.com/LiuYuancheng/Land_Based_Railway_Simulation_Cyber_Range_Document

**1.2.2 Background of the Dolibarr ERP & CRM Software**

Dolibarr ERP & CRM is a modern and modular open-source ERP and CRM solution designed to manage a wide range of organizational activities, including contacts, invoicing, orders, inventory, scheduling, and human resources.

Developed primarily in PHP with JavaScript enhancements, Dolibarr is suitable for organizations of various sizes—from small businesses to large enterprises, as well as foundations and freelancers. Its modular architecture, ease of deployment, and active open-source community make it an ideal choice for rapidly building a realistic enterprise IT environment within a cyber range. For more details, refer to the official repository: https://github.com/Dolibarr/dolibarr



------

### 2. System Architecture

#### 2.1 Architecture and Functions Overview

The Land-Based Railway Cyber Range System is designed in accordance with the ISA-95 / IEC 62264 architecture as shown below six layers ISA-95 structure diagram. Within this architecture, the Dolibarr ERP & CRM system is deployed in the Level 4 Enterprise Zone, where it serves as the company internal platform for business operations included the services to staff such as human resources management, administrative workflows, and financial operations. And the cyber exercise can configure different vulnerabilities and attack entry points that may propagate to lower OT layers. 

![](img/s_03.png)

To enhance realism, the cyber range incorporates automated user behavior through the Cluster User Simulator (script-based engine). These simulation scripts generate dynamic and continuous activities across the IT network, mimicking the daily operations of various railway company roles such IT-Support-Engineer, Officer Staff, Railway HQ operator, Train driver / safety checker. The main components of this architecture include:

- **Railway Corporate Network Environment**: A virtualized infrastructure that replicates enterprise-grade network elements, including servers, endpoints, firewalls, routers, and switches.
- **Railway ERP System**: The ERP software with the front end application and back end data base provide the main function of HRM, customer relationship, financial, ticketing and company event.
- **Staff Activity Simulation Engine**: An automated user activity generator that emulates realistic user behavior, producing network traffic and system interactions across different roles.

#### 2.2 System Network Configuration 

As shown in Section 1 (Figure 1), the Dolibarr ERP & CRM system is deployed within the corporate IT subnet (Level 4 – Enterprise Zone) of the cyber range, highlighted as the light-blue segment in the architecture. Although Dolibarr recommends deploying all components on a single server (or cloud instance) to simplify management and improve stability, this project intentionally adopts a distributed three VM (one application front end VM, one database backend VM and one File storage VM) architecture so it can be easily attacked during the cyber exercise with below attack vector:

- Web application attacks targeting the front-end server
- Database exploitation and data exfiltration scenarios
- Credential harvesting and lateral movement between VMs
- Misconfigured file services and insecure data transfer channels

The detailed network configuration is illustrated below:

![](img/s_04.png)

The main function of each VM includes:

- **ERP Front-End Server** : This VM hosts the Dolibarr application and web interface, providing access to all ERP functional modules (HR, finance, administration, etc.). It acts as the primary entry point for users via the internal network or web portal.

- **ERP Back-End Server (Database Server)** : This VM runs the database service using MySQL, which stores all ERP-related data, including user information, transactions, and system configurations. Separating the database from the application layer reflects common enterprise practices and enables database-focused attack scenarios.
- **ERP File Server** : This VM is responsible for file storage and handling user-uploaded content. As the native Dolibarr FTP module is not freely available, a lightweight Python-based FTP service is used.

All three VMs are connected through the corporate network router/switch, allowing internal railway staff to access ERP services seamlessly. The network is further protected and segmented by a DMZ firewall, which controls traffic between the internal network and external access points such as the ERP web portal. For the email server we use a Postfix email server also set inside the subnet. And as Dolicarr recommend Gmail, so currently for the Dolicarr's staff account I use the normal Gmail account. 

------

### 3. Install Dolibarr on Ubuntu VMs

To install the Dolibarr on Ubuntu System, the official web provides the installation `*.deb` package in the download link : https://www.dolibarr.org/downloads.php. But when you download and install it, you may see the "Connect to database failed" error after the step1 of the post install as shown below:

![](img/s_05.png)

This section provides a structured approach to installing and configuring Dolibarr across multiple VMs (front-end, database, and file server), along with troubleshooting steps to resolve this issue.

**3.1 Install LAMP Stack (Front-End VM)**

Before installing Dolibarr, ensure the front-end VM has a complete LAMP stack (Apache, PHP, and database client libraries):

```bash
sudo apt update
sudo apt install apache2 mariadb-server php libapache2-mod-php php-mysql php-curl php-intl php-gd php-json php-mbstring -y
```

**3.2 Download and Install Dolibarr**

Download the latest `.deb` package from the sourceforge website: https://sourceforge.net/projects/dolibarr/files/Dolibarr%20installer%20for%20Debian-Ubuntu%20%28DoliDeb%29/, then Install the package using:

```bash
sudo dpkg -i dolibarr_x.y.z-w.w_all.deb
```

If dependency issues occur, resolve them with:

```
sudo apt-get install -f
```

**3.3 Configure Database Server (Back-End VM)**

On the database VM, install and secure MySQL (or MariaDB):

```
sudo mysql_secure_installation
```

Log in to the database:

```
sudo mysql -u root -p
```

Create the Dolibarr database and user:

```mysql
CREATE DATABASE dolibarr;
CREATE USER 'dolibarruser'@'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON dolibarr.* TO 'dolibarruser'@'%';
FLUSH PRIVILEGES;
EXIT;
```

Use `'%'` instead of `'localhost'` to allow remote connections from the front-end VM.

Ensure the database server is configured to accept remote connections by editing  `/etc/mysql/mariadb.conf.d/50-server.cnf` and setting:

```bash
bind-address = 0.0.0.0
```

Restart the database service `sudo systemctl restart mysql` and  ensure port 3306 is open between VMs (firewall/security group).

**3.4 Configure Dolibarr to Use Remote Database**

By default, Dolibarr assumes the database is hosted locally. In a multi-VM setup, you must manually update the configuration. Edit the Dolibarr configuration file on the front-end VM:

```
sudo vim /etc/dolibarr/conf.php
```

Locate the database host setting and replace `localhost` with the **IP address of the database VM**, as shown below:

![](img/s_06.png)

**3.5 Complete Installation via Web Interface**

Once configuration is complete, open a browser and navigate to `http://localhost/dolibarr` or `http://<frontend_vm_ip>/dolibarr`, Redo the step1 to fill in the information then you will see the error will be cleared as shown below:

![](img/s_07.png)

Now the Dolibar is ready for using in the cyber range. We need to fill in some staff information and enable the function modules such as the HRM system and the leaving system so it can be fix the role of a ERP system in a railway company.



------

### 4. Configure the Dolibarr Function Models

This section is more related to add the information and enable the function modules used in the railway company via the Admin Dashboard. You can refer to the usage manual https://wiki.dolibarr.org/index.php/User_documentation and the https://www.dolibarr.org/dolibarr-tutorial-videos.php to learn how to use it. I only introduce some basic configuration I did in this section. Login with the admin credential you configured in the previous section to get to the setup dashboard.

#### 4.1 Setup the Company Information

Now we need to customized the company's ERP system, got to setup -> Company Origination page as shown below, fill in all the railway company general information such as address, official email, Fax, PH, Web URL, upload the company logo.

![](img/s_09.png)

Then go to the "Display" part to modify the CSS style as shown below: 

![](img/s_10.png)

If you want the user's account more easy to be attacked during the cyber attack, you can go to the security setting to disable some of the security setting such as the password format as shown below, then the user can use simple password such 123456 and during cyber exercise, the misconfigured user account can be used as a weakness point for the attacker to get in the system to cause the information leakage. 

![](img/s_11.png)

After setup the company Information then the main portal login page will be like this with the company name and logo and overview image:

![](img/s_12.png)



#### 4.2 Setup the HR System for the Company 

We can add user group for the simulated railway company now as the "Users & Groups" is the default module, but before that we need to active some HR management modules, from setup -> Modules/Application active the modules as shown below 

![](img/s_14.png)

- "Leave request management": Added the different type of leave for different group (manager, staff, engineer)
- "Expense report ": Set the report track and rules so we can build the report diagram after we add in different type of staff/user.
- Recruitment : for public the job position and the job application approval process. 
- Human resource management : the module for manage all the tools for people.

After finished configuration, we can add a new staff such as staff_alice as a OCC operator then link her permission to HR system as shown below, 

![](img/s_15.png)

Now we login Alice account and we can help her apply leave:

![](img/s_16.png)

Then we go back the admin user (as alice report to admin), then under the leaves tab we can see the new leave request and approval it as shown below:

![](img/s_17.png)



#### 4.3 Configure the Customer Relationship Management 

As the railway company need to get feed back from the customer so we also enable the Third Part and the Ticket System for customer to report the abnormal scenario of feed back the service as shown below:

![](img/s_18.png)

In the ticket system, we need to configure the public service interface so the passengers can use it as shown below:

![](img/s_19.png)

After that the passengers can access the ticket system page

![](img/s_20.png)



#### 4.4 Configure the Financial Modules

In this section as we are simulation, so we only active the salaries, then set the salary for each staff as shown below:

![](img/s_21.png)

After that we can go the the admin or user under financial group to help create new salary for the staff "test user " we the regular payment configuration as shown below:

![](img/s_22.png)



#### 4.5 Configure multi modules tools

 In the multi-module tools we setup the data import and export so we can export the data to build IT ERP system for other cyber range without from the beginning steps.

![](img/s_23.png)

 Then we also enable AI with custom AI service provided then we can link the function to the local GPU with Ollama service. 

![](img/s_24.png)

For the email as Dolibarr recommand GMAIL or Outlook service, so current I follow this instruction  https://wiki.dolibarr.org/index.php/Setup_EMails to setup use the smtp.gmail.com directly. 

For the collaborative work I only active he event collaboration as show below: 

![](img/s_25.png)

Then as admin we can create a event such as brief session and assign the attendance for different railway staff by add them in the callandar event:

 ![](img/s_28.png)

Now we almost have all the module we need, then the next step is to fill in the staff information, we can use AI to generate the staff information. Then to use the python script to generate a action in the ERP system such as apply leave in the HR system, we need to use the lib https://pypi.org/project/dolibarr/

Then we follow the example in this link https://wiki.dolibarr.org/index.php/Module_Web_Services_API_REST_(developer)#PHP to call the related API to generate the event or action. 



#### 4.6 Configure Special function module 

If you want to setup some special function such as 2FA which not in the dolibarr, you may need to purchse the module from the dolistore https://www.dolistore.com/index.php?l=en, then purchase the module you want then down load the zip file then follow this guide to install it : 

https://wiki.dolibarr.org/index.php/Module_TwoFactorAuth

![](img/s_27.png)

Now we almost finish create the ERP IT system for the cyber range which user for cyber exercise. 



------

