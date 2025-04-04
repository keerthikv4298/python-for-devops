import sys

def add(n1,n2):
    result = n1+n2
    return result

def sub(n1,n2):
    result = n1-n2
    return result
def mult(n1,n2):
    result= n1*n2
    return result
#command line arguments , we can use sys module 
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
operation = sys.argv[3]

if operation == "add":
    output = add(n1,n2)
    print(output)
elif (operation =="sub"):
    output = sub(n1,n2)
    print(output)
else:
    output = mult(n1,n2)
    print(output)
import os
#for environmental variable we can use os module
print(os.getenv("passwordcalc"))
