import ipapi

ip = "8.8.8.8"  # Example IP (Google DNS)
data = ipapi.location(ip)

print(data)  # Dictionary with IP info