#!/usr/bin/env python
import subprocess
import ipaddress
import nmap
import penkraken

class openPorts:

    def __init__(self):
        ip = input(f"{penkraken.colors['blue']}\n[>] Target IP: {penkraken.colors['reset']}")
        ip_address = ipaddress.ip_address(ip)
        self.ports_discovered = ''
        self.openPorts(ip_address)
        
    
    def openPorts(self,ip_address):
        try:
            self.count = 0
            while True:
                prange = input(f"{penkraken.colors['blue']}[>] Specify port range to scan (from 1 to 65535): {penkraken.colors['reset']}")
                if prange.isnumeric() and int(prange) in range(1, 65536):
                    break
                else:
                    print(f"{penkraken.colors['red']}\n[-] Invalid port range{penkraken.colors['reset']}")
        
            for port in range(1,int(prange)):
                proc = subprocess.Popen(["/bin/echo '' > /dev/tcp/"+str(ip_address)+"/"+str(port)+" 2>&/dev/null"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                (out, err) = proc.communicate()
                if b'ambiguous redirect' in out:
                    print(f"{penkraken.colors['magenta']}[+] Open Port:{penkraken.colors['red']} {str(port)} !!{penkraken.colors['reset']}")
                    self.count +=1
                    self.ports_discovered += str(port) + ' '

            # Display ports
            print(f"{penkraken.colors['green']}\n[+] Scan Completed!{penkraken.colors['reset']}")
            print(f"{penkraken.colors['magenta']}[+] Discovered Ports: {penkraken.colors['red']}{str(self.count)}{penkraken.colors['reset']}")
            print(f"{penkraken.colors['magenta']}[+] Ports: {penkraken.colors['red']}{self.ports_discovered}{penkraken.colors['reset']}")
        except:
            print(f"{penkraken.colors['red']}\n[-] Failed while scanning ports!{penkraken.colors['reset']}")


class nmapPorts:

    def __init__(self):
        ip = input(f"{penkraken.colors['blue']}\n[>] Target IP: {penkraken.colors['reset']}")
        ip_address = ipaddress.ip_address(ip)
        self.ports_discovered = ''
        self.portScan(ip_address)
    
    def portScan(self,ip_address):
        self.count = 0
        options = {'prange': 10000, 'aggression': 3, 'scripts': '', 'avoid_dns_res': '-n', 'skip_ping': '-Pn'}
        default = input(f"{penkraken.colors['blue']}\n[>] Use default options 'nmap -p0-10000 -T3 -sV -n -Pn' ? (y/n): {penkraken.colors['reset']}")
        if 'n' in str(default).lower():
            print(f"{penkraken.colors['blue']}\n[+] Time to set up scan options")
            # Port range
            while True:
                prange = input(f"{penkraken.colors['green']}\n[>] Specify port range to scan (from 1 to 65535): {penkraken.colors['reset']}")
                if prange.isnumeric() and int(prange) in range(1, 65536):
                    options['prange'] = int(prange)
                    break
                else:
                    print(f"{penkraken.colors['red']}\n[-] Invalid port range{penkraken.colors['reset']}")
            # Aggression level
            while True:
                aggression = input(f"{penkraken.colors['blue']}[>] Specify aggression level (1-5): {penkraken.colors['reset']}")
                if aggression.isnumeric() and int(aggression) in range(1,6):
                    options['aggression'] = int(aggression)
                    break
                else:
                    print(f"{penkraken.colors['red']}\n[-] Invalid Aggression Level{penkraken.colors['reset']}")
            # Include Scripts
            while True:
                scripts = input(f"{penkraken.colors['blue']}[>] Would you like to use nmap scripts? (y/n): {penkraken.colors['reset']}")
                if 'y' in str(scripts).lower():
                    options['scripts'] = 'C'
                    break
                elif 'n' in str(scripts).lower():
                    break
                else:
                    print(f"{penkraken.colors['red']}\n[-] Didn't understand your input{penkraken.colors['reset']}")
            # Include dns resolution
            while True:
                dns = input(f"{penkraken.colors['blue']}[>] Would you like to avoid using dns resolution (-n)? (y/n): {penkraken.colors['reset']}")
                if 'n' in str(dns).lower():
                    options['avoid_dns_res'] = ''
                    break
                elif 'y' in str(dns).lower():
                    break
                else:
                    print(f"{penkraken.colors['red']}\n[-] Didn't understand your input{penkraken.colors['reset']}")
            # Avoid using NoPing
            while True:
                ping = input(f"{penkraken.colors['blue']}[>] Would you like to use NoPing option (-Pn)? (y/n): {penkraken.colors['reset']}")
                if 'n' in str(ping).lower():
                    options['avoid_dns_res'] = ''
                    break
                elif 'y' in str(ping).lower():
                    break
                else:
                    print(f"{penkraken.colors['red']}\n[-] Didn't understand your input{penkraken.colors['reset']}")

        else:
            pass

        try:
            print(f"{penkraken.colors['green']}\n[+] Starting nmap scan (This could take some time...){penkraken.colors['reset']}") 
            nm_arguments = "-p0-"+str(options['prange'])+" -T"+str(options['aggression'])+" -sV"+str(options['scripts'])+ " " +str(options['avoid_dns_res']) + " "+ str(options['skip_ping'])
            nm = nmap.PortScanner()
            dump = nm.scan(hosts=str(ip_address), arguments=nm_arguments)
            tcp = dump['scan'][str(ip_address)]['tcp']
            results = ''
            for k,v in tcp.items():
                if v['state'] == 'open':
                    results+="\n[+] Open port: " + str(k)
                    self.count += 1
                    self.ports_discovered += str(k) + " "
                    results+="\n[+] Port info:"
                    for x,y in v.items():
                        if str(x) == "script":
                            results+="\n   -> Scripts:"
                            for a,b in y.items():
                                 results+="\n      -> " + str(a) + " : " + str(b)
                        else:
                            results+="\n   -> " + str(x) + " : " + str(y)
            
            print(f"{penkraken.colors['green']}{results}{penkraken.colors['reset']}")
            print(f"{penkraken.colors['green']}\n[+] Scan Completed!{penkraken.colors['reset']}")
            print(f"{penkraken.colors['magenta']}[+] Discovered Ports: {penkraken.colors['red']}{str(self.count)}{penkraken.colors['reset']}")
            print(f"{penkraken.colors['magenta']}[+] Ports: {penkraken.colors['red']}{self.ports_discovered}{penkraken.colors['reset']}")
            write_output = input(f"{penkraken.colors['blue']}\n[>] Would you like to write the nmap scan results to a file? (y/n): {penkraken.colors['reset']}")
            if 'y' in str(write_output).lower():
                file = open("Nmap-Results.txt", "w")
                file.write(results)
                file.close()
                print(f"{penkraken.colors['green']}\n[+] Results were succesfully exported to 'Nmap-Results.txt'{penkraken.colors['reset']}")
            else:
                pass            
                            
        except:
            print(f"{penkraken.colors['red']}\n[-] Nmap command failed{penkraken.colors['reset']}")

        


def Init():
    try:
        while True:
            x = input(f"{penkraken.colors['green']}\n[1] OpenPorts Discovery Script\n[2] Nmap Full Ports & Services Scan\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
            if str(x) != '1' and str(x) != '2':
                print(f"{penkraken.colors['red']}\n[-] Invalid Option{penkraken.colors['reset']}")
            else:
                break
    
        if str(x) == '1':
            target = openPorts()
        elif str(x) == '2':
            target = nmapPorts()

        # Return ports
        return ''.join("\n[+] " + str(x) for x in target.ports_discovered.split())

    except ValueError:
        print(f"{penkraken.colors['red']}[-] Invalid address: %s{penkraken.colors['reset']}" % sys.argv[1])
        sys.exit(1)

    except:
            print(f"{penkraken.colors['red']}\n[-] Exiting Port Scan{penkraken.colors['reset']}")

 