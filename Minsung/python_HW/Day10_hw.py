class 수학:
    def __init__(self):
        self.원주율=3.14
    def 원뿔부피(self,반지름,높이):
        부피=self.원주율*반지름*반지름*높이/3
        return 부피

대학수학=수학()
반지름=input("반지름을 입력하세요:")
높이=input("높이를 입력하세요:")
print(f"반지름이 {반지름}이고, 높이가 {높이}이면 원뿔 부피는 {대학수학.원뿔부피(int(반지름),int(높이))}")