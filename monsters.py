''' A Right Monstrous File
...maybe change all monsters to things who can attack with live feeds?
Get web scraping / this txtadv nailed first though.
'''

import random

# A Base Class for Monsters

class Monster(object):
	"""Monster"""
	def __init__(self,hp,dmg):
		self.name = name
		self.hp = hp
		self.dmg = dmg

	def is_alive(self):
		return self.hp > 0

# Classes for Monsters

class Rat(Monster):
	def __init__(self):
		super().__init__(name="Rat",hp=3,dmg=2)

class Cat(Monster):
        def __init__(self):
                super().__init__(name="Cat",hp=10,dmg=5)

class giant_kitten(Monster):
        def __init__(self):
                super().__init__(name="Giant Kitten",hp=50,dmg=5)

class Dog(Monster):
        def __init__(self):
                super().__init__(name="Dog",hp=15,dmg=5)

class Bear(Monster):
        def __init__(self):
                super().__init__(name="Bear",hp=30,dmg=10)




# List of Monsters

#Rat = Monster("Rat","1")
#Cat = Monster("Cat","2")
#Dog = Monster("Dog","3")
#Bear = Monster("Bear","4")
#monster_list = [Rat,Cat,Dog,Bear]


# Function to routinely make monsters appear (0.25chance)

#def make_monster():
	# odds of monster are 1 in 4
#	monster_in = random.randrange(4)
#	if monster_in < 3:
#		return 0
#	monster = monster_list[random.randrange(4)-1]
#	return monster


# add monster health, attacks?, escape chance?, nicknamethistime(random) 
