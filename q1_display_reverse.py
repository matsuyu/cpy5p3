#Displaying an integer reversed

def reverse(a):
    n=0
    while a>=10:
        n=(n*10)+(a%10)
        a=a//10
    n=n*10+a
    print(n)

a=int(input("Enter the integer:"))
reverse (a)

