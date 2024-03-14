class Cat:
    name=input("Please enter cat name:")
    age=int(input("Please enter cat age:"))
    
    def __init__(self,name,age):
      self.name=name
      self.age=age
      

    def info(self):
        print(f" I am a cat.My name is {self.name}.I am {self.age} years old.")
        
    def make_sound(self):
        print("Meow")
        

cat1= Cat
cat2=Cat

cat1.info()
cat1.make_sound()

cat2.info()
cat2.make_sound()
    