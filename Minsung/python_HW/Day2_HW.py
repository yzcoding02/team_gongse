# Q1 1부터 10에서 홀수
for i in range(1,11):
    if i%2==1:
        print(i)

# Q2 1부터 10에서 짝수
for i in range(1,11):
    if i%3!=0:
        print(i)

# Q3 50부터 100까지에서 3과4의 공배수
for i in range(50,100):
    if i%3==0 :
        if i%4==0 :
            print(i)

# Q4 1부터 20까지에서 7의배수들의 곱 
a=1
for i in range(1,20):
    if i%7==0:
        a*=i
print(a)

# Q5 50부터 60까지에서 4의 배수가 아닌 수들의 합
a=0
for i in range(50,60):
    if i%4!=0:
        a+=i
print(a)

# Q6 1부터 100까지에서 2의 배수들의 합 빼기 3의 배수들의 합
a=0
for i in range(1,101):
    if i%2==0:
        a+=i
b=0
for i in range(1,101):
    if i%2==1:
        b+=i
print(a-b)
