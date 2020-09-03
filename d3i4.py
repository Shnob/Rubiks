import numpy as np
from copy import copy
from math import copysign

class Rubiks:
    colors = {
        0 : ['w', 'white'],
        1 : ['g', 'green'],
        2 : ['r', 'red'],
        3 : ['b', 'blue'],
        4 : ['o', 'orange'],
        5 : ['y', 'yellow']
    }

    def __init__(self):
        self.state = None
        self.setupState()
    
    def setupState(self):
        self.state = {}
        c = 0
        for f in ['{},-2,{}', '{},{},2', '2,{},{}', '{},{},-2', '-2,{},{}', '{},2,{}']:
            for x in (-1, +0, +1):
                for y in (-1, 0, 1):
                    self.state[f.format(x, y)] = c
            c += 1

    def rotIns(self, x):
        for i in x.split():
            self.rotNot(i)

    def rotNot(self, x):
        rots = {
            "u" : ((1, -1), 1),
            "u'" : ((1, -1), 3),
            "l" : ((0, -1), 3),
            "l'" : ((0, -1), 1),
            "r" : ((0, 1), 1),
            "r'" : ((0, 1), 3),
            "d'" : ((1, 1), 1),
            "d" : ((1, 1), 3),
            "f" : ((2, 1), 1),
            "f'" : ((2, 1), 3),
            "b'" : ((2, -1), 1),
            "b" : ((2, -1), 3),

            "f2" : ((2, 1), 2),
            "l2" : ((0, -1), 2),
            "r2" : ((0, 1), 2),
            "b2" : ((2, -1), 2),
            "u2" : ((1, -1), 2),
            "d2" : ((1, 1), 2),
        }

        for i in range(rots[x.lower()][1]):
            self.rotate(rots[x.lower()][0])

    def rotate(self, info): #FACE NOTATION: Magnitude = index of axis (i.e: x:0, y:1, z:2). Which = which face on that axis. (i.e: (1,+1) = face centred on coords [0, +2, 0])
        face = info[0]
        which = info[1]

        axis = int(copysign(face, 1))

        nCube = copy(self.state)

        t = 0
        rot = None

        if axis == 0:
            rot = np.matrix([
                [1, 0, 0],
                [0, 0,-1],
                [0, 1, 0]
            ])
        elif axis == 1:
            rot = np.matrix([
                [0, 0,-1],
                [0, 1, 0],
                [1, 0, 0]
            ])
        else:
            rot = np.matrix([
                [0,-1, 0],
                [1, 0, 0],
                [0, 0, 1] # maybe should be [0, 0, 1] ???
            ])

        for p in self.state:
            coords = list(map(int, p.split(',')))
            if copysign(coords[axis], which) == coords[axis] and abs(coords[axis]) > 0:
                #print(coords)
                matCoords = np.matrix([[coords[0]], [coords[1]], [coords[2]]])
                #print(matCoords)
                newMatCoords = list(map(int, rot * matCoords))
                #print("{}       {}".format(coords, newMatCoords))
                newCoords = '{},{},{}'.format(newMatCoords[0], newMatCoords[1], newMatCoords[2])
                #print(newCoords)
                nCube[newCoords] = self.state[p]
        self.state = nCube

if __name__ == "__main__":
    cube = Rubiks()
    print(cube.state)
    cube.rotate(1, 1)
    print(cube.state)