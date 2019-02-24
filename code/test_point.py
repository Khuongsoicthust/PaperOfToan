import Point 
import random

# tao mang arrX chua hoanh do cua diem, arrY chua tung do cua diem
#  

arrX = []
arrY = []
for i in range(50):
    arrX.append(random.randint(0,200))
    arrY.append(random.randint(0,200))

point1 = Point.Point(arrX[1],arrY[1])
point2 = Point.Point(arrX[2],arrY[2])

def _test_getX():
    if point1.getX() == arrX[1]:
        return True
    else:
        return False

def _test_getY():
    if point1.getY() == arrY[1]:
        return True
    else:
        return False

def _test_setX():
    k = random.randint(0,200)
    point1.setX(k)
    if point1.getX() == k:
        return True
    else:
        return False

def _test_setY():
    k = random.randint(0,200)
    point1.setY(k)
    if point1.getY() == k:
        return True
    else:
        return False

def _test_get_ptdt():
    a,b,c = point1._get_ptdt(point2)
    if a*point1.getX()+b*point1.getY()+c == 0 and a*point2.getX()+b*point2.getY()+c == 0:
        return True
    else:
        return False

def _test_get_td():
    a,b = point1._get_td(point2)
    if a*2 == point1.getX()+point2.getX() and b*2 == point1.getY()+point2.getY():
        return True
    else:
        return False

    