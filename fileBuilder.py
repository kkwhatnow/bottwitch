import csv


def makesfile():
    #checks if file exists; if not then it creates it
	try:
		with open('userFile.txt', mode='x') as txt_file:
				fieldnames = [
					'user','gold','health','defense','speed','intelligence','agility','luck','strength',
					'observation','weapon','accessory','head','chest','gloves','pants','shoes','shield',
					'ring1','ring2','ring3','ring4','ring5','ring6','ring7','ring8','ring9','ring10'
				]
				writer = csv.DictWriter(txt_file, fieldnames=fieldnames)
				writer.writeheader()
	except:
			None
			
def makesquests():
    # checks if file exists; if not then it creates it
	try:
		with open('questFile.txt', mode='x') as txt_file:
			writer = csv.writer(txt_file)
	except:
			print("a file is already created")

def makesquestsrewards():
    # checks if file exists; if not then it creates it
	try:
		with open('questReward.txt', mode='x') as txt_file:
			fieldnames = ['questid','gold','rewardid','reward']
			writer = csv.DictWriter(txt_file, fieldnames=fieldnames)
			writer.writeheader()
	except:
			print("a file is already created")

def makesrewards():
    # checks if file exists; if not then it creates it
	try:
		with open('itemReward.txt', mode='x') as txt_file:
			fieldnames = ['rewardid','reward','type','cost','sideeffect']
			writer = csv.DictWriter(txt_file, fieldnames=fieldnames)
			writer.writeheader()
	except:
			print("a file is already created")
			
			
#This is for the users file
#And is used for the boss

user = str()

gold = int()

health = int()
defense = int()
speed = int()
intelligence = int()
agility = int()
luck = int()
strength = int()
observation = int()

weapon = str()

accessory = str()

head = str()
chest = str()
gloves = str()
pants = str()
shoes = str()

shield = str()

ring1 = str()
ring2 = str()
ring3 = str()
ring4 = str()
ring5 = str()
ring6 = str()
ring7 = str()
ring8 = str()
ring9 = str()
ring10 = str()



#What the boss can drop
bossdrops = []
desperationmove = str()


typeid = int()
#id is the primary key
#This is for the weapons and armor
#Starting with a 0 is a weapon
#With a 1 is armor
#With a 2 is a ring
#With a 3 is an accessory
#With a 4 is a shield
#With a 5 is a hybrid
#With a 6 is miscellaneous
#With a 7 is food
#With a 8 is unarmed

type = str()
#type is further specifies what it is ie the name 'armor'

itemid = int()
#id specifically for that item

name = str()
#name is the name of the item

attribute = str()
#attribute is what it adds onto like health or defense

#effect will be like +5% to health -5% to defense
effect = {

	'positive': None,
	'negative': None
}

#further descripes the effect
deseffect = str()

cost = int()


