# 반복문
# For

for i in range(10):
    print(i+1)

x = 0
while True: # x < 3대신 True로 하면 무한 루프
    print("안녕")
    x += 1
    if x == 3:
        break # 중단
    # continue는 continue를 만났을 경우 다시 while문의 첫 번째 라인으로 돌아가라, 특이한 조건에서 밑에 코드를 실행하고 싶지 않을 때 사용
