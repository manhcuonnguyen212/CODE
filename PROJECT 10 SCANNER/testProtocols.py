from scapy.all import *

def display_result(packet):
	print(packet.show())
try:
	sniff(filter="icmp",prn=display_result)
except KeyboardInterrupt:
	print("stop!")