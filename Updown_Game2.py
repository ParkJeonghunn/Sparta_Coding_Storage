from math import floor

num_list = range(1,101)
player = int(input("숫자를 입력하세요: "))
while player not in num_list:
    print('----- 다시 입력하세요 -----')
    player = int(input("숫자를 입력하세요: "))

while True:
    computer = num_list[floor(len(num_list)/2)]
    print('컴퓨터:',computer)

    if player == computer:
        print('정답입니다.')
        break

    p_ud = input('업? 다운?')
    if player > computer and p_ud == '업':
        num_list = num_list[num_list.index(computer)+1:]
    elif player < computer and p_ud == '다운':
        num_list = num_list[:num_list.index(computer)]
    else:
        print('거짓말 하지마세요')