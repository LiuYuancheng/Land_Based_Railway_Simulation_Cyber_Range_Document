# Fast Way to Setup a IT ERP System For a Critical Infra Cyber Range [ Land Based Railway System ]

**Project Design Purpose** : For the cyber range/twin (such as power, airport) used in attack and defense cyber exercise, most of time the Red/Blue/Yellow Team will focus more on the OT system, but some times there is requirement to build a company IT system (such as the internal ERP & HR ) to simulate the components in the company's corporate network in the ISA-95 Lvl5 structure, especially the attack demo/scenario is a combination of IT and OT attack or the attack init access is start from a misconfigured IT system. 

In this article, I will introduce a fast way about how I build such ERP system for the Land Based Railway Cyber Range System by using the opensource ERP DOLIBARR ERP & CRM package in several hours. three main sections will be included: 

- **System Architecture**: Introduce the cyber range architecture and position/role of the ERP system in the Railway Cyber Range.
- **ERP Software Setup:** The detailed steps to install DOLIBARR in the cyber range system and link the system with other components. 
- **ERP Function Configuration**: The detail steps to install, enable and configure the main features of DOLIBARR such as the HR system, leave application and approval, salary and use AI to create some information so the ERP system looks similar as a real one in the railway company.

**Acknowledge**: The ERP system of the cyber range is create by using the DOLIBARR without modification of the code,  for any usage for the system I will exactly follow the rules and requirement in  [DOLIBARR License Doc]( https://wiki.dolibarr.org/index.php/FAQ_What_is_Dolibarr_licence_%3F) and [[DOLIBARR Copy Right Rules](https://wiki.dolibarr.org/index.php/Rules_to_use_the_brand_name_%22Dolibarr%22). 

```python
# Author:      Yuancheng Liu
# Created:     2026/03/16
# Version:     v_0.0.1
# License:     GNU/GPL v3+ (Same as the DOLIBARR license)
```

