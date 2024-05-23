# Import necessary modules
from scapy.all import sr1, IP, ICMP, DNS, DNSQR

# Function to perform a basic network scan
def network_scan(target):
    # Sending an ICMP (ping) packet to the target
    icmp_packet = IP(dst=target)/ICMP()
    response = sr1(icmp_packet, timeout=2, verbose=False)

    # Check if there is a response
    if response:
        print(f"{target} is up.")
        print("Response details:")
        response.show()
    else:
        print(f"{target} is down or not responding.")

# Function to perform a DNS query
def dns_query(domain):
    # Sending a DNS query to the target domain
    dns_packet = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain))
    response = sr1(dns_packet, timeout=2, verbose=False)

    # Check if there is a response
    if response and response.haslayer(DNS):
        print(f"DNS query for {domain}:")
        response.show()
    else:
        print(f"No DNS response for {domain}.")

if __name__ == "__main__":
    # Ask the user for input
    target = input("Enter IP/host/domain: ")

    # Perform network scan
    network_scan(target)

    # If the input is a domain, perform a DNS query
    if '.' in target:
        dns_query(target)
