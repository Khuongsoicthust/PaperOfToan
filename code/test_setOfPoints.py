import SetOfPoints as sop 
import random
import matplotlib.pyplot as plt
tarX = []
tarY = []
senX, senY = [],[]
for i in range(1000):
    tarX.append(random.randint(0,200))
    tarY.append(random.randint(0,200))
    senY.append(random.randint(0,200))
    senX.append(random.randint(0,200))

sen,tar = [],[]
for i in range(1000):
    tar.append([tarX[i],tarY[i]])
    sen.append([senX[i],senY[i]])

points = sop.SetOfPoints()
points._set_Sensor(sen)
points._set_targetPoint(tar)
points._set_intersectionPoint()
def _plot_points(points):
    arrX,arrY = [],[]
    for point in points:
        arrX.append(point.getX())
        arrY.append(point.getY())
    plt.plot(arrX,arrY,"ro")
    plt.show()

def _plot_arr_points(arr):
    cl = ["bo","ro","go","co","mo","yo","ko","wo"]
    fig, ax = plt.subplots()
    for i in range(len(arr)):
        arrX,arrY = [],[]
        for point in arr[i]:
            arrX.append(point.getX())
            arrY.append(point.getY())

        plt.plot(arrX,arrY,cl[i%len(cl)])
        
