import scapy

# Implement your ICMP sender here


from scapy.all import sr1,IP,ICMP


def send_packet(ttl,dst):
    """
    Create a packet and send to dst with the given ttl value
    
    
    
    """
    my_packet = IP(ttl=ttl, dst=dst)/ICMP() 
    sr1(my_packet)

if __name__ == "__main__":
    send_packet(ttl=1, dst="172.18.0.3")