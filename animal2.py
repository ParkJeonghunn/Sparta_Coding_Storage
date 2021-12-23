# 이름과 동물을 지정해서 인스턴스를 생성하는 동물이라는 클래스를 생성하고,
# 동물을 상속받아 고양이 클래스를 만들어 야옹을 출력하는 함수를 만들고,
# 동물을 상속받아 강아지 클래스를 만들어 왈왈을 출력하는 함수를 만들어주세요.

class animal():
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

class cat(animal):
    def howl(self):
        print('{0}가 {1}하고 울었습니다'.format(self.name, self.voice))

class dog(animal):
    def howl(self):
        print('{0}가 {1}하고 울었습니다'.format(self.name, self.voice))

class cow(animal):
    def howl(self):
        print(f'{self.name}가 {self.voice}하고 울었습니다.')

