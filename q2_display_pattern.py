#Displaying patterns

n=int(input("Enter n:"))
def display(n):
    for i in range (n):
        A=[]
        for j in range (n):
            if j<=i:
                A.append(j+1)
            else:
                if 10<=j+1<100:
                    A.append('  ')
                elif 100<=j+1<1000:
                    A.append('   ')
                else:
                    A.append(' ')
        A.reverse()
        for j in range(n-1):
            print(A[j], end=' ')
        print(1)

display(n)

