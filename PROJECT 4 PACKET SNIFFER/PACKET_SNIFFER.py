from scapy.all import *
import argparse	

class sniffer:
	def __init__(self):
		print("Program has started!")
	def processing_packets(self,packet):
		keywords_list = ["username","user","login","password","pass"]
		if packet.haslayer("Raw"):
			http_payload = packet["Raw"].load
			if b"GET" in http_payload or b"POST" in http_payload:
				print(packet["Raw"].load)
	def sniffing_packet(self):
		sniff(prn=self.processing_packets)

try:
	test = sniffer()
	test.sniffing_packet()
except Exception as e:
	print("Quit program dute to "+str(e))