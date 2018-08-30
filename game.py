# to run the game (in a loop)

import world
from player import Player


def play():
	world.load_tiles()
	player=Player()
	room=world.tile_exists(player.location_x,player.location_y)
	while player.is_alive() and not player.is_victory():
		room=world.tile_exists(player.location_x,player.location_y)
		room.modify_player(player)
		# another check, in case the room changed the player's state
		if player.is_alive() and not player.victory:
			print("Choose an action:\n")
			available_actions = room.available_actions()
			for action in available_actions:
				print(action)
			action_input = input("Action: ")
			for action in available_actions:
				if action_input == action.hotkey:
					player.do_action(action,**action.kwargs)
					break


# let's do this!
if __name__ == "__main__":
	play()
