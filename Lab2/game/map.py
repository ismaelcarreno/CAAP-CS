# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter,
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'humanities' : S.Humanities(), #just like Dog() or Map(), They're class names because they're capitalized
				'math' : S.Math(), #left side is the key and the right side is the value 
				'writing' : S.Writing(), #This is how we reference a scene object when we enter a string because the keys are associated with the values
				'computer_science' : S.ComputerScience(), #It's a scene object because we're calling the scene constructor(__init__) when we use ()
				'death' : Death()
				# raise ValueError ('todo')
				} #Called a dictionary, data structure that holds key data values

	# initializes to a starting scene
	def __init__(self, start_scene): #Constructor function
		self.start_scene = start_scene

	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return self.scenes.get(scene_name) #could also be Map.scenes.get(scene_name) we're passing in our key here of the scene

	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene) #Giving dominos my order and address the string tht
		# opening - dominos, next  - Papa Johns, scenes.get - Lil Cesars, Current Scene is me
