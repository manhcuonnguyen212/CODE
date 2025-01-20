from scapy.all import *

# Sniff packets
packets = sniff(count=10)

# Group packets by session
sessions_dict = packets.sessions()

# Display session information
for x in sessions_dict:
    print(type(x))
    break