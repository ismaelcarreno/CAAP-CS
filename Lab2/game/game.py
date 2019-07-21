# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ''
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	print ("\nGame Over\n")
	print("Yo moves:", moves)
	if won == True:
		print("WINNER WINNER CHICKEN DINNER")
	else:
		print("You are a lameoo!!")
	# score = Score(name, moves)
	# if (self.escaped == True):
	# 	leaderboard.update(score)
		#leaderboard.insert(score)
	#raise NumberOne("You're Great")
	names = ''
	moves = 0
	exit(1)
	
	#leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name
		global moves
		print ("Welcome to my game! To quit enter :q at any time. Good luck!") # raise ValueError ('todo')
		difficulty = input("\nEnter the number of lives that you want to have, be a man or a chicken (1-2 Hard / 3-5 Medium / 5+ Too easy): ")
		if (difficulty == ':q'):
			exit(1)
		difficulty = eval(difficulty)
		# if (difficulty == ':q'):
		# 	exit(1)
		name = input("\nLet's play. Enter your name. > ") # raise ValueError ('todo')
		if (name == ':q' ):
			exit(1)
		a_map = Map('humanities') # raise ValueError ('todo')
		a_game = Engine(a_map, difficulty) #same thing as the thing above
		moves = a_game.play() #raise ValueError ('todo') ### MOST IMPORTANT FUNCTION
		game_over(a_game.won())

play_game()
