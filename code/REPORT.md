# CENG 435 -  Phase 1 Report

## Group 88

---

### Group Members<br>

----
 - Doğancem Duran - 2521508
 - Kerem Yılmaz - 2522191

### Github

---
[Project Repository](https://github.com/KeremHmd/covertovert)

### Procedure

---
- Receiver script is initially run with an optional argument for the count of packets to be listened for. No argument ensures a newer ending listening task, while other options cause the receiver to end its task after the decided amount of packets are received.
- While a Receiver instance is running, running a Sender instance sends a packet with TTL = 1 to the desired destination, after which it receives a confirming message and ends.
- Upon a packet being sent, Receiver receives and shows the contents of the received packet, and then continues listening until the quota is filled(if it even exists).
  
