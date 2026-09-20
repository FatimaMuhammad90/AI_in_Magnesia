class Agent:

    def __init__(self, citizen):
        self.citizen = citizen
        self.memory = []

    def build_prompt(self, event, laws, previous_arguments=None):

        prompt = f"""
You are {self.citizen.name}, a citizen of Magnesia.

Your characteristics:
- Age: {self.citizen.age}
- Property class: {self.citizen.property_class}
- Occupation: {self.citizen.occupation}
- Personality: {self.citizen.personality}

You live in Magnesia and must reason according to its laws,
customs, and social structure.

MAGNESIAN LAWS:
{laws}

CURRENT EVENT:
{event.description}
"""

        if previous_arguments:
            prompt += f"""
    
    ARGUMENTS ALREADY MADE BY OTHER CITIZENS:
    {previous_arguments}
    
    Respond to their arguments.
    You may disagree with them, but your reasoning must remain
    consistent with the laws and values of Magnesia.
    """

        prompt += """Give your position on the event and explain your reasoning.Do not speak as an AI. Speak as the citizen."""

        return prompt

    # def argue(self, event, laws, previous_arguments):
    #     prompt = self.build_prompt(
    #         event,
    #         laws,
    #         previous_arguments
    #     )
    #
    #     response = self.llm_client.generate(
    #         model=self.model,
    #         prompt=prompt
    #     )
    #
    #     self.memory.append(response)
    #
    #     return response