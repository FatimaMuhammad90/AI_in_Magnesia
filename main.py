# Imports
from simulation.world import Magnesia
from Citizen.Citizens import citizen1, citizen2, citizen3, citizen4, citizen5
from simulation.Event import Event
from agents.agent import Agent

# Create Magnesia
magnesia = Magnesia()

# Add all the citizens
magnesia.add_citizen(citizen1)
magnesia.add_citizen(citizen2)
magnesia.add_citizen(citizen3)
magnesia.add_citizen(citizen4)
magnesia.add_citizen(citizen5)


# Create Event
event = Event(
    "Illegal Commerce",
    "A citizen has secretly started operating a private merchant business."
)

# Agents
agents = [
    Agent(citizen1),
    Agent(citizen2),
    Agent(citizen3),
    Agent(citizen4),
    Agent(citizen5)
]


arguments = []

for agent in agents:

    prompt = agent.build_prompt(
        event,
        magnesia.laws,
        arguments
    )

    print("\n" + "=" * 60)
    print(agent.citizen.name)
    print("=" * 60)

    print(prompt)

    arguments.append(
        f"{agent.citizen.name}: [LLM response will go here]"
    )