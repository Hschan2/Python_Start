# 1단계 간단하게 로또 만들기
import random

auto = "자동"
manual = "수동"
# numbers = random.sample(range(1,46),6) => 전역 변수로 쓸 경우 똑같은 숫자가 계속 출력

while(True): # 무제한으로 반복한다
    lottoQuantity = int(input("몇 장의 로또를 구매? ")) # int형으로 입력 값을 받는다
    if lottoQuantity <= 0: # 생성할 로또 갯수가 0개 이하면 종료
        print("종료")
        break # while문 종료
    while lottoQuantity > 0: # 생성할 로또 갯수가 1개 이상일 경우 로또 생성
        print("생성된 로또 번호")
        for i in range(1, lottoQuantity+1): # 1부터 입력한 갯수+1 만큼 반복 => 1, 6 일 경우 1~5 반복
            numbers = random.sample(range(1,46),6) # 이 처럼 지역 변수로 써야 i 번마다 다른 번호가 출력
            print("[%s] [%d]: " % (auto, i), end=" ") # 1~입력한 갯수+1, end=" "는 줄바꿈 제거용이다. print는 자동으로 줄바꿈이 적용되기 때문에 이를 써야 줄바꿈이 사라진다
            # for j in range(6): # 6개까지 반복
                # print("{0:3d}".format(random.randInt(1,45)), end=" ") # 3d는 3제곱을 1부터 45 사이의 숫자를 랜덤으로 그러나 중복 숫자가 나온다
            for n in numbers:
                print("{0:3d}".format(n), end=" ") # random.sample(range(1,46),6)은 중복 제거된 숫자가 1~45까지 6번 출력되는 것이다. 다만 이는 String 타입이기 때문에 format을 위해 정수형으로 바꿔야 한다.
                                                    # 그래서 각 숫자만큼 반복해서 n에 담아 format형식에 맞게 출력되게 만든다. 이처럼 중복 제거된 숫자가 출력된다
            print()
        break # while 종료