def L(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
                print(i) #60
                break
L(3,4)
L(12,60)