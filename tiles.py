''' Map tiles! '''

import items, monsters, actions, world

class MapTile:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def adjacent_moves(self):
		# tells player all move actions for adjacent tiles (?)
		moves = []
		if world.tile_exists(self.x+1,self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x-1,self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x,self.y-1):
			moves.append(actions.MoveNorth())
		if world.tile_exists(self.x,self.y+1):
			moves.append(actions.MoveSouth())  # is that right?
		return moves
	def available_actions(self):
		# tells player all available actions in this room
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		return moves



# (these are to warn us in case we create a maptile directly)
def intro_text(self):
	raise NotImplementedError()
def modify_player(self,player):
	raise NotImplementedError()


class StartingRoom(MapTile):
	def intro_text(self):
		return """
		You open your eyes to darkness.
		As you sit yourself up,
		The floor beneath you feels like damp grass.
		A dull aching dawn lifts up the horizon.
		Birdsong begins to light up your spirit.
		Your soft pillow was a cowpat, by the way.
		You pick yourself up,
		Dust yourself down,
		And decide to just rock the ashy brunette.
		There's a door in front of you.
		Like, just a door.
		...Might as well open it?
		"""
	def modify_player(self,player):
		# Room has no action on player
		pass


class LootRoom(MapTile):
	def __init__(self,x,y,item):
		self.item=item
		super().__init__(x,y)
	def add_loot(self,player):
		player.inventory.append(self.item)
	def modify_player(self,player):
		self.add_loot(player)

class EnemyRoom(MapTile):
	def __init__(self,x,y,monster):
		self.monster=monster
		super().__init__(x,y)
	def modify_player(self,the_player):
		# is player has not killed the enemy, player is attacked.
		if self.monster.is_alive():
			the_player.hp = the_player.hp - self.monster.dmg
			print("Monster does {} damage. You have {} HP left.".format(self.enemy.dmg, the_player.hp))
	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile=self),actions.Attack(enemy=self.enemy)]
		else:
			return self.adjacent_moves()


class EmptyRoom(MapTile):
	def intro_text(self):
		return """
		Nothing of significance here.
		Smells of a field?
		You remember the cowpat.
		"""
	def modify_player(self,player):
		# Room has no action on player
		pass

class GiantKittenRoom(EnemyRoom):
	def __init__(self,x,y):
		super().__init__(x,y,monsters.giant_kitten())
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			OMG GIANT KITTY!!!
			You can feel its fuzzy claws sink into your future.
			D'awww...
			"""
		else:
			return """
			Who killed this massive kitten?
			And who's gonna help me eat it?
			"""
class FindKnifeRoom(LootRoom):
	def __init__(self,x,y):
		super().__init__(x,y,items.Knife())
	def intro_text(self):
		return """
		You nearly step on a knife.
		Instead, you step on a nail.
		OW! Who built this hitshole?
		...You pick up the knife.
		"""




class CompletionRoom(MapTile):
	def intro_text(self):
		return '''
		Well, well, well.
		You've gone and done it.
		I'm impressed.
		Still, you just lost The Game.
		;)
		'''
	def modify_player(self,player):
		player.victory=True

