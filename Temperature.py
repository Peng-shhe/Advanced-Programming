class Temperature:
    #init:initialize初始化
    def __init__(self):
        self.value = 36 #摄氏度Celcius
    
    def getKelvin(self):
        value_kelvin = self.value + 273
        return value_kelvin
    
    def setValue(self,value_new):
        if value_new < -273:
            raise Exception
        else:
            self.value = value_new

temperature_classroom = Temperature()
#temperature_classroom.value = -2800 #直接更改，跳过setValue方法，不会报错，但值会异常
temperature_classroom.setValue(-2800)#通过setValue方法设置值，会正常报错
print(temperature_classroom.getKelvin())