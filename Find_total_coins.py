x=[1,2,5]
x.sort(reverse=True)
num=int(input("Enter any Amount"))
coins=0
i=0
while num:
    high=x[i]
    coins=coins+num//high
    num=num%high
    i=i+1
print(coins)
