# MS17-010 Vulnerability Scanner

This script utilizes `nmap` to scan for the MS17-010 vulnerability, specifically targeting Microsoft SMBv1 servers. It is designed to be simple to use, requiring the user to input an IP address and a file name for the scan report. The script will then perform the scan silently, outputting the results to the specified file and informing the user if the targeted system is vulnerable.

## Requirements

- `nmap` must be installed on your system.
- You must have permission to scan the target network or IP address. Unauthorized scanning is illegal and unethical.

## Usage

1. Ensure `nmap` is installed on your system.
2. Run the script from your terminal.
3. wget the script [https://raw.githubusercontent.com/vaishnavucv/autoscan/main/MS17-010%20EternalBlue/ms17-010-scanner.sh](https://raw.githubusercontent.com/vaishnavucv/autoscan/main/MS17-010%20EternalBlue/ms17-010-scanner.sh)
4. Run `./ms17-010-scanner.sh`
5. When prompted, enter the IP address you wish to scan.
6. Next, enter a file name for the scan report. This file will be created in the directory from which you run the script.
7. The script will perform the scan silently and inform you whether the IP address is vulnerable to MS17-010. It will also advise you to open the generated report with Mousepad or your preferred text editor.

## Main Code

```bash
#!/bin/bash

# Ask for the IP address and scan file name
read -p "Enter the IP address to scan: " scan_ip
read -p "Enter the scan report file name: " scan_name

# Perform the scan without showing output in the terminal
echo "Scanning $scan_ip for vulnerabilities on port 445, please wait..."
nmap --script smb-vuln-ms17-010 -p445 $scan_ip -vv -oN $scan_name > /dev/null 2>&1

# Check if the output file contains the vulnerability details
if grep -q "VULNERABLE:" $scan_name; then
  echo "The IP $scan_ip is VULNERABLE to MS17-010."
  echo "Details found in the report:"
  grep "VULNERABLE:" $scan_name -A 10 # Display the vulnerability details from the report
else
  echo "The IP $scan_ip does NOT appear to be vulnerable to MS17-010."
fi

# Instruct the user to open the report with Mousepad or their preferred text editor
echo "Please open the scan report named '$scan_name' with Mousepad or your preferred text editor to view the details."
```

Note: Replace the placeholders and instructions as necessary to fit the specifics of your setup or environment.
Disclaimer

- ⚠️ This tool is provided for educational purposes only. Always ensure you have explicit permission to scan the network or system. Unauthorized scanning and exploitation of vulnerabilities without permission is illegal and unethical.
