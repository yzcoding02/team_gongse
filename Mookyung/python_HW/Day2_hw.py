# 1. 1~10중의 홀수만을 구하시오.
# for i in range (1,11):
#     if i%2==1:
#         print(i)

# 2. 1~10중의 3의 배수가 아닌 것만 구하시오.
# for i in range (1,11):
#     if i%3!=0:
#         print(i)

# 3. 50~100중의 3과 4의 공배수만 구하시오.
# for i in range (50,101):
#     if i%3==0:
#         if i%4==0:
#             print(i)

# 4. 1~20중의 7의 배수들의 곱을 구하시오.
# a=1
# for i in range (1,21):
#     if i%7==0:
#         a*=i
# print(a)

# 5. 50~60중의 4의 배수의 곱을 구하시오.
# a=0
# for i in range (50,61):
#     if i%4!=0:
#         a+=i
# print(a)

# 6. 1~100중의 짝수와 홀수의 곱을 구하시오.
a=0
b=0
for i in range (1,101):
    if i%2==0:
        a+=i
    if i%2==1:
        b+=i
print(a-b)     