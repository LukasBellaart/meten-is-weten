varA = int(input("Wat is a? -> "))
varB = int(input("Wat is b? -> "))

if varA > varB:
    max = str(varA)
    min = str(varB)
    print("a is het grootste getal: "+ max)
elif varA < varB:
    min = str(varA)
    max = str(varB)
    print("a is het kleinste getal: "+min)
elif varA == varB:
    min, max = str(varA), str(varB)
    print("a en b zijn even groot")

print('Het minimum is:', min)
print("Het maximum is:", max)