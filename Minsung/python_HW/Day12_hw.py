class 계산기:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def 더하기(self):
        print(self.a + self.b)
    def 빼기(self):
        print(self.a - self.b)
    def 곱하기(self):
        print(self.a * self.b)
    def 나누기(self):
        print(self.a / self.b)
    
class 복합계산기(계산기):
    def 제곱(self):
        print(self.a**self.b)
    def 몫(self):
        print(self.a%self.b)
    def 나머지(self):
        print(self.a//self.b)
    
연산1=복합계산기(3,4)
연산1.더하기()
연산1.빼기()
연산1.곱하기()  
연산1.나누기()
연산1.제곱()
연산1.몫()
연산1.나머지()
