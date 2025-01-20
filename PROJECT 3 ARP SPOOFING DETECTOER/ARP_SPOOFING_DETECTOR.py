from scapy.all import *

class detector:
	def __init__(self):
		print("Program has started!")
	def get_mac(self,ip):
		arp = ARP(pdst=ip)
		ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")
		arp_request = ethernet/arp 
		answered_list,unrespone_list = srp(arp_request,timeout=2,verbose=True)
		for x in answered_list:
			return x[1].hwsrc
	def sniff(self):
		sniff(prn=self.process_sniffed_packets)
	def process_sniffed_packets(self,packet):
		if packet.haslayer(ARP) and packet[ARP].op == 2:
			mac = packet[ARP].hwsrc
			real_mac = self.get_mac(packet[ARP].psrc)
			if mac != real_mac:
				print("[-]You are under ATTACK")

detector = detector()
detector.sniff()