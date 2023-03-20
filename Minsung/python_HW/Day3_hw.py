# Q1
i=0
while i<5:
    print("ChatGPT")
    i+=1

for i in range(1,6):
    print("ChatGPT")

# Q2
i=1
while i<11:
    if i%2==0:
        print(i)
    i+=1

for i in range(1,11):
    if i%2==0:
        print(i)

# Q3
i=1
a=0
while i<21:
    if i%4==0:
        a+=i
    i+=1
print(a)

a=0
for i in range(1,21):
    if i%4==0:
        a+=i
print(a)

# Q4
i=50
while i<71:
    if i%2==0:
        if i%3==0:
            print(i)
    i+=1

for i in range(50,71):
    if i%2==0:
        if i%3==0:
            print(i)
# Q5
i=100
a=1
while i<111:
    if i%2==1:
        a*=i
    i+=1
print(a)

a=1
for i in range(100,111):
    if i%2==1:
        a*=i
print(a)        

# Q6
i=0
a=0
while i<101:
    if i%3==0:
        a+=i
    i+=1
b=0
while i<101:
    if i%7==0:
        b+=i
    i+=1
print(a-b)

a=0
for i in range(1,101):
    if i%3==0:
        a+=i
b=0        
for i in range(1,101):
    if i%7==0:
        b+=i
print(a-b)        