#!/usr/bin/env python3
# coding: utf-8
# TP1 SMA
# 13/10/20

from enum import Enum
import random
import time

plot_0 = []
plot_1 = []
plot_2 = []

plots = [plot_0, plot_1, plot_2]

def add_agent_to_plot(plot, agent):
    if plot == 0:
        plot_0.append(agent)
        agent.plot = 0
    elif plot == 1:
        plot_1.append(agent)
        agent.plot = 1
    elif plot == 2:
        plot_2.append(agent)
        agent.plot = 2
    else:
        print("add_agent_to_plot error !")

def setup(agents):
    # mettre les agents au hasard
    # dans un plot
    for agent in agents:
        r = random.randint(0, 2)
        add_agent_to_plot(r, agent)

    for agent in agents:
        update_state(agent)

def update_state(agent):
    if agent.is_sat():
        agent.state = 'satisfaction'

# agents: blocs A, B, C, D
# état initial : aléatoire
# état final : top -> A, B, C, D -> bottom
class Agent:
    
    def __init__(self, name, goal=None, plot=None):
        self.name = name
        self.goal = goal
        self.plot = plot
        self.state = None

    def possible_moves(self):
        possible_moves = [0, 1, 2]
        list(filter(lambda a: a != self.plot, possible_moves))
        return possible_moves

    def move(self):
        choice = random.choice(self.possible_moves())
        plots[self.plot].pop(self.get_index())
        plots[choice].append(self)
        self.plot = choice

    def push(self):
        plots[self.plot][self.get_index() + 1].state = 'fuite'

    def is_free(self):
        return self.who_is_up() == 0

    def is_sat(self):
        return self.who_is_down() == self.goal

    def get_index(self):
        return plots[self.plot].index(self)

    def who_is_up(self):
        index = self.get_index()
        if len(plots[self.plot]) > (index + 1):
            return plots[self.plot][index + 1].name
        else:
            return 0

    def who_is_down(self):
        index = self.get_index()
        if index > 0:
            return plots[self.plot][index - 1].name
        else:
            return 'S'

    def do(self):
        if self.state == None:
            if self.is_free():
                self.move()

                if self.is_sat():
                    self.state = 'satisfaction'
                else:
                    self.state = None
            else:
                self.push()
                self.state = 'agression'
        elif self.state == 'fuite':
            if self.is_free():
                self.move()
                if self.is_sat():
                    self.state = 'satisfaction'
                else:
                    self.state = None
            else:
                self.push()
                self.state = 'fuite'
        elif self.state == 'agression':
            if self.is_free():
                self.move()
                if self.is_sat():
                    self.state = 'satisfaction'
                else:
                    self.state = None
            else:
                self.push()
                self.state = 'agression'

def schedule(agents):

    while not all(agent.state == 'satisfaction' for agent in agents):
        for agent in agents:
            agent.do()
        display(agents)
        time.sleep(0.2)

def display(agents):
    p0 = []
    p1 = []
    p2 = []
    for agent in plot_0:
        p0.append(agent.name)
    for agent in plot_1:
        p1.append(agent.name)
    for agent in plot_2:
        p2.append(agent.name)

    print("plot 0: ", p0)
    print("plot 1: ", p1)
    print("plot 2: ", p2)

    for agent in agents:
        print(agent.name, agent.state)

    print("----------------------------------")

def main():
    s = Agent('S')
    a = Agent('A', 'S')
    b = Agent('B', 'A')
    c = Agent('C', 'B')
    d = Agent('D', 'C')

    # choisir l'ordre d'itération des agents
    agents = [a, b, c, d]
    # les agents sont placés au hasard
    setup(agents)

    print("##################################")
    print("état initial :")
    print("##################################")
    display(agents)
    schedule(agents)
    print("##################################")
    print("état final :")
    print("##################################")
    display(agents)

if __name__ == "__main__":
    main()