#Computing GCD

def gcd(a,b):
    if a>b:
        min=b
        max=a
    else:
        min=a
        max=b
    n=min
    while max%n!=0 or min%n!=0:
        n-=1
    return(n)

a=int(input("Enter integer A:"))
b=int(input("Enter integer B:"))
print(gcd(a,b))
