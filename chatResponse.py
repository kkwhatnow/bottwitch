from clients import *

def checkwhowrote():
	r = recveive()
	#Gets User
	one = r.find(':')
	two = r.find('!')
	three = (one + 1)
	four = (two)
	five = r[three:four]
	#Gets Message
	six = r.rfind(":")
	seven = (six + 1)
	eight = r[seven:]
	if five != (''):
		print("USER: " + five + "\n" +"MESSAGE: " + eight + "\n")
		return five,eight
	#else:
	#	None
		
		

