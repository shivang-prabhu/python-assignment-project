print("Code to check whether a number is prime or not")
a=int(input("Enter a number: "))
flag=""
if a==1 or a==2:
    print(f"The number {a} is prime")
elif a%2==0:
    print(f"The number {a} is not prime")
else:
    for i in range(3,a,2):
        flag=False
        if(a%i==0):
            flag=True
    if(flag==True):
        print(f"The number {a} is not prime")
    else:
        print(f"The number {a} is prime")
