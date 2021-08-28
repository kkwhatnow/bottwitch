import csv
import random
import time
import threading
from clients import *
from chatResponse import *
from user import *
from fileBuilder import *


#does quests
def quests():
	print('quests started')
#opens up the quest file and randomally chooses a quest
	with open('questFile.txt', mode='r',newline="") as readuser:
		finduser = csv.reader(readuser)
		noneemptyrow = True
		chosen_row = []
		while noneemptyrow == True:
			for row in finduser:
				if chosen_row != None:
					chosen_row = chosen_row.append(finduser)
				else:
					continue
				chosen_row = random.choice(list(finduser))
				noneemptyrow = False
		chosen_row = chosen_row[0]
	chosen_row = eval(chosen_row)
	print(chosen_row)
			
#puts the bosses stats into variables
	id = row[0]
	quest = row[1]
	description = row[2]
	health = row[3]
	itemid = row[4]
	gold = row[5]
	weapon = row[6]
	accessory = row[7]
	head = row[8]
	chest = row[9]
	gloves = row[10]
	pants = row[11]
	shoes = row[12]
	ring1 = row[13]
	ring2 = row[14]
	ring3 = row[15]
	ring4 = row[16]
	ring5 = row[17]
	ring6 = row[18]
	ring7 = row[19]
	ring8 = row[20]
	ring9 = row[21]
	ring10 = row[22]
	shield = row[23]
	defense = row[24]
	speed = row[25]
	intelligence = row[26]
	luck = row[27]
	strength = row[28]
	observation = row[29]

		
#is used to add people
	putuserinlist = []
	
	
#loops for the quest time and allows people to join
	questjoiner(putuserinlist)
	
	with open('userFile.txt', mode='r',newline="") as readuser:
			finduser = csv.DictReader(readuser)
			for x in putuserinlist:
				for row in finduser:
					if x == row['user']:
						
					
					
					
					
					
					
					
						with open('userFiletemp.txt', mode='a', newline="") as appenduser:
							fieldnames = [
								'user','gold','health','defense','speed','intelligence','agility','luck','strength',
								'observation','weapon','accessory','head','chest','gloves','pants','shoes','shield',
								'ring1','ring2','ring3','ring4','ring5','ring6','ring7','ring8','ring9','ring10'
					]
							writer = csv.DictWriter(appenduser, fieldnames=fieldnames)
							adduser = {
								'user': five, 'gold': 0, 'health': 100, 'defense': 1, 'speed': 1, 'intelligence': 1,
								'agility': 1, 'luck': 1, 'strength': 1, 'observation': 1, 'weapon': None, 'accessory': None, 'head': None,
								'chest': None, 'gloves': None, 'pants': None, 'shoes': None, 'shield': None, 'ring1': None, 'ring2': None, 'ring3': None, 'ring4': None,
								'ring5': None, 'ring6': None, 'ring7': None, 'ring8': None, 'ring9': None, 'ring10': None
					}
							writer.writerow(adduser)


#lets those who join the quest into a list
def questjoiner(putuserinlist):
	print('this is questjon')
	makethisthestarttime = time.time()
	makethistheendtime = (makethisthestarttime + 15)
	print(makethisthestarttime)
	print(makethistheendtime)
	while makethisthestarttime < makethistheendtime:
		five, eight = checkwhowrote()
		if eight != ('!join'):
			makethisthestarttime = time.time()
			print(makethisthestarttime)
			continue
			
		elif eight == ('!join'):
			if five in putuserinlist:
				continue
			else:
				putuserinlist.append(five)
				#print(putuserinlist)
				client.send((f"PRIVMSG " + CHANNEL_NAME + " :Joining Quest!" + "\n").encode(FORMAT))
				makethisthestarttime = time.time()
				print(makethisthestarttime)
			continue
		return putuserinlist
			
		
class makesplayer:
	def __init__(self, id, quest, description, health, itemid, gold, weapon, accessory,
	head, chest, gloves, pants, shoes, ring1, ring2, ring3, ring4, ring5, ring6, ring7, ring8,
	ring9, ring10, shield, defense, speed, intelligence, luck, strength, observation, containsplayers):

		self.id = id
		self.quest = quest
		self.description = description
		self.health = health
		self.itemid = itemid
		self.gold = gold
		self.weapon = weapon
		self.accessory
		self.head = head
		self.chest = chest
		self.gloves = gloves
		self.pants = pants
		self.shoes = shoes
		self.ring1 = ring1
		self.ring2 = ring2
		self.ring3 = ring3
		self.ring4 = ring4
		self.ring5 = ring5
		self.ring6 = ring6
		self.ring7 = ring7
		self.ring8 = ring8
		self.ring9 = ring9
		self.ring10 = ring10
		self.shield = shield
		self.defense = defense
		self.speed = speed
		self.intelligence = intelligence
		self.luck = luck
		self.strength = strength
		self.observation = observation
		self.containsplayers = containsplayers
	
	def createplayer(self):
		pass



    
	
	
def flurby():
        f = open('flurby.txt', "r")
        for x in f:
            print(x)
            num = int(x)
            num += 1
            f = open('flurby.txt', mode='w')
            f.write(str(num))
            f.close()
            return str(num)
			
def rewardchooser(id):
	with open('questReward.txt', mode='r', newline="") as readuser:
		finduser = csv.DictReader(readuser)
		for row in finduser:
			if row['id'] == id:
				rewards = row['rewards']
				chance = row['chance']
				cost = row['cost']
				attribute = row['attribute']
				effect = row['effect']
				chance = (chance/1)
				chance = random.randint(1,chance)
				print(chance)
				return id,rewards,chance,cost,attribute,effect,type


					#if chance == 1:
						

def equests1():
	id = 0
	quest = ("Duel")
	description = ("Fight the little kid down the street")
	health = 10
#itemid is what has a chance to drop
	itemid = [0,1,2]
	gold = 4
	#use the itemid
	weapon = 'fists'
	accessory = 'locket'
	head = None
	chest = 'striped shirt'
	pants = 'blue jeans'
	shoes = 'converse'
	gloves = None
	ring1 = None
	ring2 = None
	ring3 = None
	ring4 = None
	ring5 = None
	ring6 = None
	ring7 = None
	ring8 = None
	ring9 = None
	ring10 = None
	shield = None
	defense = 0
	speed = 5
	intelligence = 3
	agility = 4
	luck = 2
	strength = 1
	observation = 0
	
	return (id, quest, description, health, itemid, gold, weapon, accessory,
	head, chest, gloves, pants, shoes, ring1, ring2, ring3, ring4, ring5, ring6, ring7, ring8,
	ring9, ring10, shield, defense, speed, intelligence, luck, strength, observation)
