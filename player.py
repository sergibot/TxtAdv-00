# player file

import random
import items, world

class Player():
    def __init__(self):
        self.inventory = [items.Dosh(15),items.Fists()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
    def is_alive(self):
        return self.hp > 0
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    def do_action(self,action,**kwargs):
        action_method=getattr(self,action.method.__name__)
        if action_method:
            action_method(**kwargs)
    def flee(self,tile):
	# moves player to a random adjacent tile
        available_moves = tile.adjacent_moves()
        r=random.randint(0,len(available_moves)-1)
        self.do_action(available_moves[r])
    def is_victory(self):
        print("fix this later - def is_victory in player... .")

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)
    def move_south(self):
        self.move(dx=0, dy=1)
    def move_east(self):
        self.move(dx=1,dy=0)
    def move_west(self):
        self.move(dx=-1,dy=0)

    def attack(self,monster):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            # (isinstance is a builtin function!!!)
            if isinstance(i, items.Weapon):
                if i.dmg > max_dmg:
                    max_dmg = i.dmg
                    best_weapon = i
        print("You use {} against {}.".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.dmg
        if not enemy.is_alive():
    	    print("You vanquished the {}! All praise {}!").format(enemy.name, player.name)
        else:
    	    print("{} HP is {}.".format(enemy.name,enemy.hp))

