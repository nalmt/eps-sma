# TP1 SMA 
# 13/10/20

from enum import Enum
import random

class Goal(Enum):
    S = 0
    A = 1
    B = 2
    C = 3
    D = 4

class Environment:

    plot_0 = []
    plot_1 = []
    plot_2 = []
    
    def who_is_up():

    def who_is_down():

    def add_agent_to_plot(plot, agent):
        if plot == 0:
            plot_0.add(agent)
        elif plot == 1:
            plot_1.add(agent)
        elif plot == 2:
            plot_2.add(agent)
        else:

def setup(environment, agents):
    # mettre les agents au hasard
    # dans un plot
    for agent in agents:
        r = random.randint(0, 2)
        environment.add_agent_to_plot(r, agent)


# agents: blocs A, B, C, D

# état initial : aléatoire

# état final : top -> A, B, C, D -> bottom

class Agent:
    
    def __init__(self, goal): 
        self.goal =  goal
        self.second = s 

    def move():

    def push():

    def is_free():
        # appel à Environment.who_is_up

    def is_sat():
        # appel à Environment.who_is_up

    def do():
        if not is_sat():
            if is_free():
                move()
            else:
                push()


def schedule(agents):

    # itérer en boucle sur les agents
    for agent in agents:


def main():
    environment = Environment()
    a = Agent(Goal.S)
    b = Agent(Goal.A)
    c = Agent(Goal.B)
    d = Agent(Goal.D)

    # choisir l'ordre d'itération des agents
    agents = [a, b, c, d]

    setup(environment, agents)
    

    schedule(agents)

if __name__ == "__main__":
    main()
