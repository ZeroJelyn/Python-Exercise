class Motorcycle:
     def __init__(self,Age,model,color):
         
         self.age=Age
         self.model=model
         self.color=color
         
     def show(self):
        print("A very nice motorcycle with color of {self.color}. Age:{self.age}. Model:{self.model}.")
        
     def greet(self):
            if self.age>10:
                print("The motorcycle is very old,consider buying the new one.")
            else:
                print("Enjoy your ride!")   

my_motorcycle=Motorcycle(color="Gold",Age=4,model="EX5")
my_motorcycle.show()
my_motorcycle.greet() 
