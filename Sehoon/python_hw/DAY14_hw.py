class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    
class multicalculator(calculator):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def pow(self):
        return self.a**self.b
    def Q(self):
        return self.a//self.b
    def mod(self):
        return self.a%self.b
    
복합계산기=multicalculator(4, 2)
print(복합계산기.add())
print(복합계산기.sub())
print(복합계산기.mul())
print(복합계산기.div())
print(복합계산기.pow())
print(복합계산기.Q())
print(복합계산기.mod())