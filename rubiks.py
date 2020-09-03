import pygame, sys
import d3i4
import numpy as np

mapp = lambda x, a, b, c, d : (x-a)/(b-a) * (d-c) + c

colors = [
    (255, 255, 255),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 128, 0),
    (255, 255, 0),
    (0, 0, 0)
]


b = 1/2.5
a = 1 - b

quadDic = {
    "-0" : ((a, -b, -b), (a, b, -b), (a, b, b), (a, -b, b)), #((a, -b, -b), (a, b, -b), (a, b, b), (a, -b, b))
    "-1" : ((-b, a, -b), (b, a, -b), (b, a, b), (-b, a, b)),
    "-2" : ((-b, -b, a), (b, -b, a), (b, b, a), (-b, b, a)),
    "+0" : ((-a, -b, -b), (-a, b, -b), (-a, b, b), (-a, -b, b)),
    "+1" : ((-b, -a, -b), (b, -a, -b), (b, -a, b), (-b, -a, b)),
    "+2" : ((-b, -b, -a), (b, -b, -a), (b, b, -a), (-b, b, -a))
}

del a
del b

def quad(coords):
    n = None
    if coords[0] == 2:
        n = "+0"
    elif coords[0] == -2:
        n = "-0"
    elif coords[1] == 2:
        n = "+1"
    elif coords[1] == -2:
        n = "-1"
    elif coords[2] == 2:
        n = "+2"
    elif coords[2] == -2:
        n = "-2"

    return quadDic[n]

def calcPoint(coords, dispInfo):

    point = np.matrix([
        [coords[0]],
        [coords[1]],
        [coords[2]]
    ])
    
    cx = np.cos(dispInfo[1][0]) # a
    sx = np.sin(dispInfo[1][0]) # b
    cy = np.cos(dispInfo[1][1]) # c
    sy = np.sin(dispInfo[1][1]) # d
    cz = np.cos(dispInfo[1][2]) # e
    sz = np.sin(dispInfo[1][2]) # f

    '''
    rot = np.matrix([
        [cy*cz, cy*(-sz), -sy],
        [cx*sz-(sx*sy*cz), cx*cz, (-sx)*cy],
        [sx*sz, (-sx)*sy*(-sz), cx*cy]
    ])
    '''
    
    rot = np.matrix([
        [cy*cz, -cy*sz, -sy],
        [cx*sz-(sx*sy*cz), cx*cz+sx*sy*sz, (-sx)*cy],
        [cz*cx*sy+sx*sz, cz*sx-cx*sy*sz, cx*cy]
    ])
    

    '''rot = np.matrix([
        [1, 0, 0],
        [0, cx, -sx],
        [0, sx, cx]
    ])'''

    point = rot * point

    d = 1/(dispInfo[0] - point.item(2))
    proj = np.matrix([
        [d, 0, 0],
        [0, d, 0]
    ])

    point = proj * point

    return ((point.item(0) * dispInfo[2], point.item(1) * dispInfo[2]), d)

def showPoint(screen, point):
    pos = (int(point[0] + screen.get_size()[0]/2), int(point[1] + screen.get_size()[1]/2))
    screen.set_at(pos, (255, 255, 255))

def showCircle(screen, point, size, c):
    #col = (255, 255, 255)
    col = colors[c]
    pos = (int(point[0] + screen.get_size()[0]/2), int(point[1] + screen.get_size()[1]/2))
    pygame.draw.circle(screen, col, pos, int(size))

def showPoly(screen, point, c):
    col = colors[c]
    pos = []
    for p in point:
        pos.append((int(p[0] + screen.get_size()[0]/2), int(p[1] + screen.get_size()[1]/2)))
    pygame.draw.polygon(screen, col, pos)

def renderCube(screen, cube, dispInfo):
    points = []
    for p in cube.state:
        info = [[], []]
        
        for c in range(4):
            coords = list(map(int, p.split(',')))
            '''
            if c < 2:
                coords[0] -= 1/2
                if c == 1 or c == 3:
                    coords[1] -= 1/2
                else:
                    coords[1] += 1/2
            else:
                coords[0] += 1/2
                if c == 0 or c == 2:
                    coords[1] -= 1/2
                else:
                    coords[1] += 1/2
            '''
            q = quad(coords)

            coords[0] += q[c][0]
            coords[1] += q[c][1]
            coords[2] += q[c][2]
            
            cal = calcPoint(coords, dispInfo)
            info[0].append(cal[0])
            info[1].append(cal[1])
        info[1] = (info[1][0] + info[1][1] + info[1][2] + info[1][3]) / 4
        points.append((info[0], cube.state[p], info[1]))

    points.sort(key = lambda x : x[2])
    
    for i in range(len(points)):
        showPoly(screen, points[i][0], points[i][1])
        #showCircle(screen, points[i][0], 1 + 150 * points[i][2], 6)
        #showCircle(screen, points[i][0], 150 * points[i][2], points[i][1])

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Rubiks")
    screen = pygame.display.set_mode((500, 500))

    cube = d3i4.Rubiks()

    #cube.rotNot("f")
    #cube.rotIns("U2 L U F' D U B' R' F2 U")
    #cube.rotIns("F L R2")


    dispInfo = [8, [0, 0, 0], 600]
    targDisp = [0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #print(event.unicode)
                keys = {
                    'w' : "u",
                    'W' : "u'",
                    's' : "d",
                    'S' : "d'",
                    'd' : "r",
                    'D' : "r'",
                    'a' : "l",
                    'A' : "l'",
                    'q' : "b",
                    'Q' : "b'",
                    'e' : "f",
                    'E' : "f'"
                }
                if event.unicode in keys:
                    cube.rotNot(keys[event.unicode])

        targDisp[0] = mapp(pygame.mouse.get_pos()[0], 0, screen.get_size()[0], np.pi, -np.pi)
        targDisp[1] = mapp(pygame.mouse.get_pos()[1], 0, screen.get_size()[1], np.pi, -np.pi)

        d = np.interp

        dispInfo[1][1] = targDisp[0]
        dispInfo[1][0] = targDisp[1]

        screen.fill((0, 0, 0))

        #p = calcPoint((0, 0, 0), dispInfo)
        #showCircle(screen, p, 10)

        #dispInfo[1][0] += 0.001

        renderCube(screen, cube, dispInfo)

        pygame.display.update()