# import the required libraries
import psutil
import sys,pprint
# Create main process list 
def Create_process_list():
	proc = []
	for p in psutil.process_iter():
		try:
			p.cpu_percent()
			proc.append(p)
		except  Exception as e: 
			pass 
	return proc 
## iterates through all of the processess and places them into a large dict variable 
def process_iterator(kids_iterator,key_iterator):
	for kids in kids_iterator.children():
		if len(kids.children()) == 0: 
			key_iterator[kids.pid] = [kids,len(kids.children())]
		else: 
			key_iterator[kids.pid] = [kids,len(kids.children()),{}]
			process_iterator(key_iterator[kids.pid][0],key_iterator[kids.pid][2])
def generate_process_dict(proc):
	processes = {}
	for p in proc: 
		if p.pid !=0: # skips the processes with the 0 of PID value 
			if psutil.pid_exists(p.pid): # prevents errors if a process closes beteen list creation and running this function
				if len(p.parents()) == 0: # p.parents() -> return list of parent of a process
					# filter processes except those with no reported parents
					if len(p.children()) == 0: # p.children() -> return list of children of a process
						#skip additional walks because there no children
						processes[p.pid] = [p,len(p.children())]
					else: 
						processes[p.pid] = [p,len(p.children()),{}]
						
						kids_iterator = p #parent process to investigate
						key_iterator = processes[p.pid][2] #reference to nested idc inside process dict

						process_iterator(kids_iterator,key_iterator)
	return processes

def main():
	# pprint.pprint(Create_process_list())
	# sys.exit()

	# Create a nested dict of all the current process (called process)
	try: 
		this_dict = generate_process_dict(Create_process_list())
	except Exception as e: 
		print(e)
		sys.exit()
	pprint.pprint(this_dict)
if __name__ == "__main__":
	main()