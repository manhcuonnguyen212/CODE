import sys
from scapy.all import *


class analyzer:
	def __init__(self):
		self.count = 1
		print("Program is runnings")
	def ethernetAnalysis(self,packet):
		print("----------------------ETHERNET HEADER-------------------")
		print("MAC src: {} MAC dst: {} Protocol: {}".format(packet["Ethernet"].src,packet["Ethernet"].dst,hex(packet["Ethernet"].type)))
	def ArpAnalysis(self,packet):
		print("\n---------ARP HEADER--------------")
		print("IPs src: {} IP dst: {}  Op: {}".format(packet.psrc,packet.pdst,packet.op))
	def IPAnalysis(self,packet):
		print("\n-------IP HEADER------")
		print("IP src: {}  IP dst: {}  Protocol: {} Flag: {} ".format(packet.src,packet.dst,hex(packet.proto),packet.flags))
	def IPv6Analysis(self,packet):
		print("\n-----IPv6 HEADER------")
		print("IP src: {} IP dst: {} NextHeader: {}".format(packet.src,packet.dst,packet.nh))
	def process_capturedPackets(self,packet):
		print("Packet: {}".format(self.count))
		self.count += 1
		self.ethernetAnalysis(packet["Ethernet"])
		if(packet["Ethernet"].type == 2054):
			self.ArpAnalysis(packet["ARP"])
		if(packet["Ethernet"].type == 2048):
			self.IPAnalysis(packet["IP"])
		if(packet["Ethernet"].type == 34525):
			self.IPv6Analysis(packet["IPv6"])		
	def start_analyzing(self):
		sniff(prn=self.process_capturedPackets)
def main_function():
	try:
		test = analyzer()
		test.start_analyzing()
	except KeyboardInterrupt as e :
		pass

main_function()