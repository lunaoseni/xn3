# для писма ============================================================== 

f = open("file.txt","wt")
f.write("перви код в фацле ")
print("\nдание написни в файл")
f.close()


f = open("file.txt","at")
ls = ["\nземля ","\nсолнични система ","\nгалактика ","\nвселени ","\nмулти вселени "]
f.writable(ls)
print("\nдание написни в файл")
f.close()


f = open("file.txt","a")
for i in range(10):
    f.write(f"{i}")
print("\nдание написни в файл")
f.close()


# для чтение ==============================================================

f = open("file.txt","r")
if  f.readable() :
    print("разришение ")
else :
    print("запрешон ")

d = f.read()
print(d)
f.close()


f = open("file.txt","r")
if  f.readable() :
    print("разришение ")
else :
    print("запрешон ")
for i in f :
    print(i,end="")
f.close()


f = open("file.txt","r")
if  f.readable() :
    print("разришение ")
else :
    print("запрешон ")

d = f.readline
print(d)
f.close()


f = open("file.txt","r")
if  f.readable() :
    print("разришение ")
else :
    print("запрешон ")

d = f.readline()
print(d)
print(len(d))
f.close()


f = open("file.txt","r")
if  f.readable() :
    print("разришение ")
else :
    print("запрешон ")

d = f.read()
print(d)
f.seek(0,0)
b = f.readline()
print(b)
f.seek(0,2)
f.close()