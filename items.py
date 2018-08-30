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
(Power-ups can't be used, but raise health amount!(?))
(Health is only attack/defense against monsters?!!)
(Self-healing abilities: talk to s.one, mindful breaths...?)
'''


# Base Class for Items

class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

