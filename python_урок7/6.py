import random
n = open("file2.txt", "w")
for i in  n:
a = random.randint(1, 100)
n.write(str(a))

z = open("file2.txt", "r")
z = n.read()
n.close()
