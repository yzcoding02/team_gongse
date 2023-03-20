# Q-두수의 최소공배수를 구하는 함수
def 최소공배수(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            print(i)
            break
최소공배수(12,60)
