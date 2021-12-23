class Object:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def attack(self, target):
        print(f'{self.name}가 {target.name}을 엉덩이로 공격!')
        print(f'{target.name}가 {self.dmg}만큼 피해를 받았습니다!!')
        target.hp = target.hp - self.dmg
        if target.hp <= 0:
            print(f'{target.name}가 죽었습니다!!!')
        else:
            print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        return target.hp

class Player(Object):
    def magic(self,target):
        print(f'{self.name}가 {target.name}을 액션빔으로 공격!')
        print(f'{target.name}가 50만큼 피해를 받았습니다!!')
        target.hp = target.hp - 50
        if target.hp <= 0:
            print(f'{target.name}가 죽었습니다!!!')
        else:
            print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        return target.hp

class Monster(Object):
    def stay(self):
        print(f'{self.name}가 아무것도 하지않았습니다.')

    def cure(self):
        print(f'{self.name}가 체력을 10 회복하였습니다.')
        self.hp = self.hp + 10
        return self.hp

from random import choice
from time import sleep

def Character():
    Warrior = Player('짱구', 100, 10)
    Monsters = {}
    Monsters['철수'] = Monster('철수', 10, 10)
    Monsters['맹구'] = Monster('맹구', 30, 30)
    Monsters['훈이'] = Monster('훈이', 50, 50)
    return Warrior, Monsters

def Showinfo(Player, Monsters):
    print('\n---------------턴 시작---------------')
    print(f'{Player.name}의 체력: {Player.hp}')
    for key, value in Monsters.items():
        print(f'{value.name}의 체력: {value.hp}')

def Playerturn(Player, Monsters):
    print('\n---------------짱구 턴 시작---------------')
    target = input('누구를 공격하시겠습니까? : ')
    command = input('어떻게 공격하시겠습니까? 엉덩이? 액션빔? : ')
    if command == '엉덩이':
        Player.attack(Monsters[target])
    elif command == '액션빔':
        Player.magic(Monsters[target])
    return Monsters

def Check_mdead(Monsters):
    dead_monsters = []
    for key, value in Monsters.items():
        if value.hp <= 0:
            dead_monsters.append(key)

    for i in dead_monsters:
        del Monsters[i]
    if len(Monsters) <= 0:
        return Monsters, True
    else:
        return Monsters, False

def Monsterturn(Player, Monsters):
    print('\n---------------악당 턴 시작---------------')
    sleep(2)
    for key, value in Monsters.items():
        commands = ['cure','attack','stay']
        command = choice(commands)
        if command == 'cure':
            value.cure()
        elif command == 'attack':
            value.attack(Player)
        elif command == 'stay':
            value.stay()
    return Player

def Check_pdead(Player):
    if Player.hp <= 0:
        return True
    else:
        return False

Warrior, Monsters = Character()

while True:
    Showinfo(Warrior, Monsters)
    Playerturn(Warrior, Monsters)
    sleep(1)
    Monsters, ismdead = Check_mdead(Monsters)
    if ismdead:
        print('\n-----------떡잎유치원 대장은 나야!!!-----------')
        break
    Monsterturn(Warrior, Monsters)
    ispdead = Check_pdead(Warrior)
    if ispdead:
        print("\n-----------다시 시도해보아요!!!-----------!!!")
        break
    sleep(1)