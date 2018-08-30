''' Items items juicy items

Pretty much quest items.
Should have interchangeable (monetary?) value...
So player finds them, completes quest, gets reward.
(Reward is cash and sometimes also other items!)
Cafe: sooty coffee powder, coffee beans, pinto beans, keepcup.
Bar: girls, bouncers, tourists, delivery van.
...etc.

Health items: quinoa, soya milk, chia seeds, avocado.
Power-ups: book, battery, sugar sachet, tiny canvas.
...how are powerups used? change pwups!
Weapons: fists, butter knife, cezve, (...taser?), ...
...how to make weapons degrade every use???
'''


# A Base Class for Items

class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Class for money item

class Dosh(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Dosh",
				description="A scrap of paper with the number {} inked on in...blood?".format(str(self.amt)),
				value=self.amt)


# Classes for weapon items

class Weapon(Item):
        def __init__(self,name,description,value,damage):
                self.damage = damage
                super().__init__(name,description,value)

        def __str__(self):
                return "{}\n=====\n{}Value: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Fists(Weapon):
	def __init__(self):
		super().__init__(name="Fists",
				description="The good ol' bumper brothers.",
				value=0,
				# how to make unsellable???
				damage=5)
class Knife(Weapon):
	def __init__(self):
		super().__init__(name="Knife",
				description="A stainless steel butter knife.",
				value=1,
				damage=8)

class Cezve(Weapon):
	def __init__(self):
		super().__init__(name="Cezve",
				description="For brewing coffee that packs a punch.",
				value=10,
				damage=15)


