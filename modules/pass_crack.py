#!/usr/bin/env python

import sys
sys.path.append('../')
import penkraken
import subprocess

hashcat_modes = {
    "MD5": 0,
    "MD4": 900,
    "SHA-1": 100,
    "md5crypt" : 500,
    "phpass": 400,
    "SHA-224": 1300,
    "SHA-256": 1400,
    "SHA-512": 1700,
    "NTLM": 1000,
    "MySQL5": 300,
    "MySQL323": 200,
    "SHA2-384": 10800,
    "SHA3-224": 17300,
    "SHA3-256": 17400,
    "SHA3-384": 17500,
    "SHA3-512": 17600,
    "KeePass": 13400,
    "LM": 3000,
    "HMAC-SHA1": 160,
    "WPA/WPA2": 2500,
    "Blowfish": 5100,
    "bcrypt": 3200
}

class cracker:

    def __init__(self,hash_file):
        self.results = []
        self.hash_file = hash_file
        self.cracked = False
        self.hash_val = ''
        
        print(f"{penkraken.colors['blue']}\n[+] Attempting to Identify hash type in {penkraken.colors['magenta']}{hash_file}{penkraken.colors['blue']} file!\n{penkraken.colors['reset']}")
        self.modes = []
        
        check = self.hash_identifier(hash_file)
        
        if not check:
            print(f"{penkraken.colors['red']}\n[-] Could not Identify hash type...{penkraken.colors['reset']}")
            x = input(f"{penkraken.colors['blue']}\n[>] Manually set the hashcat hash type (ex: 0 (which is MD5)): {penkraken.colors['reset']}")
            self.modes.append(x)
        
        self.cracking_wordlist = input(f"{penkraken.colors['blue']}\n[>] Path to your password wordlist (/usr/share/wordlists/rockyou.txt as default): {penkraken.colors['reset']}")
        if self.cracking_wordlist == '':
            self.cracking_wordlist = '/usr/share/wordlists/rockyou.txt'

        while True:
            self.crack()
            if self.cracked:
                break
            else:
                print(f"{penkraken.colors['red']}\n[-] Could not break hash type...{penkraken.colors['reset']}")
                print(f"{penkraken.colors['red']}\n[+] Hash examples (more in https://hashcat.net/wiki/doku.php?id=example_hashes):{penkraken.colors['reset']}")
                for k,v in hashcat_modes.items():
                    print(f"{penkraken.colors['green']}[+] {k} = {penkraken.colors['magenta']}{v}")
                x = input(f"{penkraken.colors['blue']}\n[>] Manually set the hashcat hash type and try again (ex: 0 (which is MD5)): {penkraken.colors['reset']}")
                self.modes.insert(0, x)
        
    
    def hash_identifier(self,file):
        try:
            print(f"{penkraken.colors['blue']}\n[+] Opening File...{penkraken.colors['reset']}")
            try:
                f = open(f'{file}', 'rb')
                hash_val = str(f.read().strip().decode())
                self.hash_val = hash_val
                f.close()
                print(f"{penkraken.colors['green']}[+] OK! {penkraken.colors['reset']}")
            except:
                print(f"{penkraken.colors['red']}[-] Could Not Open {file}{penkraken.colors['reset']}")
            proc = subprocess.Popen(f"/bin/echo '{hash_val}' | hash-identifier", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
            possibles = []
            b = False
            while True:
                output = proc.stdout.readline()
                if output == '' and proc.poll() is not None:
                    break
                else:
                    if '--------------------------------------------------' in output and b == True:
                        break
                    
                    elif '--------------------------------------------------' in output:
                        b = True
                    
                    elif '[+]' in output:
                        possibles.append(output.split()[1])
                        try:
                            self.modes.append(hashcat_modes[output.split()[1]])
                        except:
                            pass
            n=0
            for p in possibles:
                if n <=5 :
                    print(f"{penkraken.colors['green']}[+] Possible hash type: {penkraken.colors['magenta']}{p}{penkraken.colors['reset']}")                     
                    search_modes = "hashcat --example-hashes | grep " + p.split('(')[0] + " -B 1 | grep \"Hash mode\" | awk '{print $3}' | tr -d '#'"
                    proc = str(subprocess.check_output(search_modes, shell=True).decode())
                    for v in proc.split('\n'):
                        if v not in self.modes and v != '':
                            self.modes.append(v)
                    n+=1
                else:
                    break
            if len(possibles) == 0:
                return False

            return True

        except:
            return False

    def crack(self):
        for mode in self.modes:
            print(f"{penkraken.colors['green']}[+] Trying mode {penkraken.colors['magenta']}{mode}{penkraken.colors['reset']}")
            com = f"hashcat -m {mode} {self.hash_file} {self.cracking_wordlist}"
            proc = subprocess.Popen(com, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
            possibles = []
            cont=True
            process = []
            while cont:
                output = proc.stdout.readline()
                if output == '' and proc.poll() is not None:
                    break
                else:
                    if 'No hashes loaded.' in output:
                        print(f"{penkraken.colors['red']}[+] Mode {mode} not valid!{penkraken.colors['reset']}")
                        break
                    if 'Cracked' in output:
                        print(f"{penkraken.colors['green']}[+] Cracked! {penkraken.colors['reset']}")
                        self.results.append(f"{penkraken.colors['green']}{process[-4]}{penkraken.colors['reset']}")
                        cont = False
                        self.cracked = True
                        break
                    if 'Use --show to display them' in output:
                        com = f"hashcat -m {mode} {self.hash_file} {self.cracking_wordlist} --show"
                        proc = subprocess.check_output(com, shell=True)
                        print(f"{penkraken.colors['green']}[+] This Was already Cracked: {str(proc.decode())} {penkraken.colors['reset']}")
                        self.results.append(f"{penkraken.colors['green']}[+] This Was already Cracked: {str(proc.decode())} {penkraken.colors['reset']}")
                        cont = False
                        self.cracked = True
                        break
                    elif output:
                        print(f"{penkraken.colors['magenta']}{output.strip()}{penkraken.colors['reset']}")
                        process.append(output)
            if not cont:
                break
        
                
def Init():
    try:
        print(f"{penkraken.colors['blue']}\n[+] Welcome to the {penkraken.colors['red']}Password Cracking{penkraken.colors['blue']} module!\n{penkraken.colors['reset']}")
        hash_file = input(f"{penkraken.colors['blue']}\n[>] File with hash: {penkraken.colors['reset']}")       
        target = cracker(hash_file)
        out = ''
        for x in target.results:
            out += x + '\n'
        return out

    except:
        print(f"{penkraken.colors['red']}\n[-] Exiting Password Cracking Module{penkraken.colors['reset']}")

