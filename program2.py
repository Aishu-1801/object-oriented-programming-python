class student(object):
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def __str__(self):
        return str(self.name) + ',' + str(self.age)

vamshi = student('vamshi',22)

print(vamshi)