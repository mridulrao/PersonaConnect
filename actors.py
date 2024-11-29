'''

This file will create a base actor based on user inputs. 


'''

from default_actors import create_liam_the_logical, create_sophia_the_strategist
from default_actors import create_ethan_the_enthusiast, create_maya_the_mindful
from default_actors import create_oliver_the_optimist, create_isabella_the_investigator
from default_actors import create_daniel_the_devils_advocate, create_ella_the_creative

from default_actors import create_agent_with_customization


# List of default agent creation functions
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

def choose_or_create_agent():
    print("Welcome! Would you like to use a default agent or create your own?")
    print("1. Use a default agent")
    print("2. Create your own agent")
    choice = input("Please enter 1 or 2: ").strip()
    
    if choice == '1':
        print("\nDefault Agents Available:")
        for idx, (agent_name, _) in enumerate(default_agent_functions, start=1):
            print(f"{idx}. {agent_name}")
        agent_choice = input("Please select an agent by entering the corresponding number: ").strip()
        
        try:
            agent_index = int(agent_choice) - 1
            if 0 <= agent_index < len(default_agent_functions):
                agent_name, agent_function = default_agent_functions[agent_index]
                agent = agent_function()
                print(f"\nYou have selected {agent_name}.")
                return agent
            else:
                print("Invalid selection. Please try again.")
                return choose_or_create_agent()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return choose_or_create_agent()
    elif choice == '2':
        agent = create_agent_with_customization()
        print(f"\nYour custom agent has been created: {agent.name}")
        return agent
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return choose_or_create_agent()




