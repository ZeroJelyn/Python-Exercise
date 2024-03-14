class Tiger:
    def __init__(self,name,species,color):
        self.color=color
        self.name=name
     
    def info(self):
        print(f" My tiger name is {self.name}. My tiger colour is {self.color}.")
        
    def attack(self): 
        print(f"{self.name} pounces on its prey!")
        
tiger1=Tiger("bubu","pink")
tiger2=Tiger("Baba","Orange")

tiger1.info()
tiger2.info()     

tiger1.attack()
tiger2.attack()   