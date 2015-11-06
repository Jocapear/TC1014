x = int(input("Write one number"))
y = int(input("Write anotehr numeber"))
def gdc(a,b):
    if a > b and a%b == 0:
        return b
    elif a > b and a%b != 0:
        while a%b != 0:
            c = a%b
            a = b
            b = c
        return c
    elif b > a  and b%a == 0:
        return a
    elif b > a and b%a != 0:
        while b%a != 0:
            c = b%a
            b = a
            a = c
        return c
print("The Greatest common divisor of",x,"and",y,"is",gdc(x,y))
