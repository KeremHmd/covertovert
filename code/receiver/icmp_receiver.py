import scapy

# Implement your ICMP receiver here
from scapy.all import sniff

def packet_handler(pkt):
    """
    Show the packet features, it will be printed on stdout.\n
    This function will be called by scapy sniff function.
    
    """
    pkt.show()

def listen(p_count:int = None):
    """
    Takes only p_count as an optional argument.\n
    If p_count is not given, listen until program is exited, else listen p_count times.\n
    sniff function filters packet by being icmp and their host being 172.18.0.2 and their TTL being 1.
    """
    if p_count == None:
        a = sniff(filter="icmp and host 172.18.0.2 and ip[8] == 1", prn=packet_handler)
    else:
        a = sniff(filter="icmp and host 172.18.0.2 and ip[8] == 1", prn=packet_handler, count = p_count)

if __name__ == "__main__":
    listen(1)