x = int(input("write a number"))
def babylonian(a):
    if (a == 0):
        return 0
    r1 = a
    r2 = 0
    while (r2 != r1):
        r2 = r1
        r1 = (r1 + (a/r1))/2
    return r1
print (babylonian(x))
