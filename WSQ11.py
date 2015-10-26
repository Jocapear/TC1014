lower = int(input("Write the first number of your range"))
upper = int(input("Write the last number of your range"))
palindrome = 0
transformed = 0
lychrel = 0
List=[]
for i in range (lower,upper+1):
    List.append(i)
print (List)
for i in List:
    x = i
    x = str(x)
    reverse = x[::-1]
    if  x == reverse:
        palindrome += 1
    else:
        counter = 0
        while x != reverse and counter != 30:
            x = int(x)
            reverse = int(reverse)

            x = x + reverse
            
            x = str(x)
            reverse = x[::-1]
            
            if x == reverse:
                transformed += 1
            counter += 1
            
        if x != reverse and counter >= 30:
            print (i+1,"is Lychrel")
            lycherel += 1
                
print ("Range size:",len(List))
print ("Natural palindromes: ",palindrome)
print ("Become palindromes: ",transformed)
print ("Lychrel candidates: ", lychrel)
