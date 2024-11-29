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

factory = TinyPersonFactory("You are a random employee of a tech company")

people = []
for i in range(2):
    person = factory.generate_person(temperature=1.6)
    print(person.minibio())
    people.append(person)

len(people)


company = TinyWorld("Singularity Inc.", people)
company.make_everyone_accessible()

company.broadcast("You are asking an AI chat bot for helping you sort out a problem related to bug in a code. Provide details like your employee ID and the problem you are facing")

company.run(2)