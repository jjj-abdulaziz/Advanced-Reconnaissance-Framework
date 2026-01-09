# 🐺 CypherWolf - Advanced Reconnaissance Framework

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║   ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗            ║
║  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗           ║
║  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝           ║
║  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗           ║
║  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║           ║
║   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝           ║
║                WOLF - Advanced Recon Framework                ║
╚═══════════════════════════════════════════════════════════════╝
```

**The Ultimate Python-Based Penetration Testing Reconnaissance Tool**

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg)](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework/releases)

[Features](#-key-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Quick Start](#-quick-start)

</div>

---

## 🎯 Overview

**CypherWolf** is a comprehensive, intelligent reconnaissance framework designed for penetration testers, security researchers, and ethical hackers. Built with Python, it combines multiple scanning techniques into a unified, powerful tool that automates the information gathering phase of security assessments.

### Why CypherWolf?

- 🚀 **Fast & Efficient** - Multi-threaded scanning with configurable performance
- 🎨 **Beautiful Interface** - Color-coded terminal output with real-time progress
- 🧩 **Modular Design** - Run individual modules or full reconnaissance
- 🔍 **Comprehensive** - DNS, ports, web, subdomains, and vulnerability scanning
- 📊 **Detailed Reports** - JSON export with structured data
- 🛡️ **Production Ready** - Tested on real-world targets

---

## ⚡ Key Features

### Core Scanning Modules

| Module | Description | Key Capabilities |
|--------|-------------|------------------|
| 🌐 **DNS Recon** | Comprehensive DNS enumeration | A, AAAA, MX, NS, TXT, SOA, CNAME, PTR, SRV records + Zone transfers |
| 🔌 **Port Scanner** | Advanced port detection | Multi-threaded scanning, banner grabbing, service identification |
| 🕸️ **Web Analyzer** | Application security analysis | Headers, tech stack, directories, SSL/TLS, cookies |
| 🎯 **Subdomain Hunter** | Subdomain discovery | Certificate transparency logs + DNS bruteforce |

### 🔒 Advanced Security Features

#### **16 Automated Vulnerability Checks**

- ✅ **SQL Injection** - Error-based detection
- ✅ **XSS (Cross-Site Scripting)** - Reflected payload testing
- ✅ **Open Redirect** - Unvalidated redirect detection
- ✅ **Exposed Sensitive Files** - .git, .env, backups, configs (20+ files)
- ✅ **Security Headers** - HSTS, CSP, X-Frame-Options analysis
- ✅ **CORS Misconfigurations** - Wildcard origin detection
- ✅ **Directory Listing** - Multiple path testing
- ✅ **Information Disclosure** - Server versions, comments, banners
- ✅ **Mixed Content** - HTTP resources on HTTPS pages
- ✅ **Clickjacking** - Frame-Options vulnerabilities
- ✅ **Cookie Security** - HttpOnly, Secure, SameSite flags
- ✅ **SSL/TLS Issues** - Certificate and cipher analysis
- ✅ **Insecure Deserialization** - Pattern detection
- ✅ **Password Autocomplete** - Form security check
- ✅ **Missing Headers** - Content-Type validation
- ✅ **Technology Fingerprinting** - 20+ frameworks detected

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Internet connection

### Quick Install (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework.git
cd Advanced-Reconnaissance-Framework

# 2. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run CypherWolf
python3 cypherwolf.py --help
```

### Installation by Platform

#### 🐧 Kali Linux / Debian / Ubuntu

**Option 1: Virtual Environment (Recommended)**
```bash
# Install venv if needed
sudo apt install python3-venv -y

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python3 cypherwolf.py --help
```

### Dependencies

```
dnspython>=2.3.0
requests>=2.31.0
urllib3>=2.0.0
```

These are automatically installed via `requirements.txt`.

---

## 📖 Usage

### Basic Syntax

```bash
python3 cypherwolf.py <target> [options]
```

### Command-Line Options

