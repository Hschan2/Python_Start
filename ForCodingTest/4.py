n, m = map(int, input().split()) # n, m을 int형으로 입력 받기 (공백 기준)

result = 0 # 결과값 초기화

for i in range(n):
    data = list(map(int, input().split())) # 여러 개의 값을 int형으로 입력 받기 (공백 기준)
    minValue = 10001 # 가장 작은 수 초기화
    for a in data:
        minValue = min(minValue, a) # minValue와 data의 a중 작은 수를 넣는다 (반복으로 돌리면서)

    result = max(result, minValue) # result 안의 값과 minValue 중 큰 값을 넣는다 (반복으로 돌리면서)

print(result) # 결과 출력