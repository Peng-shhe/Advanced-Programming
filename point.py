class Point:
    #Constructor构造函数，完成初始化操作
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'x = %0.2f,y = %0.2f'%\
            (self.x,self.y)


p = Point(3,4)
print(p)
