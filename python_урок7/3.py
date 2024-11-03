"""
print("привет")
try:
    print(2/0)
except ZeroDivisionError :
    print("не делтса на 0 ")
except:
    print("setbgsffb")
print("sgfnsngf")
print("sfdfhs")



print("salom")
try:
    print(x)
except ZeroDivisionError:
    print("erorr")
except NameError :
    print("nsnnpkwkenpkknwner")

"""


def number(n):
    for i in range(n):
        try:
            a = int(input("Введите число: "))
        except ValueError :
            print("Ошибка: Введите корректное число.")
    return a 
       
l=number(int (input("n ")))
print(l)




def data(a:list ,s:int):
    try:
        d = a[s]
        print(s, " malumot ",d)
    except IndexError:
        print("ashibka")

m = [1,2,3,4,56,7,7]
f = int(input("f "))
data(m,f)