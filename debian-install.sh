#!/bin/bash

echo '[+] Installing Required Packages...'
sudo apt install golang-go wafw00f nmap exploitdb wget git sherlock whois h8mail theharvester exiftool hash-identifier hashcat
sudo pip3 install python-nmap requests holehe
echo '[+] Installing Some manual Packages into ~/tools/...'
mkdir /home/$USER/tools
sudo git clone https://github.com/jmbr/halberd && cd halberd && sudo python2 setup.py install
git clone https://github.com/GiJ03/Infoga /home/$USER/tools/infoga && cd /home/$USER/tools/infoga && python3 setup.py install
sudo ln -sf /home/$USER/tools/infoga/infoga.py /usr/local/bin/infoga
git clone https://github.com/soxoj/maigret /home/$USER/tools/maigret
pip3 install -r /home/$USER/tools/maigret/requirements.txt
sudo ln -sf /home/$USER/tools/maigret/maigret.py /usr/local/bin/maigret
git clone https://github.com/m0rtem/CloudFail /home/$USER/tools/CloudFail
pip3 install -r /home/$USER/tools/CloudFail/requirements.txt
sudo ln -sf /home/$USER/tools/CloudFail/cloudfail.py /usr/local/bin/cloudfail
echo '[+] Installing Project Discovery tools...'
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
echo '[+] Installing our favorite FUZZING tool ffuf'
go install github.com/ffuf/ffuf/v2@latest
echo '[+] Making links to Go Tools...'
sudo ln -sf /home/$USER/go/bin/subfinder /usr/local/bin/subfinder
sudo ln -sf /home/$USER/go/bin/httpx /usr/local/bin/httpx
sudo ln -sf /home/$USER/go/bin/nuclei /usr/local/bin/nuclei
sudo ln -sf /home/$USER/go/bin/ffuf /usr/local/bin/ffuf
