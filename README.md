# Advanced Reconnaissance Framework

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

**An intelligent, modular penetration testing framework for comprehensive reconnaissance**

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg)
![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Modules](#-modules) • [Examples](#-examples)

</div>

---

## 🎯 Features

CypherWolf is a next-generation reconnaissance tool that combines multiple scanning techniques into a unified, intelligent framework:

### Core Capabilities

- 🔍 **Advanced Port Scanning** - Multi-threaded scanner with banner grabbing and service detection
- 🌐 **Comprehensive DNS Reconnaissance** - Full DNS enumeration with zone transfer attempts
- 🕸️ **Intelligent Web Analysis** - Security headers, technology detection, vulnerability scanning
- 🎯 **Subdomain Hunting** - Certificate transparency + DNS bruteforce enumeration
- 🔐 **SSL/TLS Analysis** - Certificate inspection and cipher suite analysis
- 🍪 **Cookie Security Analysis** - HttpOnly, Secure, and SameSite flag verification
- 📂 **Directory Enumeration** - Smart directory discovery with status code analysis
- 🚨 **Vulnerability Detection** - Automated checks for common security issues

### Advanced Features

- ⚡ **Multi-threading** - Blazing fast scans with configurable thread pools
- 📊 **Detailed Reporting** - Comprehensive JSON output with scan summaries
- 🎨 **Beautiful CLI** - Color-coded output with progress indicators
- 🔄 **Modular Architecture** - Run individual modules or full reconnaissance
- 📝 **Verbose Logging** - Detailed operation logs for debugging
- 💾 **Export Results** - Save all findings to structured JSON files

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Quick Install

```bash
# Clone the repository
git clone https://github.com/jjj-abdulaziz/cypherwolf.git
cd cypherwolf

# Install dependencies
pip3 install -r requirements.txt

# Make executable (Linux/Mac)
chmod +x cypherwolf.py

# Run the tool
python3 cypherwolf.py --help
```

### Manual Dependencies

```bash
pip3 install dnspython requests urllib3
```

## 📖 Usage

### Basic Syntax

```bash
python3 cypherwolf.py <target> [options]
```

### Scan Modes

```bash
# Full reconnaissance scan (all modules)
python3 cypherwolf.py example.com

# DNS enumeration only
python3 cypherwolf.py example.com -m dns

# Port scanning only
python3 cypherwolf.py example.com -m ports

# Web application analysis
python3 cypherwolf.py example.com -m web

# Subdomain discovery
python3 cypherwolf.py example.com -m subdomain
```

### Advanced Options

```bash
# Save results to JSON file
python3 cypherwolf.py example.com -o results.json

# Use more threads for faster scanning
python3 cypherwolf.py example.com -m ports --threads 200

# Enable verbose output
python3 cypherwolf.py example.com -v

# Full scan with all options
python3 cypherwolf.py example.com -m full -o scan.json --threads 150 -v
```

### Command-Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `target` | - | Target domain or IP address | Required |
| `--mode` | `-m` | Scan mode (dns, ports, web, subdomain, full) | `full` |
| `--output` | `-o` | Save results to JSON file | None |
| `--threads` | `-t` | Number of threads for port scanning | `100` |
| `--verbose` | `-v` | Enable verbose output | `False` |
| `--version` | - | Show version information | - |

## 🧩 Modules

### 1. Network Scanner

**Multi-threaded port scanning with advanced service detection**

- Scans 1000+ common ports
- Banner grabbing for service identification
- Configurable thread pool for speed optimization
- Real-time progress tracking

**Output:**
- Open ports with service names
- Service banners and versions
- Response times

### 2. DNS Reconnaissance

**Comprehensive DNS information gathering**

- A, AAAA, MX, NS, TXT, SOA, CNAME, PTR, SRV records
- Zone transfer (AXFR) attempts
- Nameserver enumeration
- DNS record analysis

**Output:**
- Complete DNS record mapping
- Zone transfer vulnerabilities
- Nameserver information

### 3. Web Analyzer

**In-depth web application security analysis**

**Features:**
- Security header analysis with grading system
- Technology stack fingerprinting (20+ frameworks)
- Directory enumeration with status codes
- SSL/TLS certificate inspection
- Cookie security analysis
- Common vulnerability detection

**Detects:**
- Missing security headers (HSTS, CSP, X-Frame-Options)
- Framework and CMS versions
- Exposed admin panels
- Information disclosure
- Clickjacking vulnerabilities
- Directory listings

### 4. Subdomain Hunter

**Advanced subdomain discovery using multiple techniques**

**Methods:**
- Certificate Transparency logs (crt.sh)
- DNS bruteforce with custom wordlists
- Wildcard detection
- DNS resolution verification

**Output:**
- Discovered subdomains with IP addresses
- Active vs inactive subdomains
- Subdomain count statistics

## 💡 Examples

### Example 1: Quick DNS Check

```bash
python3 cypherwolf.py google.com -m dns
```

**Output:**
```
[14:23:45.123] 🔍 Starting DNS enumeration...
[14:23:45.456] 🎯 A: 142.250.185.46
[14:23:45.789] 🎯 MX: smtp.google.com
[14:23:46.012] 🎯 NS: ns1.google.com
```

### Example 2: Full Web Analysis

```bash
python3 cypherwolf.py example.com -m web -v
```

**Scans for:**
- Security headers and scoring
- Technologies (React, WordPress, etc.)
- Hidden directories
- SSL/TLS configuration
- Cookie security flags
- Potential vulnerabilities

### Example 3: Fast Port Scan

```bash
python3 cypherwolf.py 192.168.1.1 -m ports --threads 200
```

**Features:**
- Scans 1000+ ports in seconds
- Service identification
- Banner grabbing
- Real-time results

### Example 4: Complete Reconnaissance

```bash
python3 cypherwolf.py target.com -m full -o full_scan.json -v
```

**Performs:**
- DNS enumeration (all record types)
- Port scanning (1000+ ports)
- Web application analysis
- Subdomain discovery
- Saves everything to JSON

## 📊 Output Example

### Console Output

```
╔═══════════════════════════════════════════════════════════════╗
║             CYPHERWOLF - Advanced Recon Framework             ║
╚═══════════════════════════════════════════════════════════════╝

Target: example.com
Mode: full
Started: 2024-01-07 14:30:00

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
  SCAN SUMMARY
────────────────────────────────────────────────────────────────

DNS Records: 12 found
Open Ports: 5 found
Technologies: 8 detected
Security Grade: B
Vulnerabilities: 2 found
Subdomains: 23 found

Scan completed successfully!
```

### JSON Output

```json
{
  "target": "example.com",
  "timestamp": "2024-01-07T14:30:00",
  "scan_type": "full",
  "dns": {
    "A": ["93.184.216.34"],
    "MX": ["mail.example.com"],
    "NS": ["ns1.example.com", "ns2.example.com"]
  },
  "ports": [
    {
      "port": 80,
      "service": "HTTP",
      "banner": "Apache/2.4.41",
      "state": "open"
    }
  ],
  "web": {
    "headers": {
      "score": "5/7",
      "grade": "B"
    },
    "technologies": ["WordPress", "PHP", "jQuery"],
    "vulnerabilities": []
  },
  "subdomains": [
    {
      "subdomain": "www.example.com",
      "ips": ["93.184.216.34"]
    }
  ]
}
```

## 🛡️ Security & Ethics

### ⚠️ CRITICAL LEGAL NOTICE

**This tool is for AUTHORIZED security testing ONLY.**

### Legal Requirements

- ✅ **You MUST have explicit written permission** before scanning any system
- ✅ **Only scan systems you own** or have authorization to test
- ✅ **Comply with all local, state, and federal laws**
- ✅ **Respect bug bounty program rules** and scope limitations
- ❌ **Unauthorized scanning is ILLEGAL** in most jurisdictions
- ❌ **You are responsible** for how you use this tool

### Responsible Use

This tool should be used for:
- Authorized penetration testing
- Bug bounty programs (within scope)
- Security audits of your own systems
- Educational purposes in controlled environments
- Red team exercises with proper authorization

### Disclaimer

The developers of CypherWolf:
- Are NOT responsible for misuse of this tool
- Do NOT condone illegal activities
- Provide this tool for educational and authorized testing ONLY
- Assume NO liability for actions taken by users

**By using this tool, you agree to use it responsibly and legally.**

## 🎓 Educational Purpose

CypherWolf is designed to help security professionals and students learn about:
- Network reconnaissance techniques
- Web application security
- DNS enumeration methods
- Port scanning strategies
- Security header analysis
- Common vulnerability patterns

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to all functions
- Test your changes thoroughly
- Update documentation as needed
- Keep security and ethics in mind

## 🐛 Bug Reports & Feature Requests

Found a bug or have an idea? Please:
1. Check existing issues first
2. Create a detailed issue with:
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment details
   - Screenshots if applicable

## 📝 Roadmap

- [ ] Integration with Shodan and Censys APIs
- [ ] Automated exploit suggestion system
- [ ] GraphQL endpoint discovery
- [ ] AWS S3 bucket enumeration
- [ ] API endpoint fuzzing
- [ ] Automated report generation (HTML/PDF)
- [ ] Integration with Metasploit
- [ ] Plugin system for custom modules
- [ ] Web-based dashboard
- [ ] Docker container support
- [ ] CI/CD pipeline integration

## 🏆 Credits & Acknowledgments

Built with:
- [dnspython](https://www.dnspython.org/) - DNS toolkit
- [requests](https://requests.readthedocs.io/) - HTTP library

Inspired by:
- Nmap - Network mapper
- Recon-ng - Reconnaissance framework
- theHarvester - OSINT tool
- Sublist3r - Subdomain enumerator

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Additional Terms

This software is intended for authorized security testing only. Users must:
1. Obtain explicit written permission before scanning
2. Comply with all applicable laws and regulations
3. Use responsibly and ethically
4. Not use for malicious purposes

## 👤 Author

**Abdul Aziz**
- GitHub: [@jjj-abdulaziz](https://github.com/jjj-abdulaziz)

## ⭐ Show Your Support

If CypherWolf helped you in your security research or learning journey, please give it a ⭐️!

---

<div align="center">

**Made with ❤️ for the security community**

*Stay curious, stay ethical, stay secure* 🐺

</div>
