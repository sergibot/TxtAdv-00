''' Chapter 1 in the text adv '''
# how to make each line of text appear on user click??
# attach an image file to each scene?
# display this in a GUI? tkinter? or pygame why not!

# test edit from phone app??

def intro():

	print("Hello and welcome! You are in a field at night...")

	# start music when user presses enter?

	# clear screen

	print("And you can't remember a thing. Not even your name. Um.")
	name = input("What should I call you?/n")
	print("Well alright, but that was entirely your choice!")
	# eventually print a random variant of this line...
	
def ch1.1():
	print("So I guess I should introduce myself, too.")
	print("Oh haha where to start...")
	print(". . .")
	print("OH GOD YOU'RE ON FIRE!!?!")
	print("HOW DID THIS HAPPEN?? QUICK, ROLL AROUND ON THE FLOOR!!!")
	# give user option to roll around on the floor (tutorial entry)
	# if user doesn't respond within five seconds, put burnt/crispy/welldone at start of their name
	print("Ahh, much better. Guess you're pretty hot stuff, eh ", name, "?")
	print("We'll see if that helps you at all in these coming challenges, though.")
	print("I mean, what? Oh look, a door!")
	print("(You're still a loser in a field, though.)")
	print("Wanna head through the door? Guess you can look around for other stuff here too.")
	# give options
	# if other stuff - print("You can't see anything. It's pitch black and you're in a field.")
	print("Cool! A door!")
	print("...and it's unlocked!")
	print("You open it, but can\'t see what\'s on the other side.")
	print("Gonna try to walk through?")
	# one choice. splits into random alternative. door leads to one of:
	#  a) snail narnia, b) a library w/o light, c) a pond rave, d) a worm's art gallery
	# and some options integrate clickable bits of the pic by pygame stuff

def ch1():
	intro()
	ch1.1()


def choice(a,b,c):
	# how to vary number of choices input as variables here??
	# i_choose = input("A - ", a, "; B - ", B - ", b, "; C - ", c).lower()
	# if i_choose == 'a':
	#	return a
	# elif i_choose == 'b':
	#	return b
	# elif i_choose == 'c':
	# 	return c

def start():
	ch1()

start()
