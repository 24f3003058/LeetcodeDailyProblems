class Triangle:
    def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c 
    
    def Is_valid(self):
        if (self.x +self.y > self.z and self.x +self.z > self.y and self.y +self.z > self.x):
            return "Valid"
        else:
            return "Invalid"
    def Side_Classification(self):
        if self.Is_valid()=="Valid":
            if self.x==self.y==self.z:
                return "Equilateral"
            elif self.x==self.y or self.y==self.z or self.z==self.x:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Invalid"
    def Angle_Classification(self):
        if self.Is_valid()=="Valid":
            a,b,c=sorted([self.x,self.y,self.z])
            if (a*a +b*b) >c*c:
                return "Acute"
            elif (a*a +b*b)==c*c:
                return "Right"
            else:
                return "Obtuse"
        else:
            return "Invalid"
            
    def Area(self):
        if self.Is_valid()=="Valid":
            s=(self.x+self.y+self.z)/2
            area_sq=s*(s-self.x)*(s-self.y)*(s-self.z)
            area=area_sq**0.5
            return area
        else:
            return "Invalid"
  
