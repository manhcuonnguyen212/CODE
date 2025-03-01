import psutil
import sys,pprint
# Create main process list 
def Create_process_list():
	proc = []
	for p in psutil.process_iter():
		print(str(p)+"->>>"+str(p.parents()))

Create_process_list()