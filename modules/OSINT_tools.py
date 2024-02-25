#!/usr/bin/env python

# https://osintframework.com/ + https://github.com/topics/osint-tools
# domain/ip = https://github.com/m0rtem/CloudFail + TheHarvester + whois
# mails = https://github.com/GiJ03/Infoga + Holehe
# usernames = sherlock
# sample pdf https://pdfobject.com/pdf/sample.pdf

import sys
sys.path.append('../')
import penkraken
import subprocess

class Osint:

    def __init__(self,name):
        self.name = name
        self.doc_extensions = [".doc",".docx",".xls",".xlsx",".ppt",".pptx",".odt",".ods",".odp",".rtf",".csv",".pdf"]
        self.web_extensions = [".com",".org",".net",".gov",".edu",".int",".mil",".arpa",".biz",".info",".mobi",".name",".pro",".aero",".coop",".museum",".asia",".jobs",".tel",".travel",]

        file=False
        for x in self.doc_extensions:
            if x in name.lower():
                file = True
        
        site=False
        for x in self.web_extensions:
            if x in name.lower():
                site = True
    
        self.results = []
        if '@' in name:
            try:
                print(f"\n{penkraken.colors['green']}[+] Mail Detected!{penkraken.colors['reset']}")
                self.Holehe()
                self.infoga()
                self.h8mail()
            except:
                print(f"\n{penkraken.colors['red']}[-] Name Scan Failed{penkraken.colors['reset']}")

        elif site:
            try:
                print(f"\n{penkraken.colors['green']}[+] Domain Detected!{penkraken.colors['reset']}")
                self.TheHarvester()
                self.cloudfail()
                self.whois()
            except:
                print(f"\n{penkraken.colors['red']}[-] Mail Scan Failed{penkraken.colors['reset']}")
        
        elif file:
            try:
                print(f"\n{penkraken.colors['green']}[+] File Detected!{penkraken.colors['reset']}")
                self.exiftool()
            except:
                print(f"\n{penkraken.colors['red']}[-] Metadata extractor Failed{penkraken.colors['reset']}")     

        else:
            try:
                print(f"\n{penkraken.colors['green']}[+] Username Detected!{penkraken.colors['reset']}")
                self.sherlock()
                self.maigret()
            except:
                print(f"\n{penkraken.colors['red']}[-] Username Scan Failed{penkraken.colors['reset']}")
    
    def sherlock(self):
        try:
            output = subprocess.Popen(f'sudo sherlock {self.name}',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}\n[+] Sherlock Scan results:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Sherlock Scan Failed{penkraken.colors['reset']}")
        
    def Holehe(self):
        try:
            output = subprocess.Popen(f'holehe {self.name}',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}\n[+] Holehe Scan results:\n[+] The mail {penkraken.colors['magenta']}{self.name}{penkraken.colors['green']} has been used in:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if '[+]' in salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Holehe Scan Failed{penkraken.colors['reset']}")
    
    def infoga(self):
        try:
            output = subprocess.Popen(f'infoga --info {self.name} --breach -v 3',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}\n[+] Infoga Scan results:\n[+] The mail {penkraken.colors['magenta']}{self.name}{penkraken.colors['green']} has been used in:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Infoga Scan Failed{penkraken.colors['reset']}")
    
    def h8mail(self):
        try:
            output = subprocess.Popen(f'h8mail -t {self.name}',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}\n[+] H8Mail Scan results:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] h8mail Scan Failed{penkraken.colors['reset']}")

    def TheHarvester(self):
        try:
            output = subprocess.Popen(f'theharvester -d {self.name} -l 1000 -b bing,duckduckgo',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}\n[+] TheHarvester Scan results:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] TheHarvester Scan Failed{penkraken.colors['reset']}")
    
    def whois(self):
        try:
            output = subprocess.Popen(f'whois {self.name}',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}\n[+] Whois Scan results:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if '>>>' in salida:
                    break
                if salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")        
        except:
            print(f"\n{penkraken.colors['red']}[-] Whois Scan Failed{penkraken.colors['reset']}")
    
    def cloudfail(self):
        try:
            output = subprocess.Popen(f'cloudfail -t {self.name}',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}[+] CloudFail Results:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if 'cloudfail.py' not in salida and 'choice' not in salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] CloudFail Scan Failed{penkraken.colors['reset']}")

    def exiftool(self):
        try:
            output = subprocess.Popen(f'exiftool {self.name}',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}[+] Exiftool Results:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] ExifTool Scan Failed{penkraken.colors['reset']}")
        
    def maigret(self):
        try:
            output = subprocess.Popen(f'maigret {self.name}',stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, text=True, shell=True)
            info = f"{penkraken.colors['green']}\n[+] Maigret Scan results:\n[+] The nickname {penkraken.colors['magenta']}{self.name}{penkraken.colors['green']} has been used in:{penkraken.colors['reset']}"
            print(info)
            self.results.append(info)
            while True:
                salida = output.stdout.readline()
                if salida == '' and output.poll() is not None:
                    break
                if '100%' in salida:
                    break
                if '%' not in salida:
                    print(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
                    self.results.append(f"{penkraken.colors['magenta']}{salida.strip()}{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Holehe Scan Failed{penkraken.colors['reset']}")



def Init():
    try:
        print(f"{penkraken.colors['blue']}\n[+] Welcome to the {penkraken.colors['red']}OSINT{penkraken.colors['blue']} module!\n{penkraken.colors['reset']}")
        opt = input(f"{penkraken.colors['blue']}\n[>] Name/mail/domain/document: {penkraken.colors['reset']}")       
        target = Osint(opt)
        out = ''
        for x in target.results:
            out += x + '\n'
        return out

    except:
        print(f"{penkraken.colors['red']}\n[-] Exiting OSINT Module{penkraken.colors['reset']}")


