# imports the score class to be used in the leaderboard.
from scores import Score
from random import randint

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):

		for i in range(self.size):
			name = 'Player'
			moves = randint(10,20)
			score = Score(name, moves)
			self.board.append(score)
			self.board.sort(key=lambda x: x.get_score())

	# prints the leaderboard
	def print_board(self):
		print("==========================================")
		print("\t\tLEADERBOARD:")
		print("==========================================")
		for i in range (self.size):
			print("\t", str(i+1) + ")", self.board[i].get_name(),':', self.board[i].get_score(), "moves")

	#checks if given score should be in the leaderboard
	def update(self, score):
		self.new_scores = score.get_score()
		for i in range(self.size):
			if (self.new_scores <= self.board[i].get_score()):
				return True

		#inserts the score in the given position assuming it's better or equal to the one in the given rankmoving everything below down a rank
	def insert(self, score):
		for i in range(self.size):
			if score.get_score() < self.board[i].get_score():
				self.board.insert(i,score)
				return

		
				# elif (new_scores <= self.board[1]):
						# self.board[2:5]

		#use a for loop, there's a function called 'insert' that is built in (uses indexes)
									#raise ValueError ('todo')

#test = Leaderboard()
#test.print_board()
#test_score = Score("test", 7)
# test.print_board()