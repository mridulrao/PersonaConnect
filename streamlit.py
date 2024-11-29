import streamlit as st
import sys
sys.path.append('..')

# Import your agent creation functions
from default_actors import (
    create_liam_the_logical, create_sophia_the_strategist,
    create_ethan_the_enthusiast, create_maya_the_mindful,
    create_oliver_the_optimist, create_isabella_the_investigator,
    create_daniel_the_devils_advocate, create_ella_the_creative,
    create_agent_with_customization
)

# Import TinyPerson and other necessary modules
import tinytroupe
from tinytroupe.agent import TinyPerson

# Define agents with their properties
agents = [
    {
        'name': 'Liam the Logical',
        'function': create_liam_the_logical,
        'traits': 'Analytical, methodical, objective.',
        'background': 'Software engineer with expertise in artificial intelligence and systems design.',
        'color': '#1E90FF',  # Dodger Blue
        'icon': '🔍'
    },
    {
        'name': 'Sophia the Strategist',
        'function': create_sophia_the_strategist,
        'traits': 'Visionary, strategic, forward-thinking.',
        'background': 'Business consultant specializing in strategic planning and organizational development.',
        'color': '#32CD32',  # Lime Green
        'icon': '📊'
    },
    {
        'name': 'Ethan the Enthusiast',
        'function': create_ethan_the_enthusiast,
        'traits': 'Energetic, optimistic, motivational.',
        'background': 'Motivational speaker and personal development coach.',
        'color': '#FFD700',  # Gold
        'icon': '🌟'
    },
    {
        'name': 'Maya the Mindful',
        'function': create_maya_the_mindful,
        'traits': 'Reflective, empathetic, balanced.',
        'background': 'Psychologist with a focus on mindfulness and well-being.',
        'color': '#FF69B4',  # Hot Pink
        'icon': '💖'
    },
    {
        'name': 'Oliver the Optimist',
        'function': create_oliver_the_optimist,
        'traits': 'Hopeful, encouraging, future-oriented.',
        'background': 'Environmentalist and sustainability advocate.',
        'color': '#00BFFF',  # Deep Sky Blue
        'icon': '🌱'
    },
    {
        'name': 'Isabella the Investigator',
        'function': create_isabella_the_investigator,
        'traits': 'Curious, inquisitive, open-minded.',
        'background': 'Journalist with experience in investigative reporting.',
        'color': '#FF4500',  # Orange Red
        'icon': '🕵️‍♀️'
    },
    {
        'name': 'Daniel the Devil\'s Advocate',
        'function': create_daniel_the_devils_advocate,
        'traits': 'Critical, skeptical, challenging.',
        'background': 'Lawyer specializing in debate and rhetoric.',
        'color': '#8B0000',  # Dark Red
        'icon': '⚖️'
    },
    {
        'name': 'Ella the Creative',
        'function': create_ella_the_creative,
        'traits': 'Imaginative, artistic, intuitive.',
        'background': 'Artist and designer with a flair for innovation.',
        'color': '#800080',  # Purple
        'icon': '🎨'
    }
]


# Add custom CSS for cards and chat styling
st.markdown("""
    <style>
        /* General app background */
        body {
            background-color: #121212; /* Dark theme background */
            color: #FFFFFF;
        }

        /* Styling for cards */
        .card {
            background-color: #1E1E1E;
            border: 1px solid #333333;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        }

        /* Agent name styling */
        .card h3 {
            margin: 0;
            padding: 0;
            font-size: 1.5rem;
            color: #FFFFFF;
        }

        /* Highlighted agent name color */
        .card h3 span {
            font-weight: bold;
        }

        /* Agent traits and background */
        .card p {
            color: #B0B0B0;
            font-size: 1rem;
            margin: 10px 0;
        }

        /* Buttons */
        .card .select-button {
            background-color: #1E90FF;
            border: none;
            border-radius: 10px;
            color: #FFFFFF;
            font-size: 1rem;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
            margin-top: 10px;
        }

        .card .select-button:hover {
            background-color: #007ACC;
            transform: scale(1.05);
        }

        /* Chat bubbles */
        .chat-bubble {
            max-width: 70%;
            padding: 10px 15px;
            margin: 10px;
            border-radius: 15px;
            position: relative;
            color: #FFFFFF;
        }

        .chat-bubble-user {
            background-color: #1E90FF;
            align-self: flex-end;
            margin-left: auto;
        }

        .chat-bubble-agent {
            background-color: #333333;
            align-self: flex-start;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)


# Initialize session state variables
if 'agent' not in st.session_state:
    st.session_state.agent = None

if 'agent_name' not in st.session_state:
    st.session_state.agent_name = None

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Title of the app
st.title("🌟 Multi-Personality Agent Chat")

# Agent Selection via Cards
if st.session_state.agent is None:
    st.subheader("Select an Agent to Chat With:")
    for agent in agents:
        with st.container():
            # Display the card
            st.markdown(
                f"""
                <div class="card">
                    <h3 style="color: {agent['color']}">{agent['icon']} <span>{agent['name']}</span></h3>
                    <p><b>Traits:</b> {agent['traits']}</p>
                    <p><b>Background:</b> {agent['background']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            # Use Streamlit button for selection
            if st.button(f"Select {agent['name']}", key=f"select_{agent['name']}"):
                st.session_state.agent_name = agent['name']
                st.session_state.agent = agent['function']()
                st.session_state.conversation_history = []
                st.session_state.context_given = False
                st.rerun()
else:
    # Chat Interface
    st.subheader(f"Chatting with {st.session_state.agent_name}")

    # Provide context input if not given yet
    if not st.session_state.context_given:
        context = st.text_input("Provide context about your situation", key='context_input')
        if context:
            st.session_state.agent.listen(context)
            st.session_state.context_given = True
            # Append to conversation history
            st.session_state.conversation_history.append((st.session_state.agent_name, "Context noted. How can I assist you?"))
            # Clear the context input
            del st.session_state['context_input']
            st.rerun()

    else:
        # Display the conversation history
        for speaker, message in st.session_state.conversation_history:
            bubble_class = "chat-bubble-user" if speaker == "You" else "chat-bubble-agent"
            st.markdown(
                f"""
                <div class="chat-bubble {bubble_class}">
                    <b>{speaker}:</b> {message}
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Create a form for input
        with st.form(key='message_form', clear_on_submit=True):
            user_input = st.text_input("You:", key='user_input')
            submit_button = st.form_submit_button("Send")
            
            if submit_button and user_input:
                # Agent listens and acts
                st.session_state.agent.listen(user_input)
                agent_act = st.session_state.agent.act(return_actions=True)
                talk_content = [
                    entry['action']['content'] 
                    for entry in agent_act 
                    if entry['action']['type'] == 'TALK'
                ]

                st.session_state.agent_response = talk_content[0]
                st.session_state.conversation_history.append(("You", user_input))
                st.session_state.conversation_history.append((st.session_state.agent_name, st.session_state.agent_response))
                
                st.rerun()
