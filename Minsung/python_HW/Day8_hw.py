for i in range(1):
    if i%1==0:
        num1=input("첫 번째수:")
        num2=input("두 번째 수:")
        str=f"첫 번째수는{num1},두 번째수는{num2}, 두 수의 합은 {int(num1)+int(num2)}이고, 두 수의 차는{int(num1)-int(num2)}이고, 두 수의 곱은 {int(num1)*int(num2)}이고, 첫 번째수를 두번째 수로 나눈 몫 은는 {int(num2)//int(num1)}, 그리고 나머지는 {int(num1)%int(num2)}입니다"
        print(str[1:])

