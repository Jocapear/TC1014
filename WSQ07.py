num1 = int(input("Give me the first number"))
num2 = int(input("Give me the second number"))
counter = 0
collector = num1
while collector < num2:
    counter = counter + collector 
    collector = collector + 1
print ("The sum of the numbers from ",num1," to ",num2," is: ",counter+num2,)
    
