# 🛡️ AppSec Labs - Practical Application Security

**Sheila Wabosha | Aspiring Application Security Engineer**
📧 wabosha01@gmail.com | 🔗 github.com/wabosha0 | 📍 Kenya

This repository documents my hands-on journey mastering OWASP Top 10 and CWE vulnerabilities through building, breaking, and fixing vulnerable applications.

> **Goal:** Demonstrate exploit development, secure coding, and defensive remediation — not just theory.

---

### 🧪 Labs Completed

| # | Vulnerability | CWE | Exploit Technique | Fix Implemented | Status |
|---|---------------|-----|-------------------|-----------------|--------|
| 01 | Zip Slip - Path Traversal in Archive Extraction | CWE-22 | Crafted `evil.zip` with `../../../../tmp/pwned` to escape `uploads/` directory | `abspath + startswith` validation to enforce extraction sandbox | ✅ Complete |

---

### 📁 Lab 01: Zip Slip (CWE-22) - Python

**The Problem:** Python's `zipfile.extractall()` trusts filenames inside the zip. An attacker can use `../` sequences to write files anywhere on the server.

**What I Did:**
1. **Built vulnerable app:** `vuln.py` that extracts user-uploaded zips unsafely
2. **Built exploit:** `evil.py` generates malicious zip that escapes to `/tmp/`
3. **Verified exploitation:** Confirmed file creation outside target directory
4. **Built secure version:** `secure.py` validates canonical path before extraction
5. **Defensive pattern:** `if not abspath(target).startswith(abspath(upload_dir)): block`

**Skills Demonstrated:** Path Traversal, Secure Code Review, Python Security, Exploit Development, Defensive Programming

**Files:** `cd 01-zip-slip && python3 vuln.py`, `evil.py`, `secure.py`

---

### 🛠️ Tech Stack & Methodology

- **Languages:** Python, Bash
- **Security Testing:** Manual exploit crafting, File system abuse, Input validation bypass
- **Tools:** Kali Linux, Git, GitHub, Python `zipfile`
- **Standards:** OWASP Top 10, CWE, Secure SDLC Principles

**My Workflow for Every Lab:**
`Understand Vulnerability -> Build Vulnerable App -> Exploit It -> Fix It -> Document`

---

### 📬 For Recruiters

I am building this portfolio to transition into Application Security / Product Security. I focus on understanding how developers introduce vulnerabilities and how to build practical guards.

Available for: AppSec Intern, Junior Product Security, Bug Bounty Collaboration, Security Analyst roles.
