import numpy as np

class Rubiks:

    def __init__(self):
        self.state = None
        self.setupState()
    
    def setupState(self):
        self.state = {}
        c = 0
        for f in ['-2,{},{},{}', '{},-2,{},{}', '{},{},-2,{}', '{},{},{},-2', '+2,{},{},{}', '{},+2,{},{}', '{},{},+2,{}', '{},{},{},+2']:
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    for k in (-1, 0, 1):
                        di = f.format(i, j, k)
                        self.state[di] = c

            c += 1

    def rotate(self, rotInfo):
        pass

if __name__ == "__main__":
    cube = Rubiks()
    print(cube.state)