from Point import Point
import random

class SetOfPoints:
    """
    chua index cua tat cac cac diem co 
    """
    def __init__(self):
        """
        tap target va tap sensor la mot mang chua cac diem. arr<Point>

        """
        self.TargetPoint = []
        self.IntersectionPoint = []
        self.OtherPoint = []
        self.__Checker ={}
        self.Sensor = []
        self.Trange = 0 
        self.Srange = 0
    
    def __set_checker(self):
        for i in range(len(self.TargetPoint)):
            self.__Checker[i] = 0

        
    
    def _get_targetPoint(self):
        return self.TargetPoint
    
    def _set_Sensor(self,arr):
        for p in arr:
            point = Point(p[0],p[1])
            self.Sensor.append(point)
    
    def _display(self,t):
        S = [] 
        if t == "sensor":
            S = self.Sensor
        elif t == "target":
            S = self.TargetPoint
        elif t == "intersection":
            S = self.IntersectionPoint
        elif t == "other":
            S = self.OtherPoint
        else:
            return -1
        for p in S:
            p.displayPoint()
            print()
        return 1

    def _set_targetPoint(self,arr):
        """
        yeu cau da doc arr tu file sau do nhet target vao arr 
        """
        for p in arr:
            point = Point(p[0],p[1])
            self.TargetPoint.append(point)

    def _get_sensor_point(self):
        return self.Sensor  
    
    def _get_intersectionPoint(self):
        return self.IntersectionPoint
    
    def _get_two_points(self,X,Y):
        a, b, c = X._get_ptdt(Y)
        x0, y0 = X._get_td(Y)
        k = X._get_square_distance(Y)
        if k > 4 * X.SensingRange**2:
            return -1
        elif k == 4 * X.SensingRange**2:
            P1 = Point(x0,y0)
            self.IntersectionPoint.append(P1)
            X.Intersect.append(P1)
            Y.Intersect.append(P1)
            return 1
        else:
            if a != 0:
                A = (b/a)**2+1
                B = 2*(b/a)*(x0+c/a)-2*y0
                C = (c/a+x0)**2+y0**2-X.SensingRange**2+k/4
                y1, y2 = X._solve_ptb2(A,B,C)
                x1, x2 = (-c-b*y1)/a, (-c-b*y2)/a
                P1 = Point(x1,y1)
                P2 = Point(x2,y2)
                X.Intersect.append(P1)
                X.Intersect.append(P2)
                Y.Intersect.append(P1)
                Y.Intersect.append(P2)
                self.IntersectionPoint.append(P1)
                self.IntersectionPoint.append(P2)
                
            else:
                if b != 0:
                    A = 1
                    B = -2*x0
                    C = x0*x0+(c/b+y0)**2-X.SensingRange**2-k/4
                    x1, x2 = X._solve_ptb2(A,B,C)
                    P1 = Point(x1,-c/b)
                    P2 = Point(x2,-c/b)
                    self.IntersectionPoint.append(P1)
                    self.IntersectionPoint.append(P2)
                    X.Intersect.append(P1)
                    X.Intersect.append(P2)
                    Y.Intersect.append(P1)
                    Y.Intersect.append(P2)
            return 1  
    
    
    def _set_intersectionPoint(self):
        for i in range(len(self._get_targetPoint())-1):
            for j in range(i+1,len(self._get_targetPoint())):
                self._get_two_points(self.TargetPoint[i],self.TargetPoint[j])
    
    def _set_other_point(self):
        for point in self._get_sensor_point():
            for target in self._get_targetPoint():
                a,b,c= point._get_ptdt(target)
                x0, y0 = target.getX(),target.getY()
                if a != 0:
                    A = (b/a)**2+1
                    B = 2*(b/a)*(x0+c/a)-2*y0
                    C = (c/a+x0)**2+y0**2-target.SensingRange**2
                    y1, y2 = target._solve_ptb2(A,B,C)
                    if (y1-point.getY())*(y1-target.getY()) < 0:
                        x = (-c-b*y1)/a
                        P = Point(x,y1)
                        point.Intersect.append(P)
                        target.Intersect.append(P)
                        self.OtherPoint.append(P)
                    else:
                        x = (-c-b*y2)/a
                        P = Point(x,y2)
                        point.Intersect.append(P)
                        target.Intersect.append(P)
                        self.OtherPoint.append(P)
                
                else:
                    if b != 0:
                        A = 1
                        B = -2*x0
                        C = x0*x0+(c/b+y0)**2-target.SensingRange**2
                        x1, x2 = target._solve_ptb2(A,B,C)
                        if (x1-point.getX())*(x1-target.getX()) < 0:
                            P = Point(x1,-c/b)
                            self.OtherPoint.append(P)
                            point.Intersect.append(P)
                            target.Intersect.append(P)
                        else:
                            P = Point(x2,-c/b)
                            self.OtherPoint.append(P)
                            point.Intersect.append(P)
                            target.Intersect.append(P)
        return 0
    
    def _get_other_point(self):
        return self.OtherPoint


        