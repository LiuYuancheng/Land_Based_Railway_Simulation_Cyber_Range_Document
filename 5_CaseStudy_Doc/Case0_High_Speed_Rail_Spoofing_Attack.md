## High Speed Rail Spoofing Cyber Attack Case Study : Use Cyber Twin to Simulate the Cyber Incident Happened in Taiwan High Speed Rail 

**Project Background and Design Purpose** : 

The idea for this case study was inspired by the report “**Taiwan High Speed Rail Hit by Spoofing Attack That Stops Three Trains**” released on 06 May 2026, which described a cybersecurity incident targeting the Taiwan railway’s Operational Technology (OT) and communication infrastructure. According to the report, three high-speed rail trains were unexpectedly forced into emergency stop conditions, resulting in approximately 48 minutes of service disruption across major transit operations. Preliminary investigation indicated that the incident was related to a signal spoofing attack affecting the railway communication and control system.

![](Case0_img/s_01.png)

In this case study, the Land-Based Railway OT Simulation Cyber Twin I developed is used to simulate a similar cybersecurity scenario in a controlled cyber range environment. The objective is not to create a one-to-one replication of the real-world incident, but to demonstrate how a False Data Injection (FDI) and spoofing attack could impact railway OT operations, train signaling logic, and automated safety mechanisms within a software-defined railway cyber twin platform.

The article is organized into the following sections:

- A brief summary of the reported spoofing attack incident involving the Taiwan High Speed Rail system.
- An introduction to the simulated railway radio communication system implemented in the Land-Based Railway Cyber Twin platform.
- The design methodology used to replicate a similar spoofing attack scenario within the cyber range environment.
- A detailed demonstration of the False Data Injection (FDI) spoofing attack, including the attack process, operational impact, and incident progression during the cyber exercise.
- Discussion of possible detection methods, defensive mechanisms, and incident response strategies against this category of railway OT cyberattack.

Although this case study is implemented entirely within a software-based cyber range platform, it demonstrates how realistic railway OT attack scenarios can be reproduced safely for cybersecurity research and training purposes. The study also illustrates how OT cyber twins can help railway cybersecurity teams better understand attack behaviors, evaluate operational impact, and improve incident response readiness during cyber exercises.

```python
# Author:      Yuancheng Liu
# Created:     2026/05/06
# Version:     v_0.0.1
# Copyright:   Copyright (c) 2026 LiuYuancheng
# License:     MIT License
```

**Table of Contents**

[TOC]

------

### 1. Introduction

In April 2026, Taiwan’s high-speed railway system experienced a significant cybersecurity incident when multiple trains were forced into emergency stop conditions after a spoofing attack targeted the railway radio communication network. According to public reports, the attack was allegedly conducted by a 23 years old university student using low-cost Software-Defined Radio (SDR) equipment to analyze and inject unauthorized wireless communication signals into the railway operational system. The incident demonstrated how modern railway infrastructure can be affected by cyberattacks targeting Operational Technology (OT) communication systems and highlighted the growing cybersecurity risks faced by critical transportation infrastructure.

This case study project aims to replicate/simulate a similar cyberattack scenario within the controlled OT cyber range platform **Land-Based Railway OT Simulation Cyber Twin**. The objective of the project is not to reproduce the real-world incident exactly, but to demonstrate the possible attack workflow, vulnerability exploitation process, operational impact, attack path, and related technologies involved in a railway False Data Injection (FDI) and spoofing attack scenario. The project also demonstrates how railway OT cyber ranges can be used for cybersecurity research, professional training, incident response exercises, attack analysis, and defensive capability validation for railway operators and cybersecurity teams.



#### 1.1 Summary of the Cyber Attack and Incident

A 23-year-old university student and radio enthusiast, identified by the surname Lin, was arrested for allegedly conducting a sophisticated spoofing attack against the Taiwan High Speed Rail (THSR) system during the Qingming Festival holiday period in April 2026: 

![](Case0_img/s_02.png)

**1.1.1 Key Details of the Incident**

- **The Attack:** Using consumer-grade **Software-Defined Radio (SDR)** equipment and tools purchased online, Lin analyzed the THSR’s radio signals. He managed to crack the system's parameters and "cloned" a legitimate beacon signal to send a high-priority **"General Alarm"** message to the control center.  
- **The Impact:** The false alarm triggered safety protocols on **April 5, 2026, at 11:23 PM**, forcing three trains into immediate manual emergency stops. A fourth train was halted shortly after. The incident caused a total disruption of **48 minutes**, delaying hundreds of passengers returning from the holiday.  
- **The Vulnerability:** Experts revealed that the student exploited weaknesses in the **TETRA radio system**, which THSR had used for 19 years without rotating its security parameters. Lin reportedly cracked multiple layers of verification mechanisms to send the unauthorized signal.  
- **The Arrest:** Police traced the signal to Lin’s residence in Taichung, where they seized 11 handheld radios, an SDR receiver, and a laptop. He was released on NT$100,000 bail and faces charges for endangering public safety and interfering with transportation.  

**1.1.2 incident Aftermath**

