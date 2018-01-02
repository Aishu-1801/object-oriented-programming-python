class coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def distance(self,other):
        # type: (object) -> object
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5

c = coordinate(3,5)
origin = coordinate(0,0)

print(coordinate.distance(c,origin)) #distance is a method of coordinate calling object c and origin
print(c.distance(origin)) #it is the same as the above
print(c.__str__())