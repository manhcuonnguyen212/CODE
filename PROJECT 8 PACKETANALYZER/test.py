from scapy.all import *

def process_packets(packet):
	print(packet.show())
sniff(prn = process_packets,filter='ip')