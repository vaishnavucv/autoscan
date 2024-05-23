# Simple Port Scanner

This repository contains a simple and easy-to-use Python script for port scanning. The script uses the `nmap` module to scan a given IP address, host, or domain for open ports and lists the details of each open port, including the service name and version.

## Prerequisites
Before running the script, ensure you have Python installed on your system. Additionally, you need to install the `nmap` module and have the Nmap tool installed.
## Setup

1. Clone the repository:
    ```bash
    wget https://raw.githubusercontent.com/vaishnavucv/autoscan/main/python-nmap-v1/port-scan.py
    chmod +x port-scan.py
    ```
2. Install dependencies: You can install the `nmap` module using pip:
    ```bash
    pip install python-nmap
    ```
3. Run the application:
    ```bash
    python port-scan.py
    ```
4. Example Output:
   ```bash
   Enter the IP/host/domain to scan: example.com
   Scan results for: 93.184.216.34
   Protocol: tcp
   Port: 80	State: open	Service: http	Version: Apache httpd
   Port: 443	State: open	Service: https	Version: OpenSSL
   ```

### Explanation of the Python Script

1. **Importing the nmap module:** This allows us to use Nmap's functionality within our Python script.
   
   ```python
   import nmap
   ```
2. Defining the scan_ports function: This function takes a host (IP, domain, or hostname) as input and performs the port scan.
   ```python
   def scan_ports(host):
   ```
3. Creating an instance of the PortScanner class: This instance will be used to perform the scan.
  ```python
  nm = nmap.PortScanner()
  ```
4. Scanning the host: We use the scan method with the -sV argument to detect service/version information.
  ```python
  nm.scan(host, arguments='-sV')
  ```
5. Iterating over scanned hosts and open ports: The script prints the details of each open port, including the port number, state, service name, and version.
  ```python
  for host in nm.all_hosts():
    print(f'Scan results for: {host}')
    for proto in nm[host].all_protocols():
        print(f'Protocol: {proto}')
        lport = nm[host][proto].keys()
        for port in sorted(lport):
            print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}\t'
                  f'Service: {nm[host][proto][port]["name"]}\t'
                  f'Version: {nm[host][proto][port]["version"]}')
   ```
 6. Main function to get user input: The script prompts the user for the target host and calls the scan_ports function.
  ```python
    if __name__ == '__main__':
    target = input('Enter the IP/host/domain to scan: ')
    scan_ports(target)
  ```
#### This script provides a simple way to scan ports and gather service information using Python and Nmap. The README file explains how to set up and use the script, making it easy for others to understand and use.
