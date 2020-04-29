import matplotlib.pyplot as plt
import numpy as np

maxMeter = 250 #m 
speed = 5 #m/s
carryingAmount = 9375 #Mbit -> 75GB -> 75000MB -> 9375Mbit


meter = []
mbits = []
mbitsConst = []

for currentMeter in range(25,maxMeter): 
    time = float(currentMeter / speed)
    meter.append(currentMeter)
    currentMbit = float(carryingAmount / time) 
    mbits.append(currentMbit)
    mbitsConst.append(300)

print(meter)
print(mbits, sep='\n')


plt.plot(meter, mbits)
plt.plot(meter, mbitsConst)
plt.ylabel('Mbits/s')
plt.xlabel('Distance in meter')
plt.show()

