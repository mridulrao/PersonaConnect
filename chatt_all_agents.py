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

from default_actors import create_liam_the_logical, create_sophia_the_strategist
from default_actors import create_ethan_the_enthusiast, create_maya_the_mindful
from default_actors import create_oliver_the_optimist, create_isabella_the_investigator
from default_actors import create_daniel_the_devils_advocate, create_ella_the_creative

context = input("Give context")
query = input("Give query")

default_agent_functions = [
    ('Liam the Logical', create_liam_the_logical),
    ('Sophia the Strategist', create_sophia_the_strategist),
    ('Ethan the Enthusiast', create_ethan_the_enthusiast),
    ('Maya the Mindful', create_maya_the_mindful),
    ('Oliver the Optimist', create_oliver_the_optimist),
    ('Isabella the Investigator', create_isabella_the_investigator),
    ('Daniel the Devil\'s Advocate', create_daniel_the_devils_advocate),
    ('Ella the Creative', create_ella_the_creative)
]

for i in range(len(default_agent_functions)):
	agent_name, agent_function = default_agent_functions[i]
	print(f"Talking to {agent_name}")

	agent = agent_function()
	agent.listen(context)
	agent.listen(query)
	agent.act()


