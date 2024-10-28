#!/bin/bash
# MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption 
cat << 'EOF'
                                                    _ _____      ___  _  ___  
                                      _ __ ___  ___/ |___  |    / _ \/ |/ _ \ 
╔═╗┌┬┐┌─┐┬─┐┌┐┌┌─┐┬  ╔╗ ┬  ┬ ┬┌─┐    | '_ ` _ \/ __| |  / /____| | | | | | | |
║╣  │ ├┤ ├┬┘│││├─┤│  ╠╩╗│  │ │├┤     | | | | | \__ \ | / /_____| |_| | | |_| |
╚═╝ ┴ └─┘┴└─┘└┘┴ ┴┴─┘╚═╝┴─┘└─┘└─┘    |_| |_| |_|___/_|/_/       \___/|_|\___/ 
                                http://github.com/vaishnavu/
EOF

read -p "Enter the IP Address to scan: " scan_ip
echo ""
read -p "Enter the Scan Name: " scan_name

echo "Scanning $scan_ip for Vulberability on port 445..."
echo ""
nmap --script smb-vuln-ms17-010 -p445 $scan_ip -vv -oN $scan_name.txt > /dev/null 2>&1

if grep -q "VULNERABLE:" $scan_name.txt; then
    echo ""
    echo -e "The IP $scan_ip is \e[32m VULNERBALE \e[0m to \e[31mCVE-2017-0143 \e[0m (ms17-010)"
    echo ""
    cat $scan_name.txt | grep -A6 VULNERABLE:
    echo ""
else
    echo "The IP $scan_ip is not VULNERBALE to CVE-2017-0143 (ms17-010)"
fi

mousepad $scan_name.txt &
exit
