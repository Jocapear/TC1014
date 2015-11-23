def calculate_e(precision):
    counter = 1
    accumulative = 1
    variable = 1
    while counter != precision:
        accumulative += variable*(1/counter)
        variable = (1/counter)*variable
        counter += 1
    return accumulative
print (calculate_e(35))