The incident triggered significant public and governmental concern regarding the cybersecurity resilience of critical transportation infrastructure against low-cost and widely accessible attack technologies. Following the event, Taiwan transportation authorities initiated comprehensive reviews of railway and metro communication systems, focusing on improving authentication mechanisms, encryption, parameter management, and wireless communication security hardening.

This event also highlighted how cyberattacks targeting OT communication systems can directly affect railway operational safety, train scheduling, passenger services, and emergency response procedures.

**1.1.3 Reference Link** 

- https://gbhackers.com/taiwan-high-speed-rail-hit-by-spoofing-attack/
- https://sqmagazine.co.uk/taiwan-student-high-speed-rail-cyberattack/



#### 1.2 Introduction to the Land-Based Railway Cyber Twin Platform

As described in the incident summary, the spoofing attack primarily targeted the railway train control communication process by cloning legitimate radio communication data and injecting false alarm messages into the operational environment. To demonstrate this type of cyberattack safely, the **Land-Based Railway Cyber Twin** platform is used to simulate the railway OT environment and replicate the attack scenario. The system interface overview is shown below:

![](Case0_img/s_03.png)

**1.2.1 Cyber Twin System architecture** 

The **Land-Based Railway Simulation Cyber Twin System** is a fully software-based distributed cybersecurity simulation platform designed to emulate all six ISA-95/IEC-62264 IT and OT layers of a modern railway system. The platform includes simulation modules for multiple railway operational subsystems, including:

- Railway track fixed-block signaling systems
- Railway 3rd Track Power System
- Automatic Train Control (ATC) systems
- Automatic Train Protection (ATP) systems
- Railway Radio Communication System
- Railway station control systems
- Train dispatch and operational control center (OCC) systems
- Human-Machine Interface (HMI) monitoring systems
- Industrial communication protocols and field device simulations

The ISA-95 / IEC-62264 system architecture implementation of the railway cyber twin platform is shown below:

![](Case0_img/s_04.png)

**1.2.2 Detailed System Introduction Document**

The railway cyber range has been used in multiple international cybersecurity exercises, professional training programs, and OT security research projects. Additional project details and related technical references are available in the following documents:

