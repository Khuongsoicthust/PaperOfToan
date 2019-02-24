import math
class Point:
    def __init__(self,x,y):
        self.setX(x)
        self.setY(y)
        self.SensingRange = 2
        self.Intersect = []

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def displayPoint(self):
        print("Toa do x: ",self.x,"----Toa do y: ",self.y)
    
    def _get_square_distance(self,P):
        d = (self.getX()-P.getX())**2 + (self.getY()-P.getY())**2
        return d
    
    def _get_ptdt(self,Y):
        a = Y.getY()-self.getY()
        b = self.getX()-Y.getX()
        c = self.getX()*(self.getY()-Y.getY())+self.getY()*(Y.getX()-self.getX())
        #print("phuong trinh duong thang di qua 2 diem do la: ",a,"x + ",b,"y + ",c," = 0")
        return a, b, c

    def _get_tt(self,Y):
        a = self.getX() - Y.getX()
        b = self.getY() - Y.getY()
        c = -1 * a * (self.getX()+Y.getX())/2 + -1 * b * (self.getY()+Y.getY())/2
        #print("phuong trinh duong thang di qua 2 diem do la: ",a,"x + ",b,"y + ",c," = 0")
        return a, b, c
    
    def _solve_ptb2(self,a,b,c):
        delta = b*b - 4*a*c
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1, x2
    
    def _get_td(self,Y):
        a = (self.getX()+Y.getX())/2
        b = (self.getY()+Y.getY())/2
        return a, b
    
