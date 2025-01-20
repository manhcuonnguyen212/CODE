from scapy.all import *

def Full_Duplex_Sessions(p):
	sess = "Other"
	if p.haslayer('Ether'):
		if p.haslayer('IP'):
			if p.haslayer("TCP"):
				sess = str(sorted(["TCP",p["IP"].src,p["TCP"].sport,p["IP"].dst,p["TCP"].dport],key=str))
			elif p.haslayer("UDP"):
				sess = str(sorted(["UDP",p["IP"].src,p["UDP"].sport,p["IP"].dst,p["UDP"].dport],key=str))
			elif p.haslayer("ICMP"):
				sess = str(sorted(["ICMP",p["IP"].src,p["IP"].dst,p["ICMP"].code,p["ICMP"].type,p["ICMP"].id],key=str))
			else:
				sess = str(sorted(["IP",p["IP"].src,p["IP"].dst,p["IP"].proto],key=str))
		elif p.haslayer('ARP'):
			ess = str(sorted(["ARP",p["ARP"].psrc,p["ARP"].pdst],key=str))
	else:
		sess = p.sprintf("Ether type=%Ether.type%")
	return sess
def FTPSessionFilter(TCPSessions):
	Key = TCPSessions.keys()
	Value = TCPSessions.values()
	FTPSession = {}
	for (K,V) in zip(Key,Value):
		for x in V:
			if x.haslayer("TCP") and (x.sport == 21 or x.dport == 21):
				FTPSession[K] = V
	return FTPSession

def TCPSessionFilter(Sessions):
	Key = Sessions.keys()
	Value = Sessions.values()
	TCPSessions = {}
	for K,V in zip(Key,Value):
		newKey = K.replace("[","").replace("]","").replace("'","").replace(", ","-").split("-")
		if len(newKey) == 5:
			if newKey[4] == "TCP":
				TCPSessions[K] = V
	return TCPSessions


def FTPBruteAnalysis(FTPSessions,PrintLoginsToConsole=False,PrintSummaryToConsole=False,SaveToFile=False,TrackAttack=False):
	Keys = FTPSessions.keys()
	Values = FTPSessions.values()

	User = b""
	PasssWord = b""
	FTPSuccess = 0 
	FTPFailure = 0
	FTPFailurePackets = {}

	if TrackAttack:
		FTPAttacks = {}

	for K,V in zip(Keys,Values):
		for x in V:
			if x.haslayer("Raw"):
				if b"USER" in x["Raw"].load:
					User = x["Raw"].load.split()[1]
				elif b"PASS" in x["Raw"].load:
					PasssWord = x["Raw"].load.split()[1]
				elif b"230 Login successful" in x["Raw"].load:
					print("Found Login Success in Session: ")
					print("\t"+"Client: "+x["IP"].dst+"\t"+"Server: "+x["IP"].src)
					print("\t"+"User: "+User+"\t"+"Password: "+PasssWord)
					User=""
					PasssWord=""
				elif b"530" in x["Raw"].load:
					print("Under Attack: {}->{}".format(x["IP"].src,x["IP"].dst))
					print("\t"+"User: "+str(User)+"\t"+"Password: "+str(PasssWord))
					User = b""
					PasssWord = b""
def main_function():
	# read information about packets from offline
	Captured_packets = sniff(offline='bruteforce.pcap')
	# full duplex connection 
	FullDuplexSessions = {}
	for x in Captured_packets:
		sessionID = Full_Duplex_Sessions(x)
		if sessionID not in FullDuplexSessions:
			FullDuplexSessions[sessionID] = list()
		FullDuplexSessions[sessionID].append(x)
	#Filtering TCP Connections
	TCPSessions = TCPSessionFilter(FullDuplexSessions)

	#Filtering FTP Conections

	FTPSessions = FTPSessionFilter(TCPSessions)
	if len(FTPSessions) !=0 :
		PrintSummaryToConsole = False #Print out the summary of analysis
		PrintLoginsToConsole = False #Print out the logins found
		TrackAttack = False #Save failure sources and destination and print individual summary
		SaveToFile = False # save filelists containning failures 
		FTPBruteAnalysis(FTPSessions,PrintLoginsToConsole,PrintSummaryToConsole,SaveToFile,TrackAttack)
	else:
		print("Don't exist FTP connection")
main_function()

""" the process of FTP brute force analysis: 
			open file contains captured packets.
			seperating sessions that packets belong to.
			filtering TCP sessions.
			filtering FTP sessions
			"""