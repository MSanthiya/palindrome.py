x=int(input("Enter the number: "))
k=0
for i in range(2,x//2+1):
    if(x%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number is not prime")
