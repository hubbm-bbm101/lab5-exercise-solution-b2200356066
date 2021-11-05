N=int(input("Write a N number: "))
i=0 
y=0
for x in range(1,N+1):  
    if x%2==0:
        i+=x
    else:
        y+=x
if N%2==0:        
    print(f"Average of an even numbers:{i/(N/2)}")
else:
    print(f"Average of an even numbers:{i/((N-1)/2)}")
print(f"Sum of odd functions:{y}")