```
Required Arguments:
  target                Target domain or IP address

Optional Arguments:
  -h, --help           Show help message and exit
  -m, --mode MODE      Scan mode: dns, ports, web, subdomain, full (default: full)
  -o, --output FILE    Save results to JSON file
  -t, --threads NUM    Number of threads for port scanning (default: 100)
  -v, --verbose        Enable verbose output
  --version            Show version information
```

### Scan Modes

| Mode | Description | Speed | Use Case |
|------|-------------|-------|----------|
| `dns` | DNS enumeration only | ⚡ Fast | Quick DNS mapping |
| `ports` | Port scanning only | ⏱️ Medium | Service discovery |
| `web` | Web application analysis | ⏱️ Medium | Security assessment |
| `subdomain` | Subdomain discovery | 🐌 Slow | Mapping attack surface |
| `full` | All modules (default) | 🐌 Slow | Complete reconnaissance |

---

## 🎓 Quick Start

### Step 1: Setup

```bash
# Clone and enter directory
git clone https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework.git
cd Advanced-Reconnaissance-Framework

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Your First Scan

```bash
# Quick DNS scan
python3 cypherwolf.py google.com -m dns

# Expected output:
# [14:23:45.123] 🔍 Starting DNS enumeration...
# [14:23:45.456] 🎯 A: 142.250.185.46
# [14:23:45.789] 🎯 MX: smtp.google.com
# [14:23:46.012] ✓ Found 12 DNS records
```

### Step 3: Try Different Modes

```bash
# Port scan
python3 cypherwolf.py scanme.nmap.org -m ports

# Web analysis
python3 cypherwolf.py example.com -m web -v

# Full reconnaissance
python3 cypherwolf.py target.com -m full -o results.json
```

---

## 💡 Examples

### Example 1: Quick DNS Reconnaissance

```bash
python3 cypherwolf.py facebook.com -m dns
```

**What it does:**
- Queries A, AAAA, MX, NS, TXT, SOA, CNAME records
- Attempts zone transfer
- Shows TTL values

**Output:**
```
────────────────────────────────────────────────────────────────
  DNS RECONNAISSANCE MODULE
────────────────────────────────────────────────────────────────

[14:23:45.123] 🎯 A: 157.240.241.35
[14:23:45.456] 🎯 MX: smtpin.vvv.facebook.com
[14:23:45.789] 🎯 NS: a.ns.facebook.com
[14:23:46.012] 🎯 TXT: v=spf1 redirect=_spf.facebook.com
[14:23:46.234] ✓ Found 12 DNS records
```

### Example 2: Fast Port Scanning

```bash
python3 cypherwolf.py 192.168.1.1 -m ports --threads 200
```

**What it does:**
- Scans 1000+ common ports
- Uses 200 threads for speed
- Grabs service banners
- Identifies services

**Output:**
```
────────────────────────────────────────────────────────────────
  PORT SCANNING MODULE
────────────────────────────────────────────────────────────────

[14:30:03.123] 🔍 Scanning 1024 ports with 200 threads...
[14:30:05.456] 🎯 Port 80/HTTP - OPEN Apache/2.4.41
[14:30:05.789] 🎯 Port 443/HTTPS - OPEN nginx/1.18.0
[14:30:06.012] 🎯 Port 22/SSH - OPEN OpenSSH_8.2p1
[14:30:08.345] ✓ Found 5 open ports
```

### Example 3: Web Security Analysis

```bash
python3 cypherwolf.py example.com -m web -v -o web_scan.json
```

**What it does:**
- Analyzes security headers (A-F grading)
- Detects technologies (WordPress, React, etc.)
- Enumerates directories
- Checks SSL/TLS configuration
- Tests for 16 vulnerabilities
- Saves detailed JSON report

**Output:**
```
────────────────────────────────────────────────────────────────
  WEB APPLICATION ANALYSIS
────────────────────────────────────────────────────────────────

[14:30:09.234] 🔍 Analyzing security headers...
[14:30:09.567] ✓ Strict-Transport-Security: max-age=31536000
[14:30:09.890] ✗ Missing: Content-Security-Policy [high risk]
[14:30:10.123] ✗ Missing: X-Frame-Options [medium risk]

