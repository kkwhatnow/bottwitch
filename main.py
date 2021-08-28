from clients import *
from clientResponse import *
import time
from pyramid import *
from fileBuilder import *



#print("it works")

login()
makesquests()
makesrewards()
makesfile()
#jkdfjk()
def mainfile():
	while True:
		respondtoclinet()
mainfile()
"""threads = []

for _ in range(3):
	t = threading.Thread(target = getsuser)
	t.start()
	threads.append

for thread in threads:
	thread.join"""
