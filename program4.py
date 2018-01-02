import math

class Point(object):

    def __init__(self,x,y):
        
        self.x = x
        self.y = y

    def distance(self,other):
        # type: (object) -> object
        
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5


class Polygon:
    
    def __init__(self):
        
        self.vertice = []

    def add_point(self,point):
        
        self.vertice.append((point))
        return self.vertice

    def perimeter(self):
        
        perimeter = 0
        points =self.vertice+[self.vertice[0]]
        for i in range(len(self.vertice)):
            perimeter += points[i].distance(points[i+1])
        return perimeter




poly = Polygon()

poly.add_point(Point(1,1))
poly.add_point(Point(1,2))
poly.add_point(Point(2,2))
poly.add_point(Point(2,1))

print(poly.perimeter())
print(poly.shape())


