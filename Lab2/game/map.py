# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter,
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'the_forest' : S.Forest(),
				'secret_trail' : S.SecretTrail(),
				'normal_trail' : S.NormalTrail(), 
				'clearing' : S.Clearing(), 
				'cabin' : S.Cabin(),
				'inside' : S.Inside(),
				'safe' : S.Safe(),
				'death' : Death()
				} #Called a dictionary, data structure that holds key data values

	# initializes to a starting scene
	def __init__(self, start_scene): #Constructor function
		self.start_scene = start_scene

	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return self.scenes.get(scene_name) 

	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)
