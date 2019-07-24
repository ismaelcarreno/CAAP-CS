# importing package to be able to run the tests
from nose.tools import *
# Here you should import all the modules/classes you want to test
from game.scores import Score
import game.game

# define a function like these for each class/module you test.
# e.g. assert 2+2 == 4
def test_scores():
	score = test_score('test', 1)
	assertEqual(score.get_name(), 'test')
	assertEqual(score.get_score(), 1)

test_scores()
# etc...