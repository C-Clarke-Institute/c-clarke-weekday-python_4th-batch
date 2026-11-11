class Agent:

    no_of_agents: int = 0 #class variable

    def __init__(self, agent_id: str):
        self.id: str = agent_id #instance variable
        self.task: str = "default task"
        Agent.no_of_agents += 1

    def add_sub_agent_id(self, sub_agent_id):
        self.sub_id = sub_agent_id #Adding a new instance variable on a method
        print("Added the sub agent id")


agent1 = Agent(agent_id="001")
print(f"No of agents {agent1.no_of_agents}")
print(agent1.id)

print(agent1.sub_id)
# agent1.add_sub_agent_id("222")

print(agent1.__dict__)

if 'sub_id' in agent1.__dict__:
    print(agent1.sub_id)

if hasattr(agent1, 'sub_id'):
    print(agent1.sub_id)

agent2 = Agent(agent_id="002")
print(f"No of agents {agent1.no_of_agents}")

print(Agent.no_of_agents) #Accessing the class variable without an object
Agent.no_of_agents = 10

print(agent1.no_of_agents)
