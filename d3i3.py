from math import copysign
from copy import copy

colors = {
    0 : ['w', 'white'],
    1 : ['g', 'green'],
    2 : ['r', 'red'],
    3 : ['b', 'blue'],
    4 : ['o', 'orange'],
    5 : ['y', 'yellow']
}

class Rubiks:
    adjs = (
        ((1, ((0, 0), (1, 0), (2, 0))), (4, ((0, 0), (1, 0), (2, 0))), (3, ((0, 0), (1, 0), (2, 0))), (2, ((0, 0), (1, 0), (2, 0)))),
        ()
    )
    def __init__(self):
        self.state = None
        self.setupState()
    def setupState(self):
        self.state = [[[None]*3 for i in range(3)] for i in range(6)]

        for f in range(len(self.state)):
            for x in range(len(self.state[f])):
                for y in range(len(self.state[f][x])):
                    self.state[f][x][y] = f
    def rotate(self, f):
        nCube = copy(self)
        for a in range(len(self.adjs[f])):
            nCube.state[self.adjs[a][0]][self.adjs[a][1][0][0]][self.adjs[a][1][0][1]] = 1#self.state[self.adjs[a][0]][self.adjs[a][1][0][0]][self.adjs[a][1][0][1]]
            #nCube.state[a[0]][a[1][0][0]][a[1][0][1]] = self.state[a[-1]][a[1][0][0]][a[1][0][1]]
            #nCube.state[a[0]][a[1][0][0]][a[1][0][1]] = self.state[a[-1]][a[1][0][0]][a[1][0][1]]

        self = nCube 

if __name__ == "__main__":
    cube = Rubiks()

    print(cube.state)
    cube.rotate(0)
    print(cube.state)