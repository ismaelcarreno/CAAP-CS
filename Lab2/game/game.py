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
	global leaderboard
	# score = moves
	print ("================================\nGame Over\n================================")
	if won == True:
		print("WINNER WINNER CHICKEN DINNER")
		print("Your moves:", moves)
		score = Score(name, moves)
		if leaderboard.update(score) == True:
			leaderboard.insert(score)

	else:
		print("You became Bigfoot's dinner!")
	leaderboard.print_board()
	names = ''
	moves = 0

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():   #this is where you go to make the leaderboard permanent
	while True:
		global name
		global moves
		print ("\nWelcome to FOOT CHASE! To quit enter :q at any time. Good luck!") # raise ValueError ('todo')
		difficulty = input("\nEnter the number of lives that you want to have, be a man or a chicken.\n(1-2 Hard / 3-5 Medium / 5+ Too easy): ")
		if (difficulty == ':q'):
			exit(1)
		try:
			difficulty = int(difficulty)
		except ValueError: 
			exit(1)
		name = input("\nLet's play. Enter your name. > ")
		if (name == ':q' ):
			exit(1)
		a_map = Map('the_forest') 
		a_game = Engine(a_map, difficulty)
		moves = a_game.play() 
		game_over(a_game.won())

play_game()
