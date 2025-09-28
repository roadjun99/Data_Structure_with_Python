import random  # random 라이브러리를 불러옵니다.

answer = random.randint(10, 99)  # 10부터 99 사이의 임의의 정수를 answer에 저장합니다.
min, max = 0, 99

n = int(input("기회 : "))
for i in range(n):
    print("숫자를 입력하세요(범위:%d~%d): " % (min, max), end='')
    guess = int(input())

    if guess > answer:
        print("아닙니다. 더 작은 숫자입니다!")
        max = guess
        if (i == n - 1):
            print("최대 횟수 도달. 정답은 %d입니다." % answer)
            break
        else:
            continue
    elif guess < answer:
        print("아닙니다. 더 큰 숫자입니다!")
        min = guess
        if (i == n - 1):
            print("최대 횟수 도달. 정답은 %d입니다." % answer)
            break
        else:
            continue
    else:
        print("정답입니다. %d번 만에 맞히셨습니다.\n게임이 끝났습니다." % (i + 1))
        break