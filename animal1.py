# 이름과 동물을 지정해서 인스턴스를 생성하는 동물이라는 클래스를 생성하고,
# 동물을 상속받아 고양이 클래스를 만들어 야옹을 출력하는 함수를 만들고,
# 동물을 상속받아 강아지 클래스를 만들어 왈왈을 출력하는 함수를 만들어주세요.

class animal():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

class cat(animal):
    def howl(self):
        print('야옹')


class dog(animal):
    def howl(self):
        print('왈왈')

강아지 = cat('보리','강아지')
강아지.howl()