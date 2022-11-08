'''
Student: Valmir de Barros Pedro
Id: C0868075
CSD 1233 Python programming 

planing the class
object: CAR

1) Brand : 
2) Model : 
3) Color : 
4) Motorization : 
5) Horse Power :
6) acceleration 0 To 100 :
7) Autonomy :
8) price :

'''

'''
Creating class where  color and model is not  private.
'''
class Car:
    def __init__(self, brand, model, color, motorization, horsePower, accel0To100, autonomy, price):
        self.__brand = brand
        self.model = model
        self.color = color
        self.__motorization = motorization
        self.__horsePower = horsePower
        self.__accel0To100 = accel0To100
        self.__autonomy = autonomy
        self.__price = price

    def __str__(self):
        return f' The chosen car is from Brand: {self.__brand}\n Model: {self.model}\n the color is {self.color}\n Motorization: {self.__motorization}\n the horse power is {self.__horsePower} HP\n Acceleration: {self.__accel0To100} sec., with autonomy of {self.__autonomy} KM \n Total $ {self.__price}'
        


car1 = Car('Lucid','Lucid Air','Black','Electric',1200,3.8,830,121500)
car2 = Car('Tesla','Model3','White','Electric',480,6.7,438,60000)
car3 = Car('Ford','Mustang Mach 1','Gray','Combustion',470,6.8,17.1,74000)

