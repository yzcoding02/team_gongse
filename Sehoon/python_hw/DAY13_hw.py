class 도형:
    def __init__(self, 반지름, 높이):
        self.원주율=3.141592
        self.반지름=반지름
        self.높이=높이
    def 원기둥부피(self):
        self.원기둥부피=self.원주율*self.반지름**2*self.높이
        print(f"반지름이 {self.반지름}이고, 높이가 {self.높이}일 때 원기둥의 부피는 {self.원기둥부피}이다.")
    def 원기둥겉넓이(self):
        self.원기둥겉넓이=2*self.원주율*self.반지름**2+2*self.원주율*self.반지름*self.높이
        print(f"반지름이 {self.반지름}이고, 높이가 {self.높이}일 때 원기둥의 겉넓이는 {self.원기둥겉넓이}이다.")
    def 원뿔부피(self):
        self.원뿔부피=self.원주율*self.반지름**2*self.높이/3
        print(f"반지름이 {self.반지름}이고, 높이가 {self.높이}일 때 원뿔의 부피는 {self.원뿔부피}이다.")

원기둥=도형(5, 10)
원기둥.원기둥부피()
원기둥.원기둥겉넓이()
원뿔=도형(8, 9)
원뿔.원뿔부피()