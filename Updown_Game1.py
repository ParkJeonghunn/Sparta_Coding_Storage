import random

computer = random.randrange(1,101)

for chance in range(5):
    player = int(input("숫자를 입력하세요: "))
    if computer == player:
        print('정답입니다')
        break
    elif chance == 4:
        print('실패입니다')
        break
    elif computer > player:
        print('Up')
    elif computer < player:
        print('Down')

if chance == 4:
    print('정답은', computer,'입니다')