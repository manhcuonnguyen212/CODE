import requests
import argparse
class crawler:
	def __init__(self,Target):
		self.target = Target
		print("Program is running")
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

class directoryDiscover(crawler):
	def __init__(self,Target):
		super().__init__(Target)
		print("Programe has started!.")
	def directory_Discover(self):
		try:
			with open("folder_file.txt",'r') as F:
				for line in F:
					path = self.target + "/" + line.strip()
					if super().request(path) :
						print(path)
		except Exception as e:
			print(e)


try:
	parser = argparse.ArgumentParser(description='Crawler Tool')
	parser.add_argument('domain',type=str,help='the domain of the target that you want to discover!')
	parse = parser.parse_args()
	test = directoryDiscover(parse.domain)
	test.directory_Discover()
except Exception as e:
	print(e)

