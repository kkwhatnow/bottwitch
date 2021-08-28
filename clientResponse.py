from chatResponse import checkwhowrote
from clients import *
import time
import threading
from quests import quests, flurby
from user import getsuser, playersequipment


def respondtoclinet():
	
	turnonthefunction = 1
	
	while turnonthefunction == 1:
		five, eight = checkwhowrote()
		print(five)
		print('this is from client')
		getsuser(five,eight)
		
		if eight == None:
			turnonthefunction = 0
			
		elif eight == ('PING :tmi.twitch.tv'):
			client.send((f"PONG :tmi.twitch.tv\n").encode(FORMAT))
			turnonthefunction = 0
			 
		elif eight.startswith('!') == False:
				turnonthefunction = 0
				
		elif eight == ('!quests'):
			#onoff = True
			client.send((f"PRIVMSG " + CHANNEL_NAME + " :Starting Quest" + "\n").encode(FORMAT))
			quests()
			#t = threading.Thread(target = quests)
			#t.start()
			turnonthefunction = 0
		elif eight == ('!equipment'):
			playersequipment(five)
			turnonthefunction = 0
			
			
		else:
			turnonthefunction = 0
		turnonthefunction = 0
		

		
