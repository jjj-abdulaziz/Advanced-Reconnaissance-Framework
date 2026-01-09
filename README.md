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

[Features](#-key-features) • [Installation](#-installation) • [Usage](#-usage) • [Quick Start](#-quick-start) • [Examples](#-examples)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Modules](#-modules)
- [Examples](#-examples)
- [Vulnerability Checks](#-vulnerability-checks)
- [Output](#-output-formats)
- [Legal Notice](#-legal--ethical-notice)
- [Contributing](#-contributing)
- [License](#-license)

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

### Advanced Capabilities

#### 🔒 **16 Vulnerability Checks**

- ✅ SQL Injection detection
- ✅ XSS (Cross-Site Scripting) testing
- ✅ Open Redirect vulnerabilities
- ✅ Exposed sensitive files (.git, .env, backups)
- ✅ Security header analysis (HSTS, CSP, X-Frame-Options)
- ✅ CORS misconfigurations
- ✅ Directory listing detection
- ✅ Information disclosure (server versions, comments)
- ✅ Mixed content detection
- ✅ Clickjacking vulnerabilities
- ✅ Cookie security analysis
- ✅ SSL/TLS configuration issues
- ✅ Insecure deserialization indicators
- ✅ Autocomplete on password fields
- ✅ Missing security headers
- ✅ Technology fingerprinting (20+ frameworks)

#### 📊 **Intelligence Features**

- 🎯 **Smart Detection** - Identifies 20+ web frameworks and technologies
- 🔐 **SSL/TLS Analysis** - Certificate inspection and cipher suite evaluation
- 🍪 **Cookie Security** - HttpOnly, Secure, and SameSite flag verification
- 📂 **Directory Enumeration** - Smart discovery with status code analysis
- 🌐 **CORS Testing** - Wildcard and misconfiguration detection
- 🚨 **Severity Grading** - Critical, High, Medium, Low vulnerability classification

---

## 🚀 Installation

### Quick Install (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework.git
cd Advanced-Reconnaissance-Framework

# 2. Run automated installer
chmod +x install.sh
./install.sh

# 3. Activate virtual environment
source venv/bin/activate

# 4. You're ready!
python3 cypherwolf.py --help
```

### Manual Installation

#### For Kali Linux / Debian / Ubuntu

```bash
# Install Python venv (if not installed)
sudo apt install python3-venv -y

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x cypherwolf.py
```

#### For macOS

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x cypherwolf.py
```

#### For Windows

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### System-Wide Installation (Kali/Debian)

```bash
# Install from system repositories
sudo apt update
sudo apt install python3-dnspython python3-requests python3-urllib3 -y
```

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Internet connection for scanning

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

### Your First Scan

```bash
# Activate virtual environment
source venv/bin/activate

# Run a quick DNS scan
python3 cypherwolf.py google.com -m dns
```

### Real-World Example

```bash
# Full reconnaissance with verbose output and JSON export
python3 cypherwolf.py example.com -m full -v -o example_scan.json
```

### Testing on Safe Targets

```bash
# Test on deliberately vulnerable sites (with permission!)
python3 cypherwolf.py testphp.vulnweb.com -m web
python3 cypherwolf.py scanme.nmap.org -m ports
```

---

## 💡 Examples

### Example 1: Quick DNS Reconnaissance

```bash
python3 cypherwolf.py facebook.com -m dns
```

**Output:**
```
[14:23:45.123] 🔍 Starting DNS enumeration...
[14:23:45.456] 🎯 A: 157.240.241.35
[14:23:45.789] 🎯 MX: smtpin.vvv.facebook.com
[14:23:46.012] 🎯 NS: a.ns.facebook.com
[14:23:46.234] ✓ Found 12 DNS records
```

### Example 2: Port Scanning with Custom Threads

```bash
python3 cypherwolf.py 192.168.1.1 -m ports --threads 200
```

**Scans 1000+ ports in seconds with service identification**

### Example 3: Deep Web Application Analysis

```bash
python3 cypherwolf.py target.com -m web -v -o web_report.json
```

**Performs:**
- Security header analysis (A-F grading)
- Technology stack detection
- Directory enumeration
- SSL/TLS inspection
- Cookie security review
- 16 vulnerability checks

### Example 4: Subdomain Discovery

```bash
python3 cypherwolf.py example.com -m subdomain
```

**Discovers subdomains via:**
- Certificate Transparency logs
- DNS bruteforce with built-in wordlist
- Active DNS resolution

### Example 5: Complete Reconnaissance

```bash
python3 cypherwolf.py target.com -m full -o full_recon.json --threads 150 -v
```

**Executes:**
- DNS enumeration (all record types)
- Port scanning (1000+ ports)
- Web application analysis
- Subdomain hunting
- Comprehensive vulnerability assessment
- Saves detailed JSON report

---

## 🧩 Modules

### 1. 🌐 DNS Reconnaissance

**Comprehensive DNS information gathering**

**Records Queried:**
- A (IPv4 addresses)
- AAAA (IPv6 addresses)
- MX (Mail servers)
- NS (Name servers)
- TXT (Text records, SPF, DKIM)
- SOA (Start of Authority)
- CNAME (Canonical names)
- PTR (Reverse DNS)
- SRV (Service records)

**Advanced Features:**
- Zone transfer (AXFR) attempts
- Nameserver enumeration
- DNS record TTL analysis

**Example:**
```bash
python3 cypherwolf.py github.com -m dns
```

---

### 2. 🔌 Network Port Scanner

**Multi-threaded port scanning with service detection**

**Features:**
- Scans 1000+ common ports (1-1024 + critical services)
- Banner grabbing for version detection
- Service identification
- Configurable thread pool (default: 100)
- Real-time progress tracking

**Common Ports Scanned:**
```
21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS),
80 (HTTP), 110 (POP3), 143 (IMAP), 443 (HTTPS), 445 (SMB),
1433 (MSSQL), 3306 (MySQL), 3389 (RDP), 5432 (PostgreSQL),
5900 (VNC), 6379 (Redis), 8080 (HTTP-Alt), 27017 (MongoDB)
```

**Example:**
```bash
python3 cypherwolf.py target.com -m ports --threads 200
```

---

### 3. 🕸️ Web Application Analyzer

**In-depth web security assessment**

#### Security Headers Analysis

Checks for:
- Strict-Transport-Security (HSTS)
- Content-Security-Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- X-XSS-Protection
- Referrer-Policy
- Permissions-Policy

**Grading System:** A (Excellent) to F (Poor)

#### Technology Detection

Identifies 20+ frameworks:
- **CMS:** WordPress, Joomla, Drupal
- **Frontend:** React, Angular, Vue.js, Next.js, Gatsby
- **Backend:** Laravel, Django, Flask, Express
- **Libraries:** jQuery, Bootstrap, Tailwind CSS
- **Build Tools:** Webpack, Vite
- **Servers:** Apache, Nginx, IIS

#### Directory Enumeration

Discovers:
- Admin panels
- API endpoints
- Backup directories
- Configuration files
- Upload directories

#### SSL/TLS Analysis

- Certificate details
- Cipher suites
- Protocol versions
- Validity dates
- Issuer information

#### Cookie Security

Analyzes:
- Secure flag
- HttpOnly flag
- SameSite attribute

**Example:**
```bash
python3 cypherwolf.py example.com -m web -v
```

---

### 4. 🎯 Subdomain Hunter

**Multi-technique subdomain discovery**

**Discovery Methods:**

1. **Certificate Transparency Logs**
   - Queries crt.sh database
   - Finds subdomains from SSL certificates

2. **DNS Bruteforce**
   - Built-in wordlist of 50+ common subdomains
   - Custom wordlist support
   - Active DNS resolution

**Built-in Wordlist:**
```
www, mail, ftp, admin, dev, staging, test, api, portal,
vpn, cdn, blog, shop, forum, support, docs, wiki, mobile,
app, secure, backup, status, monitor, and more...
```

**Example:**
```bash
python3 cypherwolf.py target.com -m subdomain
```

---

## 🔒 Vulnerability Checks

CypherWolf performs 16 automated vulnerability assessments:

### Critical Severity

| Vulnerability | Detection Method | Impact |
|---------------|------------------|---------|
| **SQL Injection** | Error-based detection | Database compromise |
| **Insecure Deserialization** | Pattern matching | Remote code execution |

### High Severity

| Vulnerability | Detection Method | Impact |
|---------------|------------------|---------|
| **Missing HSTS** | Header analysis | Man-in-the-middle attacks |
| **Exposed .git Directory** | File enumeration | Source code disclosure |
| **Exposed .env Files** | File enumeration | Credential theft |
| **Database Backups** | File enumeration | Data breach |
| **Reflected XSS** | Payload injection | Session hijacking |

### Medium Severity

| Vulnerability | Detection Method | Impact |
|---------------|------------------|---------|
| **Clickjacking** | Header analysis | UI redress attacks |
| **Directory Listing** | Response analysis | Information disclosure |
| **Mixed Content** | Resource parsing | Security warnings |
| **CORS Misconfiguration** | Header analysis | Cross-origin attacks |
| **Open Redirect** | Redirect testing | Phishing |

### Low Severity

| Vulnerability | Detection Method | Impact |
|---------------|------------------|---------|
| **Sensitive Comments** | HTML parsing | Information leakage |
| **Password Autocomplete** | Form analysis | Credential storage |
| **Server Version Disclosure** | Banner analysis | Fingerprinting |
| **Technology Disclosure** | Header analysis | Attack surface mapping |

---

## 📊 Output Formats

### Console Output

```
╔═══════════════════════════════════════════════════════════════╗
║             CYPHERWOLF - Advanced Recon Framework             ║
╚═══════════════════════════════════════════════════════════════╝

Target: example.com
Mode: full
Started: 2024-01-10 14:30:00

────────────────────────────────────────────────────────────────
  DNS RECONNAISSANCE MODULE
────────────────────────────────────────────────────────────────

[14:30:01.234] 🎯 A: 93.184.216.34
[14:30:01.567] 🎯 MX: mail.example.com
[14:30:02.890] ✓ Found 12 DNS records

────────────────────────────────────────────────────────────────
  PORT SCANNING MODULE
────────────────────────────────────────────────────────────────

[14:30:03.123] 🔍 Scanning 1024 ports with 100 threads...
[14:30:05.456] 🎯 Port 80/HTTP - OPEN Apache/2.4.41
[14:30:05.789] 🎯 Port 443/HTTPS - OPEN nginx/1.18.0
[14:30:08.012] ✓ Found 5 open ports

────────────────────────────────────────────────────────────────
  WEB APPLICATION ANALYSIS
────────────────────────────────────────────────────────────────

[14:30:09.234] 🔍 Analyzing security headers...
[14:30:09.567] ✓ Strict-Transport-Security: max-age=31536000
[14:30:09.890] ✗ Missing: Content-Security-Policy [high risk]
[14:30:10.123] 🔍 Detecting technologies...
[14:30:10.456] 🎯 Detected: WordPress
[14:30:10.789] 🎯 Detected: PHP
[14:30:11.012] 🔍 Running vulnerability checks...
[14:30:12.345] 🚨 Exposed: .git/config (Git repository)
[14:30:12.678] ⚠ Found 8 vulnerabilities: Critical=1, High=2, Medium=3, Low=2

────────────────────────────────────────────────────────────────
  SUBDOMAIN ENUMERATION
────────────────────────────────────────────────────────────────

[14:30:13.901] 🔍 Checking certificate transparency logs...
[14:30:15.234] 🎯 Found: www.example.com → 93.184.216.34
[14:30:15.567] 🎯 Found: mail.example.com → 93.184.216.35
[14:30:16.890] ✓ Total subdomains found: 23

────────────────────────────────────────────────────────────────
  SCAN SUMMARY
────────────────────────────────────────────────────────────────

DNS Records: 12 found
Open Ports: 5 found
Technologies: 8 detected
Security Grade: B
Vulnerabilities: 8 found
Subdomains: 23 found

✓ Scan completed successfully!
```

### JSON Output

```json
{
  "target": "example.com",
  "timestamp": "2024-01-10T14:30:00",
  "scan_type": "full",
  "dns": {
    "A": ["93.184.216.34"],
    "MX": ["mail.example.com"],
    "NS": ["ns1.example.com", "ns2.example.com"],
    "TXT": ["v=spf1 include:_spf.example.com ~all"]
  },
  "ports": [
    {
      "port": 80,
      "service": "HTTP",
      "banner": "Apache/2.4.41 (Ubuntu)",
      "state": "open"
    },
    {
      "port": 443,
      "service": "HTTPS",
      "banner": "nginx/1.18.0",
      "state": "open"
    }
  ],
  "web": {
    "headers": {
      "headers": {
        "Strict-Transport-Security": {
          "found": true,
          "value": "max-age=31536000"
        },
        "Content-Security-Policy": {
          "found": false,
          "severity": "high"
        }
      },
      "score": "5/7",
      "grade": "B"
    },
    "technologies": [
      "WordPress",
      "PHP",
      "jQuery",
      "Bootstrap"
    ],
    "vulnerabilities": [
      {
        "type": "Exposed Sensitive File",
        "severity": "high",
        "description": "Git repository exposed at /.git/config",
        "path": ".git/config",
        "recommendation": "Remove or restrict access to sensitive files"
      }
    ],
    "ssl": {
      "version": "TLSv1.3",
      "cipher": "TLS_AES_256_GCM_SHA384",
      "cert_subject": {
        "commonName": "example.com"
      },
      "valid_until": "2025-01-10"
    }
  },
  "subdomains": [
    {
      "subdomain": "www.example.com",
      "ips": ["93.184.216.34"]
    },
    {
      "subdomain": "mail.example.com",
      "ips": ["93.184.216.35"]
    }
  ]
}
```

---

## ⚠️ Legal & Ethical Notice

### 🚨 CRITICAL WARNING

**This tool is for AUTHORIZED security testing ONLY.**

### Legal Requirements

- ✅ **You MUST have explicit written permission** before scanning any system
- ✅ **Only scan systems you own** or have authorization to test
- ✅ **Comply with all applicable laws** (Computer Fraud and Abuse Act, Computer Misuse Act, etc.)
- ✅ **Respect bug bounty program rules** and stay within defined scope
- ❌ **Unauthorized scanning is ILLEGAL** in most jurisdictions
- ❌ **You are solely responsible** for how you use this tool

### Authorized Use Cases

This tool should ONLY be used for:

- ✅ Penetration testing with written authorization
- ✅ Bug bounty programs (within defined scope)
- ✅ Security audits of your own systems
- ✅ Educational purposes in controlled lab environments
- ✅ Red team exercises with proper approval
- ✅ Authorized vulnerability research

### Legal Consequences

Unauthorized use may result in:
- 🚫 Criminal prosecution
- 🚫 Civil lawsuits
- 🚫 Fines and penalties
- 🚫 Imprisonment
- 🚫 Permanent criminal record

### Disclaimer

The developers of CypherWolf:
- Are **NOT responsible** for misuse of this tool
- Do **NOT condone** illegal activities
- Provide this tool for **educational and authorized testing ONLY**
- Assume **NO liability** for actions taken by users
- **Will cooperate** with law enforcement if tool is used illegally

**By using this tool, you agree to:**
- Use it responsibly and legally
- Obtain proper authorization
- Accept full responsibility for your actions
- Comply with all applicable laws

---

## 🎓 Educational Resources

Learn more about ethical hacking:

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackerOne Hacker101](https://www.hacker101.com/)
- [TryHackMe](https://tryhackme.com/)
- [HackTheBox](https://www.hackthebox.com/)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to all functions
- Test your changes thoroughly
- Update documentation as needed
- Keep security and ethics in mind
- Add comments for complex logic

### Ideas for Contributions

- Add new vulnerability checks
- Improve detection accuracy
- Add support for more technologies
- Create new scanning modules
- Improve performance
- Add unit tests
- Enhance documentation
- Fix bugs

---

## 🐛 Bug Reports & Issues

Found a bug? Have a suggestion?

1. Check [existing issues](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework/issues)
2. Create a [new issue](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework/issues/new) with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version)
   - Screenshots if applicable

---

## 📝 Roadmap

### Upcoming Features

- [ ] Integration with Shodan and Censys APIs
- [ ] GraphQL endpoint discovery
- [ ] AWS S3 bucket enumeration
- [ ] API endpoint fuzzing
- [ ] Automated exploit suggestion
- [ ] HTML/PDF report generation
- [ ] Metasploit integration
- [ ] Plugin system for custom modules
- [ ] Web-based dashboard
- [ ] Docker container support
- [ ] CI/CD pipeline integration
- [ ] Machine learning for anomaly detection

---

## 🏆 Credits & Acknowledgments

### Built With

- [dnspython](https://www.dnspython.org/) - DNS toolkit for Python
- [requests](https://requests.readthedocs.io/) - HTTP library
- [urllib3](https://urllib3.readthedocs.io/) - HTTP client

### Inspired By

- [Nmap](https://nmap.org/) - Network security scanner
- [Recon-ng](https://github.com/lanmaster53/recon-ng) - Reconnaissance framework
- [theHarvester](https://github.com/laramies/theHarvester) - OSINT tool
- [Sublist3r](https://github.com/aboul3la/Sublist3r) - Subdomain enumerator
- [Nikto](https://cirt.net/Nikto2) - Web server scanner

### Special Thanks

- Security research community
- Open source contributors
- Bug bounty hunters
- Ethical hackers worldwide

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Additional Terms for Security Tools

This software is intended for authorized security testing only. Users must:

1. Obtain explicit written permission before scanning
2. Comply with all applicable laws and regulations
3. Use responsibly and ethically
4. Not use for malicious purposes
5. Accept full responsibility for their actions

---

## 👤 Author

**Abdul Aziz**

- GitHub: [@jjj-abdulaziz](https://github.com/jjj-abdulaziz)
- Repository: [Advanced-Reconnaissance-Framework](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework)

---

## ⭐ Show Your Support

If CypherWolf helped you in your security research, learning journey, or bug bounty hunting:

- ⭐ Star this repository
- 🍴 Fork it for your own use
- 📢 Share it with the security community
- 🐛 Report bugs and suggest features
- 💖 Consider contributing

---

## 📊 Project Statistics

- **Lines of Code:** 1000+
- **Vulnerability Checks:** 16
- **Technology Detections:** 20+
- **Scan Modules:** 4
- **Supported Platforms:** Linux, macOS, Windows
- **License:** MIT (Open Source)

---

## 📞 Support

Need help? Have questions?

- 📖 Check the [QUICKSTART.md](QUICKSTART.md) guide
- 🐛 Open an [issue](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework/issues)
- 💬 Join discussions in Issues section
- 📧 Contact maintainers

---

<div align="center">

**Made with ❤️ for the cybersecurity community**

*Hunt responsibly. Test ethically. Secure the digital world.* 🐺

```
"The best defense is a good offense - but only with permission!"
```

[![GitHub stars](https://img.shields.io/github/stars/jjj-abdulaziz/Advanced-Reconnaissance-Framework?style=social)](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/jjj-abdulaziz/Advanced-Reconnaissance-Framework?style=social)](https://github.com/jjj-abdulaziz/Advanced-Reconnaissance-Framework/network/members)

---

**CypherWolf v1.0.0** | Released January 2024

</div>
