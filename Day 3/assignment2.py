
print("Code to find Sum of n natural numbers")
n=int(input("Enter a number: "))

sum=0
i=1
while(i<=n):
    sum=i+sum
    i=i+1
    
print(f"The sum of first {n} natural numbers is {sum}")
