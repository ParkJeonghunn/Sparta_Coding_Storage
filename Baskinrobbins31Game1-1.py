import random


print("베스킨라빈스 31 게임 프로그램입니다!")

start = random.choice([1, 0])
start = int(start)

call = 0
count = 1

while call < 31:
    if count % 2 == start:
        # 사용자의 차례
        print('사용자의 차례')
        size_of_call = input("호출할 개수를 입력하세요 : ")
        size_of_call = int(size_of_call)

        for _ in range(size_of_call):
            if call == 31:
                break
            call += 1
            print("사용자 : '{0}'!!!".format(call))

    else:
        # 컴퓨터의 차례
        print('컴퓨터의 차례')
        size_of_call = random.randint(1, 3)

        for _ in range(size_of_call):
            if call == 31:
                break
            call += 1
            print("컴퓨터 : '{0}'!!!".format(call))

    count += 1

if count % 2 == start:
    print("사용자의 승리!!")
else:
    print("컴퓨터의 승리!!")