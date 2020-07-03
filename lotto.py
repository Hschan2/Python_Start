# 1단계 간단하게 로또 만들기
import random

auto = "자동"
manual = "수동"

while(True): # 무제한으로 반복한다
    lottoQuantity = int(input("몇 장의 로또를 구매? ")) # int형으로 입력 값을 받는다
    if lottoQuantity <= 0: # 생성할 로또 갯수가 0개 이하면 종료
        print("종료")
        break # while문 종료
    while lottoQuantity > 0: # 생성할 로또 갯수가 1개 이상일 경우 로또 생성
        print("생성된 로또 번호")
        for i in range(1, lottoQuantity+1): # 1부터 입력한 갯수+1 만큼 반복
            print("[%s] [%d]: " % (auto, i), end=" ") # 1~입력한 갯수+1
            for j in range(6): # 6개까지 반복
                print("{0:3d}".format(random.randint(1,45)), end=" ") # 3d는 3제곱을 1부터 45 사이의 숫자를 랜덤으로
            print()
        break # while 종료