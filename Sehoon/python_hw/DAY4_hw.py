# Q-두수의 최소공배수를 구하는 함수
# def L(a,b):
#     for i in range(max(a,b),(a*b)+1):
#         if i%a==0 and i%b==0:
#             print(i)
#             break
# L(12,60)
# def GCD(a,b,c):
#     for i in range(min(a,b,c),0,-1):
#         if a%i==0 and b%i==0 and c%i==0:
#             return print(i)
# GCD(4,6,10)
# GCD(10,15,20)
def LCM(a,b,c):
    for i in range(min(a,b,c),0,-1):
        if a%i==0 and b%i==0 and c%i==0:
            return print(i)
LCM(4,6,10)
LCM(10,15,20)