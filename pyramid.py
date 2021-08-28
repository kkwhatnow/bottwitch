from clients import *
import time
def jkdfjk():
	jfij = 1
	x = 1
	kk = 0
	#must have a space at the end of the emote
	emote = "jervalInChamp "
	LUL = emote
	LULO = emote
	colon = " :"
	tall = 49
	rtall = 50
	while kk != -1:
		if x == tall or jfij == 0 and x != 0:
			jfij = 0
			LUL *= x
			colon += LUL
			client.send((f"PRIVMSG " + CHANNEL_NAME + colon + "\n").encode(FORMAT))
			time.sleep(0.1)
			colon = " :"
			LUL = LULO
			x -= 1
			continue
		elif x == 0:
			kk = -1
			continue
		elif x != rtall:
			LUL *= x
			colon += LUL
			client.send((f"PRIVMSG " + CHANNEL_NAME + colon + "\n").encode(FORMAT))
			time.sleep(0.1)
			colon = " :"
			LUL = LULO
			x += 1
			continue
		else:
			continue
		
