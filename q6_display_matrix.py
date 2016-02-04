#Displaying matrix of 0s and 1s

import random
n=int(input("Enter n:"))
a=[[0 for i in range (n)]for i in range(n)]
i=0
j=0
for i in range(n):
    for j in range(n):
        a[i][j]=random.randrange(0,2)
for i in range(n):
    for j in range(n-1):
        print(a[i][j], end=' ')
    print(a[i][j])
