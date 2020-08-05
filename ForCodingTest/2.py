# 큰 수 더하기

n, m, k = map(int, input().split()) # int형으로 띄어쓰기 기준으로 구분해 입력 받기
data = list(map(int, input().split())) # N개의 수를 위처럼 입력 받기

data.sort() # list로 입력 받은 값을 정렬
first = data[n - 1] # data에서 첫 번째로 큰 수
second = data[n - 2] # data에서 두 번째로 큰 수

count = int(m / (k + 1)) * k # count는 정수형으로 받는다
count += m % (k + 1) # 가장 큰 수가 더해지는 횟수

result = 0 # 결과를 담을 값
result += (count) * first # 첫 번째로 큰 값 더하기
result += (m - count) * second # 두 번째로 큰 값 더하기

print(result)