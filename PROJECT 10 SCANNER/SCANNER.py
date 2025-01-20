from scapy.all import *
class scanner:
	def __init__(self,target):
		self.ip = target
	def get_ip(self):
		return self.ip
class host_scanner(scanner):
		def __init__(self,target_ip):
			print("the program has run!")
			super().__init__(target_ip)
		def creating_ICMP_Packet(self):
			ether_header = Ether(dst="98:3b:8f:10:dd:0d")
			ip_header = IP(src="192.168.1.14",dst=super().get_ip())
			icmp_header = ICMP()
			icmp_packet = ether_header/ip_header/icmp_header
			print(icmp_header.summary())
			#answered_list,unrespone_list = sr(icmp_header)
			#return answered_list
		def analyzing(self):
			answered = self.creating_ICMP_Packet()
			for x in answered:
				if x[1].type==0:
					print("{} is up ".format(super().get_ip()))
		def run(self):
			try:
				self.analyzing()
			except KeyboardInterrupt:
				print("the program stopped!")
Scan = host_scanner("8.8.8.8")
Scan.run()	