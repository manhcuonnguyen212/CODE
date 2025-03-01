import time,psutil,os,sys
from prettytable import PrettyTable 

def Create_process_list():
	proc = []
	for p in psutil.process_iter():
		try:
			p.cpu_percent()
			proc.append(p)
		except  Exception as e: 
			pass 
	return proc 
def main():
	try: 
		while True:
			processs_cpu_table = PrettyTable(['PID','PNAME','STATUS','CPU','NUM THREADS','MEMORY(MB)'])
			topCPU = {}
			topMEM = {}
			time.sleep(0.5)
			for p in Create_process_list():
				if p.pid !=0:
					topCPU[p] = p.cpu_percent() / psutil.cpu_count()
					topMEM[p] = p.memory_info().rss 
			top_cpu_list = sorted(topCPU.items(),key=lambda x: x[1],reverse = True)
			top_mem_list = sorted(topMEM.items(),key=lambda x: x[1],reverse = True)
			top10cpu = top_cpu_list[:10]
			top10mem = top_mem_list[:10]
			for p,cpu_percent in top10cpu:
				try: 
					with p.oneshot(): #p.oneshot() context manager in psutil is used to optimize multiple calls to the same process by reducing system calls
						processs_cpu_table.add_row([str(p.pid),p.name(),p.status(),f'{cpu_percent:.2f}'+"%",p.num_threads(),f'{p.memory_info().rss/1e6:.3f}'])
				except Exception as e: 
					pass
			process_mem_table = PrettyTable(['PID','PNAME','STATUS','CPU','NUM THREADS','MEMORY(MB)'])
			for p,mem in top10mem:
				try: 
					with p.oneshot():
						process_mem_table.add_row([str(p.pid),p.name(),p.status(),f'{p.cpu_percent()/psutil.cpu_count():.2f}'+"%",p.num_threads(),f'{mem/1e6:.3f}'])
				except Exception as e: 
					pass
			os.system("cls")
			print(processs_cpu_table)
			print(process_mem_table)
			time.sleep(3)
	except KeyboardInterrupt:
		print("stopping")
		sys.exit(0)
	except Exception as e:
		print(e)
if __name__ == "__main__":
	main()