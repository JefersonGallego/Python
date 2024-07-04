


class Point2D:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f'({self.x},{self.y})'

    @classmethod
    def zero(cls):
        return cls(0,0)

class Point3D(Point2D):
     
     def __init__(self,x,y,z):
         super().__init__(x,y)
         self.z=z
    
     def __str__(self):
         return super().__str__()[0:-1] + f',{self.z})'

p1=Point2D(4,5)
print(p1)

p2=Point3D(4,-57,4)
print(p2)

p3=Point2D.zero()
print(p3)