# discover subdomain
import requests
"""
class crawler:
	def __init__(self,target):
		self.Target = target

	def request(self,subdomain):
		try:
			return requests.get("http://"+subdomain)		
		except requests.exceptions.ConnectionError:
			pass 	

	def discover_subdomain(self):
		subdomain = ""
		with open("subdomain.txt",'r') as F:
			for line in F :
				subdomain = line.strip() +"."+self.Target
				result = self.request(subdomain)
				if result:
					print(subdomain)


Crawler = crawler("google.com")
Crawler.discover_subdomain()
"""