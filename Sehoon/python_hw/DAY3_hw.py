# 1-chatGPT 5번
# -1-for
# for i in range(5):
#     print("chatGPT")
# -2-while
# i=0
# while i<5:
#     print("chatGPT")
#     i+=1
# 2-1에서 10까지의 수중 짝수만
# -1-for
# for i in range(1,11):
#     if i%2==0:
#         print(i)
# -2-while
# i=1
# while i<11:
#     if(i%2==0):
#         print(i)
#     i+=1
# 3-1에서 20까지의 수중 4의 배수들의 합
# -1-for
# a=0
# for i in range(1,21):
#     if i%4==0:
#         a+=i
# print(a)
# -2-while
# a=0
# i=0
# while i<21:
#     if(i%4==0):
#         a+=i
#     i+=1
# print(a)
# 4-50에서 70까지의 수중 2와 3의 공배수
# -1-for
# for i in range(50,71):
#     if i%2==0: 
#         if i%3==0:
#             print(i)
# -2-while
# i=50
# while i<71:
#     if(i%2==0):
#         if(i%3==0):
#             print(i)
#     i+=1
# 5-100에서 110까지의 수중 홀수들의 곱
# -1-for
# a=1
# for i in range(100,111):
#     if i%2!=0:
#         a*=i
# print(a)
# -2-while
# a=1
# i=100
# while i<111:
#     if(i%2!=0):
#         a*=i
#     i+=1
# print(a)
# # 6-1에서 100까지의 수중 3의 배수들의 합에서 7의 배수들의 합을 뺀 수
# -1-for
# a=0
# b=0
# for i in range(1,101):
#     if i%3==0: 
#         a+=i
#     if i%7==0:
#         b+=i
# print(a-b)
# -2-while
# a=0
# b=0
# i=1
# while i<101:
#     if(i%3==0):
#         a+=i
#     if(i%7==0):
#         b+=i
#     i+=1
# print(a-b)