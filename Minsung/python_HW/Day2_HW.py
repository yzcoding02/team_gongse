# Q1
for i in range(1,11):
    if i%2==1:
        print(i)

# Q2
for i in range(1,11):
    if i%3!=0:
        print(i)

# Q3
for i in range(50,100):
    if i%3==0 :
        if i%4==0 :
            print(i)

# Q4
a=1
for i in range(1,20):
    if i%7==0:
        a*=i
print(a)

# Q5
a=0
for i in range(50,60):
    if i%4!=0:
        a+=i
print(a)

# Q6
a=0
for i in range(1,101):
    if i%2==0:
        a+=i
b=0
for i in range(1,101):
    if i%2==1:
        b+=i
print(a-b)
