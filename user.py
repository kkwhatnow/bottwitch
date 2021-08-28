import csv
from fileBuilder import *

	
#adds whoever speaks to a file
def getsuser(five,eight):
	stopsgetsuser = True
	stopsredundentcy = ['kkwhatnow']
	while stopsgetsuser == True:
	
#checks if user is in file; if not then they are added
		
		for x in stopsredundentcy:
			print(x)
			print('this si x')
			if five == x:
				print('stop then x')
				stopsgetsuser = False
				break
				
			elif stopsredundentcy == None:
				break
				
		stopsredundentcy.append(five)
		
		with open('userFile.txt', mode='r',newline="") as readuser:
			finduser = csv.DictReader(readuser)
			for row in finduser:
				"""row['user'] == five
				or row['user'] == None
				or row['user'] == ''
				or five == ''
				or row == '\n'"""
				if row['user'] == five:
					break
				elif row['user'] != five and (row != None or row != ''):
					continue
				elif row == '':
					with open('userFile.txt', mode='a', newline="") as appenduser:
						print('inside of append')
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

		print('i ended')
		stopsgetsuser = False
		

def updateuser(putuserinlist2):
	print('this is uptdate user')
    # finds user in file to update them after quest
    
    # puts those being updated into a quest
    
	with open('userFile.txt', mode='r', newline="") as readuser:
		finduser = csv.DictReader(readuser)
        #print('dkk')
		
def playersequipment(five):
	with open('userFile.txt', mode='r', newline="") as readuser:
		finduser = csv.DictReader(readuser)
		for row in finduser:
			if row['user'] == five:
				print(row)
				user = row['user'],
				gold = row['gold'],
				health = row['health'],
				defense = row['defense'],
				speed = row['speed'],
				intelligence = row['intelligence'],
				agility = row['agility'],
				luck = row['luck'],
				strength = row['strength'],
				observation = row['observation'],
				weapon = row['weapon'],
				accessory = row['accessory'],
				head = row['head'],
				chest = row['chest'],
				gloves = row['gloves'],
				pants = row['pants'],
				shoes = row['shoes'],
				shield = row['shield'],
				ring1 = row['ring1'],
				ring2 = row['ring2'],
				ring3 = row['ring3'],
				ring4 = row['ring4'],
				ring5 = row['ring5'],
				ring6 = row['ring6'],
				ring7 = row['ring7'],
				ring8 = row['ring8'],
				ring9 = row['ring9'],
				ring10 = row['ring10']

			
				stats = '''<table>\n
							<tr>\n
							<th>user</th>\n
							<th>gold</th>\n
							<th>health</th>\n
							<th>defense</th>\n
							<th>speed</th>\n
							<th>intelligence</th>\n
							<th>agility</th>\n
							<th>luck</th>\n
							<th>strength</th>\n
							<th>observation</th>\n
							<th>weapon</th>\n
							<th>accessory</th>\n
							<th>head</th>\n
							<th>chest</th>\n
							<th>gloves</th>\n
							<th>pants</th>\n
							<th>shoes</th>\n
							<th>shield</th>\n
							<th>ring1</th>\n
							<th>ring2</th>\n
							<th>ring3</th>\n
							<th>ring4</th>\n
							<th>ring5</th>\n
							<th>ring6</th>\n
							<th>ring7</th>\n
							<th>ring8</th>\n
							<th>ring9</th>\n
							<th>ring10</th>\n
							</tr>\n
							<tr>\n
							<td>''', user, '''</td>\n
							<td>''', gold, '''</td>\n
							<td>''', health, '''</td>\n
							<td>''', defense, '''</td>\n
							<td>''', speed, '''</td>\n
							<td>''', intelligence, '''</td>\n
							<td>''', agility, '''</td>\n
							<td>''', luck, '''</td>\n
							<td>''', strength, '''</td>\n
							<td>''', observation, '''</td>\n
							<td>''', weapon, '''</td>\n
							<td>''', accessory, '''</td>\n
							<td>''', head, '''</td>\n
							<td>''', chest, '''</td>\n
							<td>''', gloves, '''</td>\n
							<td>''', pants, '''</td>\n
							<td>''', shoes, '''</td>\n
							<td>''', shield, '''</td>\n
							<td>''', ring1, '''</td>\n
							<td>''', ring2, '''</td>\n
							<td>''', ring3, '''</td>\n
							<td>''', ring4, '''</td>\n
							<td>''', ring5, '''</td>\n
							<td>''', ring6, '''</td>\n
							<td>''', ring7, '''</td>\n
							<td>''', ring8, '''</td>\n
							<td>''', ring9, '''</td>\n
							<td>''', ring10, '''</td>\n
						  </tr>\n
						</table>\n'''
				stats = stats.strip()
				print(stats)
				user = user[0]
				try:
					with open(user + '.html',mode='x', newline = "") as createuser:
						pass
				except:
					pass			
	with open(user + '.html', mode='w', newline = "") as createuser:
		createuser.write('''<!DOCTYPE html>\n
				<html>\n
				<title>\n''')
		createuser.write(user)
		createuser.write('\n')
		createuser.write('''</title>\n
				<head>\n
				<link rel="stylesheet" href="user.css">\n
				</head>\n
				<body>\n
				<h1>\n''')
		createuser.write(user)
		createuser.write('\n')
		createuser.write(''' Stats</h1>
				<div class = 'user'>\n
				''')
		createuser.write(stats)
		createuser.write('\n')
		createuser.write('''
				</div>\n

				<div class = 'inventory'>\n
				</div>\n

				</body>\n
				</html>\n
				''')
				
		
		
        
		




