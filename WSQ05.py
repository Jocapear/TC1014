f = float(input("Give me your temperature in F°"))
c = float(5 * (f - 32)/9)
print(f,"F° is equivalent to ",c,"C°.")
if(c>99):
    print("Water will boil at ",c,"C°.")
else:
    print("Water will NOT boil at ",c,"C°.")
