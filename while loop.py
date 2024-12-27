for i in range(1000,1,-1):
    if i%2!=0:
        print(i)

odd_numbers =[i for i in range(1000,-1,-1)if i %2!=0]
print(odd_numbers)

k=1000
while k<=0:
    if k%2!=0:
        print(k)
    k-=1