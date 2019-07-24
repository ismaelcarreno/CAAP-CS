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


class Forest(Scene):

	name = 'the_forest'

	def enter(self):
		print("FOREST\n==========================================")
		print ("You were hiking on a trail in the alaskan mountains when suddely the whole forest began to tremble. You turn around and see that a 10ft tall monster that is competely covered with hair is running towards you. You begin to panic and...")
		return self.action() #we're returning the return value of action




	def action(self):
		print ("\nWhat will you do?")
		
		choice = input("\n1) - Run into the abyss of the forest \n2) - Run on the trail  \n3) - Hold your ground and fight \nEnter number: ")
		
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("\nTHAT'S NOT AN INT!")
		   return self.exit_scene(self.name)


		if int(choice) == 1:
			print ("You run off the trail and vanish within the forest.")
			return self.exit_scene('secret_trail')
		elif int(choice) == 2:
			print ("You stay on the trail and just run, hoping for the best.")
			return self.exit_scene('normal_trail')
		elif int(choice) == 3:
			print ("Bigfoot hits you and you go flying. Your body goes limp and everything goes black.")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome 

class NormalTrail(Scene):

	name = 'normal_trail'

	def enter(self):
		print("NORMAL TRAIL\n==========================================")
		print ("The trail comes to a dead end where a raging river is blocking your path. Bigfoot is only a few meters behind you.")
		return self.action()

	def action(self):
		print ("\nWhat will you do?")
		choice = input("\n1) - Juke Bigfoot \n2) - Run alongside the river  \n3) - Jump into the river \nEnter number: ")
		
		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("\nTHAT'S NOT AN INT!")
		   return self.exit_scene(self.name)



		if int(choice) == 1:
			print ("You slip and Bigfoot steps on you.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("You follow the current of the river and run in that direction.")
			return self.exit_scene('clearing')
		elif int(choice) == 3:
			print ("You don't know how to swim so the current takes you down and you drown.")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome 

class SecretTrail(Scene):

	name ='secret_trail'

	def enter(self):
		print("SECRET TRAIL\n==========================================")
		print ("You're slowly losing your pace and Bigfoot is getting closer by the passing second. You might be able to run faster, but he will soon catch up when your legs give out.")
		return self.action() #we're returning the return value of action

	def action(self):
		print ("\nWhat will you do?")
		choice = input("\n1) - Hide \n2) - Keep on running \n3) - Turn and fight \nEnter number: ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("\nTHAT'S NOT AN INT!")
		   return self.exit_scene(self.name)



		if int(choice) == 1:
			print ("You hide under a bush, but Bigfoot finds you and kills you with one punch.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("You keep on running and pray that something will help you.")
			return self.exit_scene('clearing') 
		elif int(choice) == 3:
			print ("You charge toward Bigfoot, but he tackles you down and ends your life.")
			return self.exit_scene('death') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Clearing(Scene):

	name ='clearing'

	def enter(self):
		print("CLEARING\n==========================================")
		print ("You stumble upon  a clearing that has a cabin situated on the far end. Bigfoot has closed the distance and is right behind you. Will you make it or should you just find an alternative option....") 
		return self.action() #we're returning the return value of action

	def action(self):
		print ("\nWhat will you do?")
		choice = input("\n1) - Run toward the cabin \n2) - Run into the forest \n3) - Turn and fight \nEnter number: ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("\nTHAT'S NOT AN INT!")
		   return self.exit_scene(self.name)



		if int(choice) == 1:
			print ("You run toward the cabin and make it to the door.")
			return self.exit_scene('cabin')
		elif int(choice) == 2:
			print ("You run into the forest and trip, Bigfoot catches up and kills you.")
			return self.exit_scene('death') 
		elif int(choice) == 3:
			print ("You charge toward Bigfoot, but he tackles you down and ends your life.")
			return self.exit_scene('death') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Cabin(Scene):

	name ='cabin'

	def enter(self):
		print("CABIN\n==========================================")
		print ("You notice that the door is unlocked. You turn around and see that Bigfoot will be on the front porch in a matter of seconds.")
		return self.action() #we're returning the return value of action

	def action(self):
		print ("\nWhat should you do?")
		choice = input("\n1) - Hide \n2) - Trap him inside \n3) - Barricade the door \nEnter number: ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("\nTHAT'S NOT AN INT!")
		   return self.exit_scene(self.name)



		if int(choice) == 1:
			print ("You hide under the bed, but the attempt is feeble as Bigfoot quickly finds you in the tiny cabin. He steps on you and instantly ends you.")
			return self.exit_scene('death') 
		elif int(choice) == 2:
			print ("You let him in and attempt to juke him, so that he's left inside. However, he trips you as you try to run around and captures you")
			return self.exit_scene('death') 
		elif int(choice) == 3:
			print ("You block the door with the few pieces of furniture that are inside")
			return self.exit_scene('inside') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Inside(Scene):

	name = 'inside'	

	def enter(self):
		print("INSIDE\n==========================================")
		print ("*Bang* *Bang* \nThe barricade is keeping Bigfoot out, but not for long. You begin rummaging through the cabin for anything to aid you. The cabin is pretty empty, but you find a safe under the bed. It has a code, you try to unlock it out of desperation.")
		return self.action()

	def action(self):
		code = [2, 1, 4]
		guesses = 0
		for i in range(3):
			print ("Enter digit %d." % (i+1))
			guess = input("[Lock]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except ValueError:
			   print("\nTHAT'S NOT AN INT!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("NOPE!")
				guesses += 1
				guess = input("[Lock]> ") 
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except ValueError: 
				   print("\nTHAT'S NOT AN INT!")
				   return self.exit_scene(guess)
				   guess = -1 

		if guesses < 10:
			print ("The safe opens and reveals a possible way to escape.")
			return self.exit_scene('safe')
		else:
			print ("The safe doesn't budge and Bigfoot breaks through the door. He towers over you and ends your life with a single punch.")
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		 return outcome



class Safe(Scene):

	name = 'safe'

	def enter(self):
		print("SAFE\n==========================================")
		print("There are 3 different guns within the safe, each with an empty clip. There's a box of ammo, but it corresponds to only one weapon and you have no idea which one it could be. The door breaks behind you, you grab a bullet and choose one of the guns.")
		return self.action()


	def action(self):
		print ("\nWhich one do you take?")
		good_weapon = randint(1,3)
		guess = input("[Weapon #]> ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
		   guess = int(guess)
		except ValueError: 
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(guess) != good_weapon:
			print ("You slip the bullet into the gun, turn, aim and shoot.... the gun doesn't fire. He towers over you and then everything goes black.")
			return self.exit_scene('death')
		else:
			print ("You slip the bullet into the gun, turn, aim and shoot Bigfoot on the temple. He falls face down on the floor.")
			return self.exit_scene('finished')

	def exit_scene(self, outcome):
		return outcome
