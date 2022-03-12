# Read me
# Print nabopunkter i stedet for afstand
# Print number os dist calc
# Upload github

import math

class Point:
    def __init__(self, x, y, pos_Px, pos_Py, pos_QRx, pos_QRy):
        self.x = x
        self.y = y
        self.pos_Px = pos_Px
        self.pos_Py = pos_Py
        # self.pos_QRx = pos_QRx
        # self.pos_QRy = pos_QRy

def dist(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def minDist(P):
    m = 1000000
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            m = min(m, dist(P[j], P[i]))
    return(m)

def closestPair(Px, Py):
    N = len(Px)

    if N <= 3:
        return minDist(Px)

    # Construct Qx, Qy, Rx, Ry
    L = Px[math.floor(N/2)].x

    Qx = [] #venstre sorteret efter x
    Qy = [] #venstre sorteret efter y
    Rx = []
    Ry = []

    for i in range(N):
        # ith position in Px - add to Q or R
        if Px[i].x < L:
            Qx.append(Px[i])
        else:
            Rx.append(Px[i])
        # ith position in Py - add to Q or R
        if Py[i].x < L:
            Qy.append(Py[i])
        else:
            Ry.append(Py[i])

    for i in range(len(Qx)): #math.floor(N/2)
        Qx[i].pos_Px = i
        Qy[i].pos_Py = i
        Rx[i].pos_Px = i
        Ry[i].pos_Py = i

    # Hvert punkt i Q er nu i Qx og Qy
    dQ = closestPair(Qx, Qy)
    dR = closestPair(Rx, Ry)
    delta = min(dQ, dR)

    # Kombinér løsninger
    # Find punkt på x-akse, som deler punkterne i to lige store dele
    L = Qx[len(Qx) - 1].x

    # Find points in P where for all p dist(p, L) < delta
    Sy = []
    for i in range(len(Py)):
        if abs(Py[i].x - L) <= delta:
            Sy.append(Py[i])

    minS = 1000
    for i in range(len(Sy)):
        for j in range(i + 1, min(15, len(Sy))):
            minS = min (minS, dist(Sy[i], Sy[j]))

    return min(delta, minS)


# Read points
P = []
file = open("Input.txt","r")
line = file.readline()
while(line):
    l = [int(x) for x in line.split(" ")]
    p = Point(l[0], l[1], 0, 0, 0, 0)
    P.append(p)
    line = file.readline()
file.close()

N = len(P)

Px = sorted(P, key=lambda e: e.x)
Py = sorted(P, key=lambda e: e.y)

for i in range(N):
    Px[i].pos_Px = i
    Py[i].pos_Py = i

print("Closest pair ", closestPair(Px, Py))
