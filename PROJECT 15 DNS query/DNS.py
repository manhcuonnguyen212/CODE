import dns.resolver 
try: 
	answers = dns.resolver.resolve('ptithcm.edu.vn','MX')
	print(answers.response)
	print("_______________")
	print(answers.rrset)
	print(answers.rret[0:3]) #only returns three entries
except Exception as e:
	print(e)
print("_______________")
try:
	answers2 = dns.resolver.resolve_address('115.165.166.67') # For PTR record
	print(answers2.response)
except Exception as e:
	print(e)