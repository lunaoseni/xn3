n = open("латин.txt","w")
n.write("#include<iosteram>int main () { return 0; }")
n.close()

n = open("латин.txt","r")
a = n.read()
n.close()

s = len(a)

print(s)