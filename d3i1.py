import pygame, sys
from math import copysign

pygame.init()

colors = {
    0 : ['w', 'white'],
    1 : ['g', 'green'],
    2 : ['r', 'red'],
    3 : ['b', 'blue'],
    4 : ['o', 'orange'],
    5 : ['y', 'yellow']
}

class Rubiks:
    def __init__(self):
        self.state = None
        self.setupState()
    def setupState(self):
        self.state = {
            '0-0': None,
            '00+': None,
            '0+0': None,
            '00-': None,
            '-00': None,
            '0+0': None
        }
        n = 0
        for i in self.state:
            self.state[i] = []

            for j in range(3):
                self.state[i].append([])
                for k in range(3):
                    self.state[i][j].append(colors[n][0])

            n += 1
            
        

if __name__ == "__main__":
    cube = Rubiks()

    print(cube.state)