- https://github.com/LiuYuancheng/Land_Based_Railway_Simulation_Cyber_Range_Document
- [Use PLC to Implement Land Based Railway Track Fixed Block Signaling OT System](https://www.linkedin.com/pulse/use-plc-implement-land-based-railway-track-fixed-block-yuancheng-liu-saaec)
- [Simulating Simple Railway Station Train Dock and Depart Auto-Control System with IEC104 PLC Simulator](https://www.linkedin.com/pulse/simulating-simple-railway-station-train-dock-depart-auto-control-liu-vsscc)
- [Implementing Different Human-Machine Interfaces (HMI) for a Land-Based Railway Cyber Range](https://www.linkedin.com/pulse/implementing-different-human-machine-interfaces-hmi-land-based-liu-cqojc)
- [Design and Usage of the Human-Machine Interfaces (HMI) for a Land-Based Railway Cyber Range](https://www.linkedin.com/pulse/design-usage-human-machine-interfaces-hmi-land-based-railway-liu-idpfc)

- [Design of the Train Control for Land-Based Railway Cyber Range](https://www.linkedin.com/pulse/design-train-control-land-based-railway-cyber-range-yuancheng-liu-alusc)

- [Fast Way to Setup an ERP(IT) System For the  Land Based Railway System Cyber Range](https://www.linkedin.com/pulse/fast-way-setup-erpit-system-critical-infra-cyber-range-yuancheng-liu-psykc)



------

### 2. Spoofing Attack Analysis

This section analyzes the Taiwan High Speed Rail (THSR) spoofing attack using the MITRE ATT&CK for ICS (Industrial Control Systems) framework and explains how a similar attack scenario can be replicated within the Land-Based Railway Simulation Cyber Twin System. The objective includes:

- Understand the attacker’s workflow, identify the related ICS attack techniques. 
- Demonstrate how False Data Injection (FDI) and signal spoofing attacks can affect railway Operational Technology (OT) environments.

#### 2.1 MITRE ATT&CK for ICS Framework Mapping

This section maps the reported THSR spoofing attack to the MITRE ATT&CK for ICS framework and identifies which attack techniques are implemented in the cyber twin simulation environment.

The attack workflow consists of several stages, including wireless reconnaissance, communication exploitation, signal impersonation, false data injection, and operational disruption. The mapping diagram is shown below:

![](Case0_img/s_05.png)

| **Tactic**                 | **Technique ID** | **Technique Name**                         | **Attack Detail**                                            | Apply  on Cyber Twin |
| -------------------------- | ---------------- | ------------------------------------------ | ------------------------------------------------------------ | -------------------- |
| **Reconnaissance**         | **T0887**        | **Wireless Sniffing**                      | Lin used a Software-Defined Radio (SDR) filter to intercept and analyze TETRA radio signals. | Yes                  |
| **Initial Access**         | **T0860**        | **Wireless Compromise**                    | Exploited the unencrypted or weakly secured TETRA radio frequencies used by THSR for 19 years. | Yes                  |
| **Execution**              | **T0807**        | **Command-Line Interface**                 | Used a laptop and SDR software tools to decode parameters and program handheld radios. | Yes                  |
| **Persistence**            | **T0859**        | **Valid Accounts / Parameters**            | Bypassed 7 layers of verification by using legitimate (cloned) system parameters and beacons. | No                   |
| **Evasion**                | **T0849**        | **Masquerading**                           | Programmed handheld radios to "impersonate" legitimate THSR beacons to avoid rejection by the control center. | Yes                  |
| **Impair Process Control** | **T0855**        | **Unauthorized Command Message**           | Transmitted a high-priority "General Alarm" signal to the control center and trains. | Yes                  |
| **Impact**                 | **T0879**        | **Damage to Property / Denial of Service** | Forced emergency braking on 4 trains, causing a 48-minute total operational shutdown. | Yes                  |

Within the cyber twin environment, most of the attack stages can be replicated safely using simulated OT communication protocols, virtual RTUs, and software-defined signaling systems.



#### 2.2 Replicated Attack Outline on Cyber Twin

The primary attack vector in the reported spoofing incident was the injection of unauthorized alarm data into the railway communication system. Therefore, this case study focuses on simulating a similar False Data Injection (FDI) attack within the railway cyber twin platform. 

In the real-world incident, the attacker targeted wireless radio communication infrastructure using spoofed beacon signals. In the cyber range environment, the wireless and radio communication links are simulated using industrial OT communication protocols over IP networks. The protocol selected for this case study is **Siemens S7comm**, which is commonly used for industrial communication between PLCs, RTUs, SCADA systems, and distributed OT devices over Ethernet, wireless bridges, and industrial radio links.

The replicated attack workflow consists of the following stages:

- **Signal Analysis** : S7Comm radio signals analysis and data decryption.
- **Parameter Cracking and Packet Construction** : Decode train data parameters and generate the false data packet. 
- **False Data Injection**: Transmit unauthorized false operational packet to train data collection RTU via radio antenna. 
- **Operational Impact on OCC** : Trigger abnormal operational states within the OCC and activate emergency protection logic. 
- **Safety Mechanism Activation** : Demonstrate how the railway protection system responds to abnormal cased service disruption. 

#### 2.3 Introduction of False Data Injection (FDI) Attack

False Data Injection (FDI) is a cyberattack technique in which attackers intentionally inject manipulated or forged data into an Operational Technology (OT) system to influence system behavior, operational decisions, or automated control logic.

- **Objective:** The main goal of FDI is to manipulate the data within the OT system, leading to incorrect or misleading information being processed by the control systems.
- **Method:** Attackers inject false or manipulated data into the sensors or communication channels within the OT system. This can lead to the control systems making incorrect decisions based on the compromised data.
- **Example:** In a power grid, an FDI attack might involve injecting false sensor readings that indicate lower electricity demand than actual. This could lead to incorrect decisions in adjusting power generation levels, potentially causing disruptions or even damage to the system.



------

### 3. Design of Radio Communication System in Cyber Twin

Before we start to introduce the attack path and technology I will simulated on the cyber twin, I will introduce how I designed the impacted sub-system in the cyber range so you know which part is the vulnerable part for the cyber attack. The impacted 2 sub system are the train power system (emergency stop) and the railway train data communication system. The two sub-system workflow diagram as shown below: 

![](Case0_img/s_06.png)

#### 3.1 Design of Railway 3rd Track Power System

As shown in the diagram, the 3rd Track along the train moving track will provide electrical power to the train. In the cyber twin I simulated the 750V DC power under the EN-50155 standard. The 3rd track is splitted to several continuous block (as shown in the diagram B01, B02, B03...) and the train use pantograph to connect to the blocks one by one to get power when it is running. 

Each block is linked to the 750V-DC transformer and the link will be controlled by a minorized control breaker/controllable Relay  (CR01, CR02, CR03.. ), each of the breaker will be linked to the third track control PLC 's output coil, so the PLC can one and off the power of each block. 

The PLC is connect to the Railway OCC's Train remote control HMI via Modbus-TCP, so the OCC operator can remote cut-off and turn on the power supply to the train. During the emergency stop process, the the HMI will send the braker on to train remotely, if the train didn't reduce the speed, the operator can force cut off the power supply to the train to make the train stop.

The Power system will be the Impacted system which caused the service disruption. 

#### 3.2 Design of Railway Radio Communication System

The Railway communication system will be the main targeted system of the spoofing attack. As shown in the diagram, the train will have one simulated data broadcast antenna to transmit the train current real time operational information (current speed, average spped, brake air pressure, input voltage, motor current, train motor RPM, radar state, time stamp ...) to the Radio antenna tower along next to the track. The data transmit follows the General S7 Message Structure (PDU) 

In the cyber twin along the track every fix distance will be a simulated data reviver tower to pick the trains operational information, all the tower will connect to the Radio Link data management RTU, then the RTU will send multiple trains information to the OCC via Siemens-S7comm protocol and the information will be processed and display on the train control HMI dashboard. 