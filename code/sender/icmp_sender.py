import scapy

# Implement your ICMP sender here


from scapy.all import sr1,IP,ICMP


def send_packet():
    my_packet = IP(ttl=1, dst="172.18.0.3")/ICMP()
    sr1(my_packet)

if __name__ == "__main__":
    while True:
        cmd = input("Type send to send packet, exit to close the program: ")
        if cmd.lower() == "send":
            send_packet()
        elif cmd.lower() == "exit":
            break
        else:
            print("Invalid command")