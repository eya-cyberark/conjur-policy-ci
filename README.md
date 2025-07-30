# 🚀 GitHub Action Pipeline for Managing Conjur Policies (JWT Auth)

This GitHub Action automates the process of **loading and managing Conjur policies**, ensuring that changes made to policy files in your repository are automatically applied to your Conjur Cloud instance using **JWT (OIDC) authentication** via GitHub Actions.

---

## 🔍 Overview

This GitHub Actions workflow:

- Uses GitHub OIDC tokens to securely authenticate to Conjur Cloud.
- Validates YAML syntax of policy files.
- Automatically applies changes for `policy/01_*.yml` (hosts) and `policy/02_*.yml` (ACLs).
- Runs on `push` to `main` and on pull requests targeting `main`.

---

## ✅ Features

- 🔐 **JWT/OIDC Authentication** via GitHub's secure identity token  
- ⚙️ **Automated Policy Deployment** from GitHub CI/CD  
- 🧪 **YAML Linting** using `yamllint`  
- 🧠 **Change Detection**: Only uploads changed policy files  
- 🔒 **No Secrets Stored**: Secure and keyless authentication  

---

## 📁 Policy File Structure

Organize policy files like this:

```
policy/
├── 01_host.yml   # Host definitions
└── 02_acls.yml   # ACL rules
```

Naming conventions:
- `01_*.yml`: host identities
- `02_*.yml`: permissions (ACLs)

---

## 🛠 Prerequisites

Before using this workflow:

- ✅ Conjur Cloud must have the `authn-jwt` authenticator enabled.
- 🆔 A JWT service ID must be configured (e.g., `EyaGithub`).
- 🔐 A host identity (e.g., `host/my-app/github-actions`) must be created in Conjur.
- 🔗 GitHub OIDC must be enabled on your repo:  
  Go to `Settings > Actions > Workflow permissions`, and enable **Read and write permissions** and **OIDC token requests**.

---

## 🔧 Required GitHub Permissions

```yaml
permissions:
  id-token: write
  contents: read
```

---

## 🧬 Workflow Summary

The CI pipeline performs the following steps:

1. Checkout Code  
2. Install Tools (`jq`, `curl`, `yamllint`)  
3. Request OIDC JWT from GitHub  
4. Authenticate to Conjur Cloud with JWT  
5. Validate YAML syntax  
6. Detect changed files in `policy/`  
7. Upload changed policy files  

---
