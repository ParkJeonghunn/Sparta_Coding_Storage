import random

Start= random.choice(['Player','Computer'])
num_list = range(1,32)
def br31():
    for num in num_list:
        print(num)

while True:

    if Start == 'Player':
        print('Player가 선공입니다')
        p_ud = int(input('숫자를 입력하세요'))
        num_list[:num_list.index(p_ud) + 1]
        for num in num_list:
            print(num)
    else:
        print('컴퓨터가 선공입니다')
        computer = random.choice([1, 2, 3])
        num_list[:num_list.index(computer) + 1]
        for num in num_list:
            print(num)







