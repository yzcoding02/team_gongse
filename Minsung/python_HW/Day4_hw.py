# def L(a,b):
#     for i in range(max(a,b),(a*b)+1):
#         if i%a==0 and i%b==0:
#                 return print(i)
# L(3,4)
# L(12,60)

def GCD(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return print(i)
GCD(4,6)
GCD(10,20)

def GCD2(a,b,c):
    for i in range(min(a,b,c),0,-1):
        if a%i==0 and b%i==0 and c%i==0:
            return print(i)
GCD2(2,4,6)
