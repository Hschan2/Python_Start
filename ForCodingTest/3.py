n, m = map(int, input().split()) # n, m을 int형으로 공백을 기준으로 입력 받기

result = 0 # 결과 값 초기화

for i in range(n):
    data = list(map(int, input().split())) # data를 여러 개의 int형으로 공백 기준으로 입력 받기
    minValue = min(data) # data에서 가장 작은 값
    result = max(result, minValue) # 가장 작은 값 중에 가장 큰 값

print(result)