def gcd(a, b, c):
    for i in range(min(a,b,c),0,-1):
        if a%i==0 and b%i==0 and c%i==0:
            return print(i)
gcd(4,6,10)
gcd(10,20,30)