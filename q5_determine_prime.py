#Prime number

def is_prime(j):
    prime=True
    for i in range(2,j-1):
        if j%i==0:
            prime=False
    return(prime)

l=1
n=0
A=[]
for j in range(1,1000):
    if is_prime(j)==True:
        A.append(j)
        n=n+1
for k in range(n):
    if l<10:
        print("{0:<5}".format(A[k]),end='')
        l+=1
    else:
        print("{0:<5}".format(A[k]))
        l=1
              
