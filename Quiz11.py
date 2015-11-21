#1
def calculate_e(precision):
    counter = 1
    accumulative = 1
    variable = 1
    while True:
        accumulative += variable*(1/counter)
        variable = (1/counter)*variable
        new = accumulative + variable*(1/counter)
        if (new - accumulative) < precision:
            break
        counter += 1
    return accumulative
print (calculate_e(.0005)) #modify the parameter as you wish

#2
def process_file(filename):
    name = open(filename)
    content = name.read()
    list = content.split(" ")
    print (list)
    counter = 0
    for i in list:
        if i.lower() == "banana":
            counter += 1
    print (counter)
process_file("file.txt") #there must be a file called like this, or you write your own if you wish

