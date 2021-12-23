# 이름과 동물을 지정해서 인스턴스를 생성하는 동물이라는 클래스를 생성하고,
# 동물을 상속받아 고양이 클래스를 만들어 야옹을 출력하는 함수를 만들고,
# 동물을 상속받아 강아지 클래스를 만들어 왈왈을 출력하는 함수를 만들어주세요.

class Animal:
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def meow(self):
        return f'{self.name}은 왈왈왈'

class Dog(Animal):
    def bark(self):
        return f'{self.name}은 야옹'

dog1 = Dog('뽀삐')
print(dog1.bark())