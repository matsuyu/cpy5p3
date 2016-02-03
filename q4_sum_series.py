#Summing series

def m_series(i):
    sum=0
    for j in range (1,i+1):
        sum=sum+(j)/(j+1)
    print("{0:<15}{1:<15.4f}".format(i,sum))

print("{0:15}{1:15}".format("i","m(i)"))
for i in range(1,21):
    m_series(i)
