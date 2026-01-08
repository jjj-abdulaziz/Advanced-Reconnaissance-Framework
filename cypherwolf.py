#!/usr/bin/env python3
"""
CypherWolf - Advanced Reconnaissance Scanner
An intelligent, modular penetration testing framework
Author: Your Name
Version: 1.0.0
"""

import socket
import ssl
import requests
import dns.resolver
import subprocess
import sys
import argparse
import concurrent.futures
import json
import time
import re
import hashlib
from datetime import datetime
from urllib.parse import urlparse, urljoin
from collections import defaultdict
import threading

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ASCII Art Banner
BANNER = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗           ║
║  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗          ║
║  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝          ║
║  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗          ║
║  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║          ║
║   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝          ║
║                                                               ║
║            WOLF - Advanced Recon Framework                    ║
║         Intelligent Reconnaissance & OSINT Tool               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'

class Logger:
    """Enhanced logging system with levels and timestamps"""
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.results = []
        self.lock = threading.Lock()
    
    def log(self, message, level="info", save=True):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        icons = {
            "info": "ℹ",
            "success": "✓",
            "warning": "⚠",
            "error": "✗",
            "scan": "🔍",
            "found": "🎯",
            "vuln": "🚨"
        }
        
        colors = {
            "info": Colors.BLUE,
            "success": Colors.GREEN,
            "warning": Colors.YELLOW,
            "error": Colors.RED,
            "scan": Colors.CYAN,
            "found": Colors.GREEN,
            "vuln": Colors.RED
        }
        
        icon = icons.get(level, "•")
        color = colors.get(level, Colors.ENDC)
        
        output = f"[{Colors.GRAY}{timestamp}{Colors.ENDC}] {color}{icon}{Colors.ENDC} {message}"
        
        if level != "info" or self.verbose:
            print(output)
        
        if save:
            with self.lock:
                self.results.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message
                })
    
    def header(self, text):
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'─' * 70}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.CYAN}  {text}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'─' * 70}{Colors.ENDC}\n")

