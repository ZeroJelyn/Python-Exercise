import random
nmbr=random.randint(1,10)
print(nmbr)
      
r1=random.random()
print(r1)
      
r2=random.choice([1,2,3,4,5,6,7,8,9])
print(r2)
      
r3=random.randint(1,1800)
print(r3)

total=0
expense=[]
for i in range(5):
    expense.append(float(input("Enter a number:")))
    
total=sum(expense)
print("Total: ",total)

roll=random.randint(1,3)
print(roll)
if roll==1:
    loot="emas"


