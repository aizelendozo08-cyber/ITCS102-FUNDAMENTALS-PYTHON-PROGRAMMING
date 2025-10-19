#Make a Diamond using loops
print("\t\t *")
for b in range(2,10,1):
    for u in range(10,b,-1):
        print(" ",end=" ")
    for tm in range(1,b,1):
        print("*",end=" ")
    for hm in range(1,b,1):
        print("*",end=" ")
    print()
for me in range(1,10,1):
    for u in range(1,me,1):
        print(" ",end=" ")
    for tm in range(10,me,-1):
        print("*",end=" ")
    for hm in range(10,me,-1):
        print("*",end=" ")
    print()
print("\t\t *")