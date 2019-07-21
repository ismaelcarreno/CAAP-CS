 # This is the engine of the game, basically runs everything

class Engine(object):

	# global variables to keep track of game status and live count
	escaped = False #raise ValueError ('todo')
	lives = 0   #raise ValueError ('todo')

	# initializes the map in the game
	def __init__(self, scene_map, lives):
		self.scene_map = scene_map
		self.lives = lives
	# takes current scene, plays it, gets the next scene, and updates the game
	# should also return the number of moves the game takes in total
	def play(self):
		current_scene = self.scene_map.opening_scene() # scene map is refering to a_map. It's calling the opening scene function of the scene_map object and saving it to current_scene
		next_scene_name = ''
		checkpoint = current_scene
		n_moves = 0
		
		while (next_scene_name != 'finished' and self.lives > 0):
			print ("\n*******************************************************************") #raise ValueError ('todo')
			print(current_scene)
			next_scene_name = current_scene.enter() #(This is me again) current_scene is the object and enter being called on a scene object and we want it to return the enter value within the current_scene object

			if (next_scene_name == ':q'):
				exit(1)
			elif (next_scene_name == 'death'):
				checkpoint = current_scene
				# n_moves += 1
				#current_scene = self.scene_map.next_scene(current_scene) not needed? #First one: for the first scene solely? Second one: for every other scene?
				current_scene = self.scene_map.next_scene(next_scene_name) #difference between this one and the one above
				#raise ValueError ('todo')
			elif (next_scene_name == 'died'):
				self.lives -= 1
				current_scene = checkpoint #it resets the location to the beginning?
				# n_moves += 1
				# print("You dead") #added by me
				# return self.won()#added by me
				#raise ValueError ('todo')
			else:
				checkpoint = current_scene #?????
				n_moves += 1
				current_scene = self.scene_map.next_scene(next_scene_name)
				
		if (next_scene_name == 'finished'):
			print("\nYou're out my boy!!!!")
			self.escaped = True

		return n_moves
				#self.escaped = True
				#what's self.scene_map ???
				# print()
				# return self.won()
				#self.escaped = True
				#raise ValueError ('todo')

			# if (exit scene):
			# 	self.escaped = True
			# 	return n_moves
			# 	print("You have escaped, nice")
				# if (raise ValueError ('todo')):
				# 	self.escaped = True
				# 	return n_moves #raise ValueError ('todo')

	# updates the variable to determine whether player won or failed.
	def won(self):
		if(self.escaped == True):
			return True
		if(self.escaped == False):
			return False #what does this do	#raise ValueError ('todo')
