from math import copysign

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
        self.state = [[[None]*5 for x in range(5)] for x in range(5)]

        #top
        def face(f):
            for i in range(3):
                for j in range(3):
                    pass
        #top
        face((0, -1, 0))
    def rotate(self, ins):
        pass

if __name__ == "__main__":
    cube = Rubiks()

    print(cube.state)