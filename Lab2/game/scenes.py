# imports random madule form library
from random import randint

# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class Humanities(Scene):

	name = ''#raise ValueError ('todo')

	def enter(self):
		print ("You're humanities teacher has bombarded you with work!")
		#raise ValueError ('todo')
		return self.action() #we're returning the return value of action




	def action(self):
		print ("What will you do?")
		#raise ValueError ('todo')
		choice = input("\n1) - Self-care \n2) - Ignore it  \n3) - Work on Math \nEnter number: ")
		
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except :
		   print("That's not an int!")
		   return self.exit_scene(self.name)



		if int(choice) == 1:
			print ("You decide to go biking and suddenly... a car runs over you.")
			#raise ValueError ('todo')
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Your ego begins to nag at your conscious and drives you insane.")
			#raise ValueError ('todo')
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Math is life, so why even bother with reading meaningless literature.")
			#raise ValueError ('todo')
			return self.exit_scene('math') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome #this is yo outcome

class Math(Scene):

	name = ''#raise ValueError ('todo')

	def enter(self):
		print ("You stare at the pset with a quizzical expression.")
		return self.action()
		#raise ValueError ('todo')
		#return raise ValueError ('todo')

	def action(self):
		print ("You get a notificaion in your email about a posting in Canvas. What's your passcode?")
		#raise ValueError ('todo')
		code = [3, 2, 1]
		guesses = 0
		# loop to check three random integers, one at a time
		for i in range(3):
			print ("Enter digit %d." % (i+1))
			guess = input("[keypad]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except : #ValueError
			   print("That's not an int!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("WRONG!")
				guesses += 1
				guess = input("[keypad]> ") #why does this come up twice
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except : #ValueError
				   print("That's not an int!")
				   guess = -1 #what???

		if guesses < 10:
			print ("You access your account and see a reminder from your writing workshop.")
			#raise ValueError ('todo')
			return self.exit_scene('writing')
		else:
			print ("You have forgotten your passcode, so you punch your computer out of frustration and break your hand.")
			#raise ValueError ('todo')
			return self.exit_scene('death') # raise ValueError ('todo')

	def exit_scene(self, outcome):
		 return outcome
	#def exit_scene(raise ValueError ('todo')):
		#return raise ValueError ('todo') """


	



	"""def enter(self):
		print ("You do a dive roll into the Weapon Armory, crouch and scan the room")
		return self.action()
		#raise ValueError ('todo')
		#return raise ValueError ('todo')

	def action(self):
		print ("There's a keypad lock on the box")
		#raise ValueError ('todo')
		code = [randint(0,9), randint(0,9), randint(0,9)]
		guesses = 0
		# loop to check three random integers, one at a time
		for i in range(3):
			print ("Enter digit %d." % (i+1))
			guess = input("[keypad]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except : #ValueError
			   print("That's not an int!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("BZZZZEDDD!")
				guesses += 1
				guess = input("[keypad]> ") #why does this come up twice
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except : #ValueError
				   print("That's not an int!")
				   guess = -1 #what???

		if guesses < 10:
			print ("The container clicks open and the seal breaks, letting gas out.")
			#raise ValueError ('todo')
			return self.exit_scene('the_bridge')
		else:
			print ("The lock buzzes one last time and then you hear a sickening")
			#raise ValueError ('todo')
			return self.exit_scene('death') # raise ValueError ('todo')

	def exit_scene(self, outcome):
		 return outcome
	#def exit_scene(raise ValueError ('todo')):
		#return raise ValueError ('todo') """

class Writing(Scene):

	name ='the_bridge'

	def enter(self):
		print ("The reminder states that your essay is due tonight, but you haven't started...")
		#raise ValueError ('todo')
		return self.action() #we're returning the return value of action

	def action(self):
		print ("What will you do?")
		#raise ValueError ('todo')
		choice = input("\n1) - Run away \n2) - Work on it \n3) - Procrastinate \nEnter number: ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except :
		   print("That's not an int!")
		   return self.exit_scene(self.name)



		if int(choice) == 1:
			print ("Your stipend is quickly taken away and you're left with nothing.")
			#raise ValueError ('todo')
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("The pressure is too much for you and your anxiety sky rockets, ultimately giving you an anxiety attack.")
			#raise ValueError ('todo')
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("You remember that cs is due in two days, so you begin working on it.")
			#raise ValueError ('todo')
			return self.exit_scene('computer_science') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class ComputerScience(Scene):

	name = ''

	def enter(self):
		print("Use the Escape Pod!!!!!")
		return self.action()
		#raise ValueError ('todo')


	def action(self):
		print ("There's 5 pods, which one do you take?")
		good_pod =  3  #randint(1,5)
		guess = input("[pod #]> ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
		   guess = int(guess)
		except: #ValueError
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(guess) != good_pod:
			print ("You jump into pod %s and hit the death button."% guess)
			#raise ValueError ('todo')
			return self.exit_scene('death')
		else:
			print ("You jump into pod %s and hit the win button."% guess)
			#raise ValueError ('todo')
			return self.exit_scene('finished')

	def exit_scene(self, outcome):
		return outcome
