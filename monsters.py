''' A Right Monstrous File
...maybe change all monsters to things who can attack with live feeds?
Get web scraping / this txtadv nailed first though.
'''

import random

# Class for Monsters

class Monster(object):
	"""Monster"""
	def __init__(self,name,level):
		self.name = name
		self.level = level


# List of Monsters

Rat = Monster("Rat","1")
Cat = Monster("Cat","2")
Dog = Monster("Dog","3")
Bear = Monster("Bear","4")
monster_list = [Rat,Cat,Dog,Bear]


# Function to routinely make monsters appear (0.25chance)

def make_monster():
	# odds of monster are 1 in 4
	monster_in = random.randrange(4)
	if monster_in < 3:
		return 0
	monster = monster_list[random.randrange(4)-1]
	return monster


# add monster health, attacks?, escape chance?, nicknamethistime(random) 
