# 거스름돈

n = 1260
# 동전 갯수
count = 0

# 화폐
list = [500, 100, 50, 10]

for coin in list:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전 갯수, // => 나누고 소수점 버리고 정수만 반환
    n %= coin

print(count) # 6