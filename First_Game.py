from sys import exit

bag = ['Apple']

def start():
	print "You are now in a small cave."
	print "You have a small inventory with space for two items. Simply type 'inventory' to view."
	print "Do you choose to go straight, right, or left?"

	move = True
	while move:
		next = raw_input('> ')

		if next == 'straight':
			deeper()
		elif next == 'left':
			dead("Oops! You fall into a pit.")
		elif next == 'right':
			sword()
		elif next == 'inventory':
			print bag
			print "Where do you choose to go?"
		else:
			print "Please enter valid input."

def dead(why):
	"""Ends the game""" 
	print why, "Game over."
	playAgain()

def playAgain():
	again = raw_input('Play again? (Yes/No)\n> ')
	if again == 'yes':
		start()
	else:
		exit(0)


#def monster():
	#print "A monster has killed you."

def deeper():
	print "You step deeper into the cave. You hear hissing."
	print "Do you choose to go forward or turnaround?"
	move = True

	while move:
		next = raw_input('> ')

		if next == 'forward' and 'Sword' not in bag:
			dead("You cannot defend yourself. A monster has killed you.")
			move = False
		elif next == 'forward' and 'Sword' in bag:
			kill()
		elif next == 'turnaround':
			turnaround()
		elif next == 'inventory':
			print bag
			print "Where do you choose to go?"
		else:
			print "Please input 'forward' or 'turnaround'."

def turnaround():
	print "You decide to turnaround."
	print "Do you choose to go straight, right, or left?"
	move = True
	
	while move:
		next = raw_input('> ')

		if next == "straight":
			print "That is the exit. You cannot exit."
			turnaround()
		elif next == "right" and 'Sword' not in bag:
			dead("You cannot defend yourself. A monster has killed you.")
		elif next == "right" and 'Sword' in bag:
			kill()
		elif next == "left" and 'Sword' in bag:
			print "That is where you picked up the sword."
			turnaround()
		elif next == 'left' and 'Sword' not in bag:
			sword()
		elif next == 'inventory':
			print bag
			print "Where do you choose to go?"
		else:
			print "Please input 'straight', 'right', or 'left'."

def turnaround2():
	print "You decide to turnaround."
	print "Do you choose to go straight. right, or left?"
	move = True

	while move:
		next = raw_input('> ')



def sword():
	print "You stumble across a sword."
	print "Do you pick up sword? (Yes/No)"
	move = True

	while move:
		next = raw_input('> ')

		if next == 'yes':
			print "You have added 'Sword' to your inventory."
			bag.append('Sword')
			deeper()
		elif next == 'no':
			print "You have ignored the sword."
			deeper()
		elif next == 'inventory':
			print bag
			print "Do you want the sword?"
		else:
			print "Please input 'yes' or 'no'."

def kill():
	print "The sword shines and kills the monster!"
	print "You now exit the cave and win!"
	playAgain()


start()

