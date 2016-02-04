#Converting milliseconds to hours, minutes, and seconds

def convert_ms(n):
    a.append(n%(1000*60)//1000)
    a.append(':')
    a.append(n%(1000*60*60)//1000//60)
    a.append(':')
    a.append(n//1000//60//60)
    return(a)

n=int(input("Enter seconds:"))
a=[]
convert_ms(n)
a.reverse()
for i in range(4):
    print(a[i],end='')
print(a[4])
