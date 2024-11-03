"""
def rek(a, s=0):
    if s == len(a):
        return
    if s < len(a):
        print(a[s])
        rek(a, s + 1)

n = ["Привет", "мир", "это", "рекурсия"]
rek(n)
"""