[14:30:10.456] 🔍 Detecting technologies...
[14:30:10.789] 🎯 Detected: WordPress
[14:30:11.012] 🎯 Detected: PHP
[14:30:11.234] 🎯 Detected: jQuery

[14:30:11.567] 🔍 Running vulnerability checks...
[14:30:12.890] 🚨 Exposed: .git/config (Git repository)
[14:30:13.123] 🚨 Missing HSTS on HTTPS site
[14:30:13.456] ⚠ Directory listing at /uploads/
[14:30:14.789] ⚠ Found 8 vulnerabilities: Critical=1, High=2, Medium=3, Low=2

Security Grade: C
```

### Example 4: Subdomain Discovery

```bash
python3 cypherwolf.py target.com -m subdomain
```

**What it does:**
- Queries Certificate Transparency logs
- Performs DNS bruteforce
- Resolves all found subdomains
- Shows IP addresses

**Output:**
```
────────────────────────────────────────────────────────────────
  SUBDOMAIN ENUMERATION
────────────────────────────────────────────────────────────────

[14:30:15.123] 🔍 Checking certificate transparency logs...
[14:30:17.456] 🎯 Found: www.target.com → 93.184.216.34
[14:30:17.789] 🎯 Found: mail.target.com → 93.184.216.35
[14:30:18.012] 🎯 Found: api.target.com → 93.184.216.36
[14:30:20.345] 🔍 Performing DNS bruteforce...
[14:30:22.678] 🎯 Found: dev.target.com → 192.168.1.100
[14:30:25.901] ✓ Total subdomains found: 23
```

### Example 5: Complete Reconnaissance

```bash
python3 cypherwolf.py target.com -m full -o full_scan.json --threads 150 -v
```

**What it does:**
- DNS enumeration (all record types)
- Port scanning (1000+ ports, 150 threads)
- Web application analysis
- Subdomain discovery
- All 16 vulnerability checks
- Saves comprehensive JSON report

**Duration:** 5-15 minutes depending on target

---

## 🧩 Modules Deep Dive

### 1. 🌐 DNS Reconnaissance

**Queries all DNS record types:**
- **A** - IPv4 addresses
- **AAAA** - IPv6 addresses
- **MX** - Mail servers
- **NS** - Name servers
- **TXT** - Text records (SPF, DKIM, DMARC)
- **SOA** - Start of Authority
- **CNAME** - Canonical names
- **PTR** - Reverse DNS
- **SRV** - Service records

**Advanced Features:**
- Zone transfer (AXFR) attempts
- TTL analysis
- Nameserver enumeration

### 2. 🔌 Port Scanner

**Comprehensive port analysis:**
- Scans ports 1-1024 (well-known)
- Plus critical services (1433, 3306, 3389, 5432, 6379, 8080, 27017)
- Multi-threaded (default: 100 threads)
- Banner grabbing
- Service identification
- Real-time progress tracking

**Detected Services:**
```
FTP (21), SSH (22), Telnet (23), SMTP (25), DNS (53),
HTTP (80), POP3 (110), IMAP (143), HTTPS (443), SMB (445),
MSSQL (1433), Oracle (1521), MySQL (3306), RDP (3389),
PostgreSQL (5432), VNC (5900), Redis (6379), MongoDB (27017)
```

### 3. 🕸️ Web Application Analyzer

**Security Header Analysis:**
- Strict-Transport-Security (HSTS)
- Content-Security-Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- X-XSS-Protection
- Referrer-Policy
- Permissions-Policy
- **Grading:** A (Excellent) to F (Poor)

**Technology Detection (20+):**
- **CMS:** WordPress, Joomla, Drupal
- **Frontend:** React, Angular, Vue.js, Next.js, Gatsby, Nuxt.js
- **Backend:** Laravel, Django, Flask, Express
- **Libraries:** jQuery, Bootstrap, Tailwind CSS, Material-UI
- **Build Tools:** Webpack, Vite
- **Servers:** Apache, Nginx, IIS, Microsoft-IIS

**Directory Enumeration:**
```
admin, login, dashboard, api, backup, uploads,
.git, .env, config, phpmyadmin, wp-admin, test
```

**SSL/TLS Analysis:**
- Certificate details
- Cipher suites
- Protocol versions (TLS 1.2, 1.3)
- Validity dates
- Issuer information

**Cookie Security:**
- Secure flag check
- HttpOnly flag check
- SameSite attribute check

### 4. 🎯 Subdomain Hunter

**Discovery Methods:**

1. **Certificate Transparency Logs**
   - Queries crt.sh database
   - Finds subdomains from SSL certificates
   - Historical certificate data

2. **DNS Bruteforce**
   - Built-in wordlist of 50+ common subdomains
   - Active DNS resolution
   - Wildcard detection

**Built-in Wordlist:**
```
www, mail, ftp, admin, dev, staging, test, api, portal,
vpn, cdn, blog, shop, forum, support, docs, wiki, mobile,
app, secure, backup, status, monitor, remote, cloud, mx
```

---

## 🔒 Vulnerability Checks

### Critical Severity (Immediate Action Required)

| # | Vulnerability | Detection | Impact |
|---|---------------|-----------|---------|
| 1 | **SQL Injection** | Error-based testing | Database compromise, data theft |
| 2 | **Insecure Deserialization** | Pattern matching | Remote code execution |

### High Severity (High Risk)

| # | Vulnerability | Detection | Impact |
|---|---------------|-----------|---------|
| 3 | **Missing HSTS** | Header analysis | Man-in-the-middle attacks |
| 4 | **Exposed .git Directory** | File probe | Source code disclosure |
| 5 | **Exposed .env File** | File probe | Credential theft |
| 6 | **Database Backups** | File enumeration | Complete data breach |
| 7 | **Reflected XSS** | Payload injection | Session hijacking |

### Medium Severity (Moderate Risk)

| # | Vulnerability | Detection | Impact |
|---|---------------|-----------|---------|
| 8 | **Clickjacking** | Header analysis | UI redress attacks |
| 9 | **Directory Listing** | Response parsing | Information disclosure |
| 10 | **Mixed Content** | Resource analysis | HTTPS downgrade |
| 11 | **CORS Misconfiguration** | Header check | Cross-origin attacks |
| 12 | **Open Redirect** | Redirect testing | Phishing attacks |

### Low Severity (Best Practice)

| # | Vulnerability | Detection | Impact |
|---|---------------|-----------|---------|
| 13 | **Sensitive Comments** | HTML parsing | Information leakage |
| 14 | **Password Autocomplete** | Form analysis | Credential exposure |
| 15 | **Server Version Disclosure** | Banner analysis | Fingerprinting |
| 16 | **Technology Disclosure** | Header analysis | Attack surface mapping |

**Sensitive Files Checked (20+):**
```
.git/config, .env, .DS_Store, web.config, .htaccess,
composer.json, package.json, phpinfo.php, backup.sql,
database.sql, dump.sql, config.php.bak, wp-config.php.bak,
Dockerfile, .gitignore, composer.lock, yarn.lock
```

---

## 📊 Output Formats

### Console Output

Beautiful, color-coded terminal output with real-time progress:

```
╔═══════════════════════════════════════════════════════════════╗
║             CYPHERWOLF - Advanced Recon Framework             ║
╚═══════════════════════════════════════════════════════════════╝

