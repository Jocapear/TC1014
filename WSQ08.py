x = int(input("Write the first number"))
y = int(input("Write the second number"))
def op1 (a,b):
    return a + b
def op2 (a,b):
    return a - b
def op3 (a,b):
    return a * b
def op4 (a,b):
    return a / b
def op5 (a,b):
    return a%b
print("The sum of ",x," and ",y," is ",op1(x,y))
print(x," minus ",y," is ",op2(x,y))
print("The product of ",x," and ",y," is ",op3(x,y))
print("The division of ",x," and ",y," is ",op4(x,y))
print("The remainder of ",x," and ",y," is ",op5(x,y))
