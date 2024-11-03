n = open("file1.txt", "r")
a = n.read()  

# Разбиваем текст на слова
s = a.split()

# хранения длинного и короткого слов
d = ''
f= s[0] 

# Проходим по всем словам
for i in s:
    # самого длинного
    if len(i) > len(d):
        d = i
    # самого короткого
    if len(i) < len(f):
        f = i

n.close()

print(f"Самое длинное слово: {d}")
print(f"Самое короткое слово: {f}")



#==========================================

l,r,e=[],[],[]
for j in s:
   l.extend(j.split(" , "))

for j in r:
    e.extend(j.split())

nat = sorted(e,key= len)
print(nat[0],"\n",nat[-1])

n.close()