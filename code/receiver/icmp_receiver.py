import scapy

# Implement your ICMP receiver here
from scapy.all import sniff

def packet_handler(pkt):
    print(pkt.show())


print("Receiving packages:")
a = sniff(filter="icmp and host 172.18.0.2 and ip[8] == 1", prn=packet_handler)