class Shape: 
    def __init__(self): 
        self.number_of_sides = 0
        
    def describe(self): 
        return "this shape has " + str(self.number_of_sides) + " sides."

# This class displays inheritance from Shape
class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.number_of_sides = 3    

s = Shape()
print(s.describe())

t= Triangle()
print(t.describe()) # this shape has 3 sides.