n=int(input("Enter the n valve:"))
count=0
for i in range(2,n):
 if n%i==0:
        count=count+1
        break
if count==0:
    print("Prime number")
else:
        print("Not a prime number")