class NetworkScanner:
    """Advanced network scanning module"""
    
    def __init__(self, logger):
        self.logger = logger
        self.results = {}
    
    def advanced_port_scan(self, target, ports=None, threads=100):
        """Multi-threaded port scanner with service detection"""
        self.logger.header("PORT SCANNING MODULE")
        
        if ports is None:
            # Comprehensive port list
            ports = list(range(1, 1024))  # Well-known ports
            ports.extend([1433, 1521, 3306, 3389, 5432, 5900, 6379, 8000, 8080, 8443, 9090, 27017])
        
        open_ports = []
        total = len(ports)
        scanned = 0
        
        def scan_port(port):
            nonlocal scanned
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((target, port))
                sock.close()
                
                if result == 0:
                    # Try to grab banner
                    banner = self._grab_banner(target, port)
                    service = self._identify_service(port, banner)
                    
                    port_info = {
                        "port": port,
                        "service": service,
                        "banner": banner,
                        "state": "open"
                    }
                    
                    self.logger.log(f"Port {port}/{service} - OPEN {banner}", "found")
                    return port_info
                    
            except:
                pass
            finally:
                scanned += 1
                if scanned % 100 == 0:
                    self.logger.log(f"Progress: {scanned}/{total} ports scanned", "info")
            
            return None
        
        self.logger.log(f"Scanning {total} ports with {threads} threads...", "scan")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            results = executor.map(scan_port, ports)
            open_ports = [r for r in results if r is not None]
        
        self.results['ports'] = open_ports
        self.logger.log(f"Found {len(open_ports)} open ports", "success")
        return open_ports
    
    def _grab_banner(self, target, port, timeout=2):
        """Attempt to grab service banner"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((target, port))
            
            # Try sending HTTP request for web services
            if port in [80, 8080, 8000, 8443]:
                sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            
            return banner[:100] if banner else ""
        except:
            return ""
    
    def _identify_service(self, port, banner):
        """Enhanced service identification"""
        common_services = {
            20: 'FTP-DATA', 21: 'FTP', 22: 'SSH', 23: 'Telnet',
            25: 'SMTP', 53: 'DNS', 80: 'HTTP', 110: 'POP3',
            143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS',
            995: 'POP3S', 1433: 'MSSQL', 1521: 'Oracle', 3306: 'MySQL',
            3389: 'RDP', 5432: 'PostgreSQL', 5900: 'VNC', 6379: 'Redis',
            8000: 'HTTP-Alt', 8080: 'HTTP-Proxy', 8443: 'HTTPS-Alt',
            9090: 'WebSM', 27017: 'MongoDB'
        }
        
        service = common_services.get(port, 'unknown')
        
        # Banner-based detection
        if banner:
            banner_lower = banner.lower()
            if 'ssh' in banner_lower:
                service = f"SSH ({banner.split()[0]})"
            elif 'http' in banner_lower:
                service = f"HTTP ({banner.split()[0]})"
            elif 'ftp' in banner_lower:
                service = f"FTP ({banner.split()[0]})"
        
        return service

class DNSRecon:
    """Advanced DNS reconnaissance"""
    
    def __init__(self, logger):
        self.logger = logger
        self.results = {}
    
    def comprehensive_dns_scan(self, target):
        """Comprehensive DNS enumeration"""
        self.logger.header("DNS RECONNAISSANCE MODULE")
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME', 'PTR', 'SRV']
        dns_data = {}
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(target, record_type)
                records = []
                
                for rdata in answers:
                    record_value = str(rdata)
                    records.append(record_value)
                    self.logger.log(f"{record_type}: {record_value}", "found")
                
                dns_data[record_type] = records
                
            except dns.resolver.NoAnswer:
                self.logger.log(f"No {record_type} records", "info")
            except dns.resolver.NXDOMAIN:
                self.logger.log(f"Domain does not exist", "error")
                return None
            except Exception as e:
                self.logger.log(f"Error with {record_type}: {str(e)}", "warning")
        
        # Zone transfer attempt
        self.logger.log("Attempting zone transfer...", "scan")
        zone_transfer = self._attempt_zone_transfer(target, dns_data.get('NS', []))
        if zone_transfer:
            dns_data['zone_transfer'] = zone_transfer
        
        self.results = dns_data
        return dns_data
    
    def _attempt_zone_transfer(self, target, nameservers):
        """Attempt DNS zone transfer (AXFR)"""
        transfers = []
        
        for ns in nameservers:
            try:
                ns_clean = ns.rstrip('.')
                zone = dns.zone.from_xfr(dns.query.xfr(ns_clean, target))
                transfers.append({
                    'nameserver': ns,
                    'records': len(zone.nodes)
                })
                self.logger.log(f"Zone transfer successful from {ns}!", "vuln")
            except:
                pass
        
        return transfers if transfers else None

class WebAnalyzer:
    """Advanced web application analysis"""
    
    def __init__(self, logger):
        self.logger = logger
        self.results = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
    
    def comprehensive_web_scan(self, target):
        """Comprehensive web application scanning"""
        self.logger.header("WEB APPLICATION ANALYSIS")
        
        url = target if target.startswith('http') else f'https://{target}'
        
        results = {}
        
        # Security headers
        results['headers'] = self._check_security_headers(url)
        
        # Technology detection
        results['technologies'] = self._detect_technologies(url)
        
        # Directory enumeration
        results['directories'] = self._directory_bruteforce(url)
        
        # Vulnerability checks
        results['vulnerabilities'] = self._vulnerability_checks(url)
        
        # SSL/TLS analysis
        results['ssl'] = self._ssl_analysis(target)
        
        # Cookie analysis
        results['cookies'] = self._analyze_cookies(url)
        
        self.results = results
        return results
    
    def _check_security_headers(self, url):
        """Enhanced security header checking"""
        self.logger.log("Analyzing security headers...", "scan")
        
        try:
            response = self.session.get(url, timeout=10, verify=False)
            headers = response.headers
            
            security_headers = {
                'Strict-Transport-Security': {'found': False, 'severity': 'high'},
                'Content-Security-Policy': {'found': False, 'severity': 'high'},
                'X-Frame-Options': {'found': False, 'severity': 'medium'},
                'X-Content-Type-Options': {'found': False, 'severity': 'medium'},
                'X-XSS-Protection': {'found': False, 'severity': 'low'},
                'Referrer-Policy': {'found': False, 'severity': 'low'},
                'Permissions-Policy': {'found': False, 'severity': 'low'}
            }
            
            score = 0
            max_score = len(security_headers)
            
            for header, info in security_headers.items():
                if header in headers:
                    info['found'] = True
                    info['value'] = headers[header]
                    score += 1
                    self.logger.log(f"✓ {header}: {headers[header]}", "success")
                else:
                    self.logger.log(f"✗ Missing: {header} [{info['severity']} risk]", "warning")
            
            # Check for information disclosure
            if 'Server' in headers:
                self.logger.log(f"Server header disclosed: {headers['Server']}", "warning")
            
            if 'X-Powered-By' in headers:
                self.logger.log(f"X-Powered-By disclosed: {headers['X-Powered-By']}", "warning")
            
            return {
                'headers': security_headers,
                'score': f"{score}/{max_score}",
                'grade': self._calculate_grade(score, max_score)
            }
            
        except Exception as e:
            self.logger.log(f"Error checking headers: {str(e)}", "error")
            return {}
    
    def _detect_technologies(self, url):
        """Advanced technology fingerprinting"""
        self.logger.log("Detecting technologies...", "scan")
        
        technologies = []
        
        try:
            response = self.session.get(url, timeout=10, verify=False)
            html = response.text.lower()
            headers = response.headers
            
            # Framework detection patterns
            detections = {
                'WordPress': [r'wp-content', r'wp-includes', r'wordpress'],
                'Joomla': [r'joomla', r'/components/com_'],
                'Drupal': [r'drupal', r'/sites/all/'],
                'React': [r'react', r'_react', r'reactdom'],
                'Angular': [r'angular', r'ng-version'],
                'Vue.js': [r'vue\.js', r'__vue__', r'data-v-'],
                'jQuery': [r'jquery'],
                'Bootstrap': [r'bootstrap'],
                'Laravel': [r'laravel', r'laravel_session'],
                'Django': [r'csrfmiddlewaretoken', r'django'],
                'Flask': [r'flask'],
                'Next.js': [r'__next', r'_next/static'],
                'Gatsby': [r'gatsby'],
                'Nuxt.js': [r'__nuxt', r'nuxt'],
                'Webpack': [r'webpack'],
                'Vite': [r'vite'],
                'Tailwind': [r'tailwind'],
                'Material-UI': [r'material-ui', r'mui']
            }
            
            for tech, patterns in detections.items():
                for pattern in patterns:
                    if re.search(pattern, html) or re.search(pattern, str(headers).lower()):
                        technologies.append(tech)
                        self.logger.log(f"Detected: {tech}", "found")
                        break
            
            # CMS detection
            if 'wp-json' in html:
                technologies.append('WordPress REST API')
                self.logger.log("WordPress REST API exposed", "warning")
            
            # Check for common JS libraries
            js_libs = ['axios', 'lodash', 'moment.js', 'chart.js', 'd3.js']
            for lib in js_libs:
                if lib in html:
                    technologies.append(lib)
                    self.logger.log(f"Detected: {lib}", "info")
            
            return list(set(technologies))
            
        except Exception as e:
            self.logger.log(f"Error detecting technologies: {str(e)}", "error")
            return technologies
    
    def _directory_bruteforce(self, url):
        """Smart directory enumeration"""
        self.logger.log("Enumerating directories...", "scan")
        
        common_dirs = [
            'admin', 'administrator', 'login', 'dashboard', 'panel',
            'api', 'v1', 'v2', 'docs', 'documentation',
            'backup', 'backups', 'old', 'temp', 'tmp',
            '.git', '.env', '.htaccess', 'config', 'conf',
            'uploads', 'images', 'files', 'assets', 'static',
            'wp-admin', 'wp-content', 'wp-includes',
            'phpmyadmin', 'phpMyAdmin', 'pma',
            'test', 'dev', 'staging', 'beta',
            'robots.txt', 'sitemap.xml', 'crossdomain.xml'
        ]
        
        found_dirs = []
        
        for directory in common_dirs:
            try:
                test_url = urljoin(url, directory)
                response = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                
                if response.status_code in [200, 301, 302, 403]:
                    found_dirs.append({
                        'path': directory,
                        'status': response.status_code,
                        'size': len(response.content)
                    })
                    
                    status_color = "found" if response.status_code == 200 else "warning"
                    self.logger.log(f"Found: /{directory} [{response.status_code}]", status_color)
                    
            except:
                pass
        
        return found_dirs
    
    def _vulnerability_checks(self, url):
        """Basic vulnerability detection"""
        self.logger.log("Running vulnerability checks...", "scan")
        
        vulnerabilities = []
        
        # Check for clickjacking
        try:
            response = self.session.get(url, timeout=10, verify=False)
            if 'X-Frame-Options' not in response.headers and 'Content-Security-Policy' not in response.headers:
                vulnerabilities.append({
                    'type': 'Clickjacking',
                    'severity': 'medium',
                    'description': 'Missing X-Frame-Options and CSP frame-ancestors'
                })
                self.logger.log("Potential clickjacking vulnerability", "vuln")
        except:
            pass
        
        # Check for directory listing
        test_paths = ['/', '/images/', '/uploads/', '/files/']
        for path in test_paths:
            try:
                test_url = urljoin(url, path)
                response = self.session.get(test_url, timeout=5, verify=False)
                if 'index of' in response.text.lower():
                    vulnerabilities.append({
                        'type': 'Directory Listing',
                        'severity': 'medium',
                        'path': path
                    })
                    self.logger.log(f"Directory listing enabled at {path}", "vuln")
            except:
                pass
        
        return vulnerabilities
    
    def _ssl_analysis(self, target):
        """SSL/TLS configuration analysis"""
        self.logger.log("Analyzing SSL/TLS...", "scan")
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((target, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=target) as ssock:
                    cert = ssock.getpeercert()
                    
                    ssl_info = {
                        'version': ssock.version(),
                        'cipher': ssock.cipher()[0],
                        'cert_subject': dict(x[0] for x in cert['subject']),
                        'cert_issuer': dict(x[0] for x in cert['issuer']),
                        'valid_from': cert['notBefore'],
                        'valid_until': cert['notAfter']
                    }
                    
                    self.logger.log(f"SSL/TLS Version: {ssl_info['version']}", "success")
                    self.logger.log(f"Cipher: {ssl_info['cipher']}", "info")
                    
                    return ssl_info
        except Exception as e:
            self.logger.log(f"SSL analysis failed: {str(e)}", "error")
            return {}
    
    def _analyze_cookies(self, url):
        """Cookie security analysis"""
        self.logger.log("Analyzing cookies...", "scan")
        
        try:
            response = self.session.get(url, timeout=10, verify=False)
            cookies = response.cookies
            
            cookie_analysis = []
            
            for cookie in cookies:
                analysis = {
                    'name': cookie.name,
                    'secure': cookie.secure,
                    'httponly': cookie.has_nonstandard_attr('HttpOnly'),
                    'samesite': cookie.get_nonstandard_attr('SameSite')
                }
                
                if not cookie.secure:
                    self.logger.log(f"Cookie '{cookie.name}' missing Secure flag", "warning")
                
                if not analysis['httponly']:
                    self.logger.log(f"Cookie '{cookie.name}' missing HttpOnly flag", "warning")
                
                cookie_analysis.append(analysis)
            
            return cookie_analysis
            
        except:
            return []
    
    def _calculate_grade(self, score, max_score):
        """Calculate security grade"""
        percentage = (score / max_score) * 100
        
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'

class SubdomainHunter:
    """Advanced subdomain enumeration"""
    
    def __init__(self, logger):
        self.logger = logger
        self.results = []
    
    def hunt_subdomains(self, target, wordlist=None):
        """Multi-technique subdomain discovery"""
        self.logger.header("SUBDOMAIN ENUMERATION")
        
        subdomains = set()
        
        # Certificate transparency
        self.logger.log("Checking certificate transparency logs...", "scan")
        ct_subdomains = self._check_crt_sh(target)
        subdomains.update(ct_subdomains)
        
        # DNS bruteforce
        self.logger.log("Performing DNS bruteforce...", "scan")
        if wordlist:
            bruteforce_subs = self._bruteforce_subdomains(target, wordlist)
        else:
            bruteforce_subs = self._bruteforce_subdomains(target, self._get_default_wordlist())
        subdomains.update(bruteforce_subs)
        
        # Resolve all found subdomains
        resolved_subdomains = []
        for subdomain in subdomains:
            ips = self._resolve_subdomain(subdomain)
            if ips:
                resolved_subdomains.append({
                    'subdomain': subdomain,
                    'ips': ips
                })
                self.logger.log(f"Found: {subdomain} → {', '.join(ips)}", "found")
        
        self.results = resolved_subdomains
        self.logger.log(f"Total subdomains found: {len(resolved_subdomains)}", "success")
        return resolved_subdomains
    
    def _check_crt_sh(self, target):
        """Query certificate transparency logs"""
        try:
            url = f"https://crt.sh/?q=%.{target}&output=json"
            response = requests.get(url, timeout=15)
            data = response.json()
            
            subdomains = set()
            for cert in data:
                names = cert.get('name_value', '').split('\n')
                for name in names:
                    name = name.strip().lower()
                    if name.endswith(target) and '*' not in name:
                        subdomains.add(name)
            
            return subdomains
        except:
            return set()
    
    def _bruteforce_subdomains(self, target, wordlist):
        """Bruteforce subdomain discovery"""
        found = set()
        
        def check_subdomain(word):
            subdomain = f"{word}.{target}"
            if self._resolve_subdomain(subdomain):
                return subdomain
            return None
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(check_subdomain, wordlist)
            found = {r for r in results if r}
        
        return found
    
    def _resolve_subdomain(self, subdomain):
        """Resolve subdomain to IP addresses"""
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            return [str(rdata) for rdata in answers]
        except:
            return None
    
    def _get_default_wordlist(self):
        """Get default subdomain wordlist"""
        return [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
            'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'mx', 'm', 'mobile',
            'admin', 'administrator', 'login', 'portal', 'dev', 'development', 'test',
            'staging', 'qa', 'uat', 'beta', 'alpha', 'demo', 'api', 'api-v1', 'api-v2',
            'app', 'apps', 'cdn', 'static', 'assets', 'media', 'images', 'img', 'www1',
            'www2', 'vpn', 'remote', 'cloud', 'secure', 'backup', 'shop', 'store',
            'blog', 'forum', 'support', 'help', 'docs', 'status', 'monitor', 'wiki'
        ]

class CypherWolf:
    """Main scanner orchestrator"""
    
    def __init__(self, target, args):
        self.target = target
        self.args = args
        self.logger = Logger(verbose=args.verbose)
        
        # Initialize modules
        self.network_scanner = NetworkScanner(self.logger)
        self.dns_recon = DNSRecon(self.logger)
        self.web_analyzer = WebAnalyzer(self.logger)
        self.subdomain_hunter = SubdomainHunter(self.logger)
        
        self.results = {
            'target': target,
            'timestamp': datetime.now().isoformat(),
            'scan_type': args.mode
        }
    
    def run(self):
        """Execute the scan based on mode"""
        print(f"{Colors.CYAN}{BANNER}{Colors.ENDC}")
        print(f"{Colors.BOLD}Target:{Colors.ENDC} {Colors.CYAN}{self.target}{Colors.ENDC}")
        print(f"{Colors.BOLD}Mode:{Colors.ENDC} {Colors.CYAN}{self.args.mode}{Colors.ENDC}")
        print(f"{Colors.BOLD}Started:{Colors.ENDC} {Colors.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.ENDC}\n")
        
        self.logger.log("⚠ LEGAL WARNING: Only scan authorized systems!", "warning")
        print()
        
        mode = self.args.mode
        
        try:
            if mode in ['dns', 'full']:
                self.results['dns'] = self.dns_recon.comprehensive_dns_scan(self.target)
            
            if mode in ['ports', 'full']:
                self.results['ports'] = self.network_scanner.advanced_port_scan(
                    self.target,
                    threads=self.args.threads
                )
            
            if mode in ['web', 'full']:
                self.results['web'] = self.web_analyzer.comprehensive_web_scan(self.target)
            
            if mode in ['subdomain', 'full']:
                self.results['subdomains'] = self.subdomain_hunter.hunt_subdomains(self.target)
            
            # Generate report
            self._generate_report()
            
            # Save results
            if self.args.output:
                self._save_results()
            
        except KeyboardInterrupt:
            self.logger.log("\nScan interrupted by user", "warning")
            sys.exit(0)
        except Exception as e:
            self.logger.log(f"Critical error: {str(e)}", "error")
            sys.exit(1)
    
    def _generate_report(self):
        """Generate scan summary report"""
        self.logger.header("SCAN SUMMARY")
        
        # DNS Summary
        if 'dns' in self.results:
            dns_count = sum(len(v) if isinstance(v, list) else 1 
                          for v in self.results['dns'].values() if v)
            print(f"{Colors.BOLD}DNS Records:{Colors.ENDC} {dns_count} found")
        
        # Port Summary
        if 'ports' in self.results:
            open_count = len(self.results['ports'])
            print(f"{Colors.BOLD}Open Ports:{Colors.ENDC} {open_count} found")
        
        # Web Summary
        if 'web' in self.results:
            tech_count = len(self.results['web'].get('technologies', []))
            vuln_count = len(self.results['web'].get('vulnerabilities', []))
            headers_info = self.results['web'].get('headers', {})
            security_grade = headers_info.get('grade', 'N/A') if headers_info else 'N/A'
            print(f"{Colors.BOLD}Technologies:{Colors.ENDC} {tech_count} detected")
            print(f"{Colors.BOLD}Security Grade:{Colors.ENDC} {security_grade}")
            print(f"{Colors.BOLD}Vulnerabilities:{Colors.ENDC} {vuln_count} found")
        
        # Subdomain Summary
        if 'subdomains' in self.results:
            subdomain_count = len(self.results['subdomains'])
            print(f"{Colors.BOLD}Subdomains:{Colors.ENDC} {subdomain_count} found")
        
        print(f"\n{Colors.GREEN}Scan completed successfully!{Colors.ENDC}\n")
    
    def _save_results(self):
        """Save results to JSON file"""
        try:
            with open(self.args.output, 'w') as f:
                json.dump(self.results, f, indent=4, default=str)
            self.logger.log(f"Results saved to {self.args.output}", "success")
        except Exception as e:
            self.logger.log(f"Error saving results: {str(e)}", "error")

def main():
    parser = argparse.ArgumentParser(
        description='CypherWolf - Advanced Reconnaissance Scanner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 cypherwolf.py example.com -m full
  python3 cypherwolf.py example.com -m web -o results.json
  python3 cypherwolf.py example.com -m ports --threads 200
  python3 cypherwolf.py example.com -m subdomain -v
        """
    )
    
    parser.add_argument('target', help='Target domain or IP address')
    parser.add_argument('-m', '--mode', 
                       choices=['dns', 'ports', 'web', 'subdomain', 'full'],
                       default='full',
                       help='Scan mode (default: full)')
    parser.add_argument('-o', '--output', 
                       help='Save results to JSON file')
    parser.add_argument('-t', '--threads', 
                       type=int, 
                       default=100,
                       help='Number of threads for port scanning (default: 100)')
    parser.add_argument('-v', '--verbose', 
                       action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--version', 
                       action='version', 
                       version='CypherWolf v1.0.0')
    
    args = parser.parse_args()
    
    # Clean target
    target = args.target.replace('http://', '').replace('https://', '').split('/')[0]
    
    # Initialize and run scanner
    scanner = CypherWolf(target, args)
    scanner.run()

if __name__ == "__main__":
    main()