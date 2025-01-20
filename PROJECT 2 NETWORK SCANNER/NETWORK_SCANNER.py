from scapy.all import *
import sys
import time
import argparse
class network_scanner:
	def __init__(self,ip):
		print("Network scanner is started scannning!")
		self.IP = ip 
	def create_ARP_packet(self):
		arp_layer = ARP(op=1,pdst=self.IP)
		ether_layer = Ether(dst="ff:ff:ff:ff:ff:ff")
		return ether_layer/arp_layer
	def send_packet(self):
		packet = self.create_ARP_packet()
		answered_list,unrespone_list = srp(packet,verbose=True,timeout=2)
		return answered_list
	def display_result(self):
		packet_list = self.send_packet()
		information = []
		for packet in packet_list:
			information.append({"ip":packet[1].psrc,"mac":packet[1].hwsrc})
		print("IP\t\t\tMAC\n____________________________________________")
		for x in information:
			print(x["ip"]+"\t\t"+x["mac"])
		sys.exit("Scan completely")
try:
	argment = argparse.ArgumentParser(description="Network scanner tool")
	argment.add_argument("network",type=str,help="The network that you want to scan!")
	arg = argment.parse_args()
	scanner = network_scanner(arg.network)
	scanner.display_result()
except Exception:
	print("[-] Occuring error during implementing program")