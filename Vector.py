class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y 

    def distance_from_origin(self):
        d=(self.x**2 + self.y**2)**0.5
        return d

    def distance_form_another_vector(self, p,q):
        d=((self.x -p)**2 +(self.y -q)**2)**0.5
        return d

    def __str__(self):
        s='(' + str(self.x) + ',' +str(self.y)+ ')'
        return s

v= Vector(5,6)
print(v)
