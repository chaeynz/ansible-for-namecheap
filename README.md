# Ansible for Namecheap

[![Ansible Collection](https://img.shields.io/badge/Ansible-Collection-blue?style=flat-square&logo=ansible)](https://galaxy.ansible.com/)
[![License](https://img.shields.io/github/license/chaeynz/ansible-for-namecheap?style=flat-square)](LICENSE)

This Ansible collection provides modules to manage and query Namecheap via its API.

---
## 📦 **Installation**

### Install via Ansible Galaxy:
```bash
ansible-galaxy collection install chaeynz.namecheap
```

---

## ⚙️ **Configuration**

Before using the collection, set up your **API credentials**.
You can pass them as **api_user** and **api_token** arguments in the modules, or as **environment variables** **NAMECHEAP_USER**, **NAMECHEAP_TOKEN**



Ensure that your IP is **whitelisted** in Namecheap's API settings.

---

## 📚 **Available Modules**
| Module | Description |
|-|-|
| `nc_lookup` | Lookup module to query any of the get methods listed on https://www.namecheap.com/support/api/methods/ |
