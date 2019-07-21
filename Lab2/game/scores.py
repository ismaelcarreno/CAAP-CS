class Score(object):
	name = 'player'
	score = 9999

	# initializes score and players name
	def __init__(self, name=None, score=None):
		self.name =  name or self.name 
		self.score = score or self.score
		#raise ValueError ('todo')

	# returns the name associated with score
	def get_name(self):
		raise ValueError ('todo')

	# returns score of player
	def get_score(self):
		raise ValueError ('todo')
