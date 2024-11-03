import random as r 
import os; os .system("cls")
x = r.randint(0,15)
print(x)

print(r.randrange(0,19,2))
print(r.randrange(10,-10,-1))
print(r.randrange(0,19))

ls = [1,2,3,4,5,6,7,8,9,10]
print(ls)
r.shuffle(ls)
print(ls)

t = r.choice(ls)
print(t)
