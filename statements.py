a = int(input(" enter number = "))
b = int(input(" enter number = "))
c = int(input(" enter number = "))

if(a>b and a>c):
    print("a is the largest")
elif(b>a and b>c):
    print("b is the largest")
elif(c>a and c>b):
    print("c is the largest")
else:
    print("end")           