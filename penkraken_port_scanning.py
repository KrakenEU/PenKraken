#!/usr/bin/env python
import subprocess
import ipaddress
import nmap

class openPorts:

    def __init__(self):
        ip = input("\n[>] Target IP: ")
        ip_address = ipaddress.ip_address(ip)
        self.ports_discovered = ''
        self.openPorts(ip_address)
        
    
    def openPorts(self,ip_address):
        self.count = 0
        while True:
            prange = input("[>] Specify port range to scan (from 1 to 65535): ")
            if prange.isnumeric() and int(prange) in range(1, 65536):
                break
            else:
                print("\n[-] Invalid port range")
    
        for port in range(1,int(prange)):
            proc = subprocess.Popen(["/bin/echo '' > /dev/tcp/"+str(ip_address)+"/"+str(port)+" 2>&/dev/null"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            (out, err) = proc.communicate()
            if b'ambiguous redirect' in out:
                print("[+] Open Port: " + str(port)+" !!")
                self.count +=1
                self.ports_discovered += str(port) + ' '

        # Display ports
        print("\n[+] Scan Completed!")
        print("[+] Discovered Ports: " + str(self.count))
        print("[+] Ports: " + self.ports_discovered)


class nmapPorts:

    def __init__(self):
        ip = input("\n[>] Target IP: ")
        ip_address = ipaddress.ip_address(ip)
        self.ports_discovered = ''
        self.portScan(ip_address)
    
    def portScan(self,ip_address):
        self.count = 0
        options = {'prange': 10000, 'aggression': 3, 'scripts': '', 'avoid_dns_res': '-n', 'skip_ping': '-Pn'}
        default = input("\n[>] Use default options 'nmap -p0-10000 -T3 -sV -n -Pn' ? (y/n): ")
        if 'n' in str(default).lower():
            print("\n[+] Time to set up scan options")
            # Port range
            while True:
                prange = input("\n[>] Specify port range to scan (from 1 to 65535): ")
                if prange.isnumeric() and int(prange) in range(1, 65536):
                    options['prange'] = int(prange)
                    break
                else:
                    print("\n[-] Invalid port range")
            # Aggression level
            while True:
                aggression = input("[>] Specify aggression level (1-5): ")
                if aggression.isnumeric() and int(aggression) in range(1,6):
                    options['aggression'] = int(aggression)
                    break
                else:
                    print("\n[-] Invalid Aggression Level")
            # Include Scripts
            while True:
                scripts = input("[>] Would you like to use nmap scripts? (y/n): ")
                if 'y' in str(scripts).lower():
                    options['scripts'] = 'C'
                    break
                elif 'n' in str(scripts).lower():
                    break
                else:
                    print("\n[-] Didn't understand your input")
            # Include dns resolution
            while True:
                dns = input("[>] Would you like to avoid using dns resolution (-n)? (y/n): ")
                if 'n' in str(dns).lower():
                    options['avoid_dns_res'] = ''
                    break
                elif 'y' in str(dns).lower():
                    break
                else:
                    print("\n[-] Didn't understand your input")
            # Avoid using NoPing
            while True:
                ping = input("[>] Would you like to use NoPing option (-Pn)? (y/n): ")
                if 'n' in str(ping).lower():
                    options['avoid_dns_res'] = ''
                    break
                elif 'y' in str(ping).lower():
                    break
                else:
                    print("\n[-] Didn't understand your input")

        else:
            pass

        try:
            print("\n[+] Starting nmap scan (This could take some time...)") 
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
            
            print(results)
            print("\n[+] Scan Completed!")
            print("[+] Discovered Ports: " + str(self.count))
            print("[+] Ports: " + self.ports_discovered)
            write_output = input("\n[>] Would you like to write the nmap scan results to a file? (y/n): ")
            if 'y' in str(write_output).lower():
                file = open("Nmap-Results.txt", "w")
                file.write(results)
                file.close()
                print("\n[+] Results were succesfully exported to 'Nmap-Results.txt'")
            else:
                pass            
                            
        except:
            print("\n[-] Nmap command failed")

        


def Init():
    try:
        while True:
            x = input("\n[1] OpenPorts Discovery Script\n[2] Nmap Full Ports & Services Scan\n\n[>] Choose option: ")
            if str(x) != '1' and str(x) != '2':
                print("\n[-] Invalid Option")
            else:
                break
    
        if str(x) == '1':
            target = openPorts()
        elif str(x) == '2':
            target = nmapPorts()

        # Return ports
        return ''.join("\n[+] " + str(x) for x in target.ports_discovered.split())

    except ValueError:
        print('[-] Invalid address: %s' % sys.argv[1])
        sys.exit(1)

    except:
            print("\n[-] Exiting Program")

 