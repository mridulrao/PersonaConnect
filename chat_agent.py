import json
import sys
import csv
sys.path.append('..')


import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.extraction import default_extractor as extractor
from tinytroupe.extraction import ResultsReducer
import tinytroupe.control as control


from actors import choose_or_create_agent

agent = choose_or_create_agent()

context = input("Give a context about your situation")

agent.listen(context)

multi_turn = 5

while multi_turn: 
	user_msg = input()
	agent.listen(user_msg)
	agent.act()
	multi_turn -= 1