Target: example.com
Mode: full
Started: 2024-01-10 14:30:00

────────────────────────────────────────────────────────────────
  SCAN SUMMARY
────────────────────────────────────────────────────────────────

DNS Records: 12 found
Open Ports: 5 found
Technologies: 8 detected
Security Grade: B
Vulnerabilities: 8 found (Critical=1, High=2, Medium=3, Low=2)
Subdomains: 23 found

✓ Scan completed successfully!
```

### JSON Export

Structured data perfect for automation and integration:

```json
{
  "target": "example.com",
  "timestamp": "2024-01-10T14:30:00",
  "scan_type": "full",
  "dns": {
    "A": ["93.184.216.34"],
    "MX": ["mail.example.com"]
  },
  "ports": [
    {
      "port": 443,
      "service": "HTTPS",
      "banner": "nginx/1.18.0",
      "state": "open"
    }
  ],
  "web": {
    "headers": {
      "score": "5/7",
      "grade": "B"
    },
    "technologies": ["WordPress", "PHP", "jQuery"],
    "vulnerabilities": [
      {
        "type": "Exposed Sensitive File",
        "severity": "high",
        "description": "Git repository exposed at /.git/config",
        "recommendation": "Remove or restrict access"
      }
    ]
  },
  "subdomains": [
    {
      "subdomain": "www.example.com",
      "ips": ["93.184.216.34"]
    }
  ]
}
```

---

## ⚠️ Legal & Ethical Notice

### 🚨 CRITICAL WARNING

**This tool is for AUTHORIZED security testing ONLY.**

### You MUST Have Permission

- ✅ **Written authorization** before scanning ANY system
- ✅ **Only scan systems you own** or have explicit permission to test
- ✅ **Stay within authorized scope** (bug bounty programs, pentests)
- ✅ **Comply with all laws** (CFAA, Computer Misuse Act, etc.)
- ❌ **Unauthorized scanning is ILLEGAL**
- ❌ **You are solely responsible** for your actions

### Legal Consequences of Misuse

- 🚫 Criminal prosecution
- 🚫 Heavy fines
- 🚫 Imprisonment
- 🚫 Civil lawsuits
- 🚫 Permanent criminal record

### Authorized Use Cases

✅ Penetration testing with written contract
✅ Bug bounty programs (within scope)
✅ Security audits of your own systems
✅ Educational labs and sandboxes
✅ Red team exercises with approval
✅ Authorized vulnerability research

### Disclaimer

The developers:
- Are **NOT responsible** for misuse
- Do **NOT condone** illegal activities
- Provide this for **educational purposes ONLY**
- Assume **NO liability** for user actions
- **Will cooperate** with law enforcement

**By using CypherWolf, you agree to use it legally and ethically.**

---

## 🤝 Contributing

We welcome contributions! Here's how:

### How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

### Ideas for Contributions

- 🔍 Add new vulnerability checks
- 🎯 Improve detection accuracy
- 🚀 Enhance performance
- 📝 Improve documentation
- 🐛 Fix bugs
- 🧪 Add unit tests
- 🌐 Support more technologies

---

## 🐛 Bug Reports

Found a bug? Please open an issue with:

- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)
- Screenshots if applicable

---

## 📝 Roadmap

### Coming Soon

- [ ] Shodan & Censys API integration
- [ ] GraphQL endpoint discovery
- [ ] AWS S3 bucket enumeration
- [ ] API fuzzing module
- [ ] HTML/PDF report generation
- [ ] Metasploit integration
- [ ] Plugin system
- [ ] Web dashboard
- [ ] Docker support
- [ ] CI/CD integration

---

## 🏆 Credits

**Built With:**
- [dnspython](https://www.dnspython.org/) - DNS toolkit
- [requests](https://requests.readthedocs.io/) - HTTP library
- [urllib3](https://urllib3.readthedocs.io/) - HTTP client

**Inspired By:**
- Nmap, Recon-ng, theHarvester, Sublist3r, Nikto

**Special Thanks:**
- Security research community
- Open source contributors
- Ethical hackers worldwide

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

**Additional Terms:** This software is for authorized security testing only.

---

## 👤 Author

**Abdul Aziz**

- GitHub: [@jjj-abdulaziz](https://github.com/jjj-abdulaziz)
- Project: [Advanced-Reconnaissance-Framework](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework)

---

## ⭐ Support

If CypherWolf helped you:

- ⭐ Star this repository
- 🍴 Fork it
- 📢 Share with others
- 🐛 Report issues
- 💖 Contribute code

---

<div align="center">

**Made with ❤️ for the cybersecurity community**

*Hunt responsibly. Test ethically. Secure the world.* 🐺

```
"The best hackers are the ones who ask permission first."
```

---

**CypherWolf v1.0.0** | Released January 2025

[![GitHub](https://img.shields.io/github/stars/jjj-abdulaziz/Advanced-Reconnaissance-Framework?style=social)](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework)

</div>
