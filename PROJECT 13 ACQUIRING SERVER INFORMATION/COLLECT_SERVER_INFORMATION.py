# Platform module is used to gather system infor
# import platform
# print("OS: "+platform.system())
# print("Release: "+platform.release())
# print("Version: "+platform.version())
# print("HostName: "+platform.node())
# print("Processor: " +platform.processor())
# print("Platform: "+ platform.platform())

#psutil module allows to restrieve types of components of system runing.
import psutil
# print("Total of CPUs: {}".format(psutil.cpu_count(True)))
# print("The percent of cpu usage: {}".format(psutil.cpu_percent(percpu=True)))
# #print("Memo infor: {}".format(psutil.memory_info()))
# print(f"Disk infor: {psutil.disk_partitions(all=True)}")
# print(f"Network interface: {psutil.net_if_addrs()}")
# connections = psutil.net_connections()
# for x in connections:
# 	if(x.status == "ESTABLISHED"):
# 		print(psutil.Process(x.pid))
# print(f"Process infor: {psutil.pids()}")
# print(f"Battery infor: {psutil.sensors_battery()}")
# print(f"Boot time: {psutil.boot_time()/3600}")
# import winapps
# for app in winapps.list_installed():
# 	if "winhttrack" in app.name.lower():
# 	 	app.uninstall()
# 	 	print("deleted")
# for app in winapps.list_installed():
# 	print(str(app.name) +"->"+ str(app.version))
import wmi
ip = "192.168.1.5"
username = r"manhCuongNguyen"
password = "1"
try:
	connection = wmi.WMI(ip,user=username,password=password)
	print("Connection established!")
except Exception as e:
	print("fail in trying connection with an error: "+ str(e))	