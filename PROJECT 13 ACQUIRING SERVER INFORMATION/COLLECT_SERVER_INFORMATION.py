import wmi

c = wmi.WMI()
for os in c.Win32_OperatingSystem():
	print("OS NAME: {}".format(os.caption))
	print("OS VERSION: {}".format(os.version))
	print(f"OS ARCHITECTURE: {os.OSArchitecture}")
	print(f"{os._username_}")