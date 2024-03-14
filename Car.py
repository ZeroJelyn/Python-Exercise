class Car:
      def __init__(self,color,size,model):
          self.color=color
          self.size=size
          self.model=model
          self.speed=0
                
      def info(self):
         print(f" My new car color is {self.color}.The car model is {self.model} and the size {self.model}.The speed of the car is {self.speed}.The speed og the car is")
        
        
car1=Car("red","Toyota","small")
car2=Car("blue","Myvi","medium")

car1.info()
car2.info()

