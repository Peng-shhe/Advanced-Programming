class Circle:
    def __init__(self):
        #成员变量 member variables
        self.radius = None
        self.x = None
        self.y = None
        pass
    
    def setRadius(self,new_radius):
        if new_radius < 0:
            raise Exception
        else:
            self.radius = new_radius
    
    def setSrc(self,new_x,new_y):
        if new_x is None or new_y is None:
            raise Exception
        else:
            self.x = new_x
            self.y = new_y
    
    def getC(self):
        c =2 * 3.1415926535897 * self.radius
        return c
    
    def getS(self):
        s = 3.1415926535897 * self.radius ** 2
        return s
    
circle_a = Circle()
circle_a.setRadius(5)
circle_a.setSrc(0,0)
print('C of circle_a = %0.2f'%(circle_a.getC()))
print('S of circle_a = %0.2f'%(circle_a.getS()))

circle_b = Circle()
circle_b.setRadius(15)
circle_b.setSrc(10,-2)
print('C of circle_b = %0.2f'%(circle_b.getC()))
print('S of circle_b = %0.2f'%(circle_b.getS()))