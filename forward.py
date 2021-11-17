import numpy as np
import math as m

jointlens = [2, 2, 2, 2]
startcoords = [0, 0]
startangles = [0, 0, 0, 0]
anglechanges = [45, 45, 45, 45]

for angle in range(len(anglechanges)):
    startangles[angle] = m.radians(startangles[angle])
    anglechanges[angle] = m.radians(anglechanges[angle])

class transformation:
    def __init__(self, jointlen, anglechange):
        self.jointlen = jointlen
        self.anglechange = anglechange
    def matrix(self):
        return np.matrix([[m.cos(self.anglechange), -m.sin(self.anglechange), self.jointlen],
                          [m.sin(self.anglechange), m.cos(self.anglechange), 0],
                          [0, 0, 1]])


transformations = []

for i in range(len(jointlens)):
    print(i)
    transformations.append(transformation(jointlens[i], anglechanges[i]))
    
output = np.array([
    [startcoords[0]],
    [startcoords[1]],
    [1]
    ])

for i in range(len(transformations)):
    output = np.matmul(transformations[i].matrix(), output)
    
print(output)