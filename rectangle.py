# 직사각형의 가로, 세로만 지정해서 직사각형을 생성하면,
# 멤버 메소드를 이용해 넓이와 둘레를 구할 수 있는 클래스를 작성하세요.
# (생성자, 넓이, 둘레 함수 총 3가지가 포함되어야함)
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        return result

    def circumference(self):
        result = self.length*2 + self.width*2
        return result

