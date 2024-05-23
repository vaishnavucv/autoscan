# Importing the nmap module to use its port scanning functionality
import nmap

# Function to scan ports on the given host
def scan_ports(host):
    # Create an instance of the PortScanner class
    nm = nmap.PortScanner()
    
    # Scan the host for open ports and service versions
    # '-sV' flag is used to detect service/version info
    nm.scan(host, arguments='-sV')
    
    # Iterate over the scanned hosts (should be just one)
    for host in nm.all_hosts():
        print(f'Scan results for: {host}')
        
        # Iterate over the open ports
        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            
            # Get the list of open ports for the protocol
            lport = nm[host][proto].keys()
            
            # Sort the ports
            for port in sorted(lport):
                # Print port number, state, name, and version of the service
                print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}\t'
                      f'Service: {nm[host][proto][port]["name"]}\t'
                      f'Version: {nm[host][proto][port]["version"]}')

# Main function to get user input and call the scan function
if __name__ == '__main__':
    # Prompt the user to enter an IP, host, or domain to scan
    target = input('Enter the IP/host/domain to scan: ')
    
    # Call the scan_ports function with the user input
    scan_ports(target)
