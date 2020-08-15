n, m = map(int, input().split()) # 공백 구분으로 int형 입력 받기

result = 0 # 결과값 초기화

while n >= m: # m이 n보다 크거나 같을 때와
    while n % m != 0: # n을 m으로 나눌 때의 나머지가 0이 아닐 때까지
        n -= 1 # n을 1씩 뺀다
        result += 1 # 결과값에 1씩 더한다
    n //= m # 나누고 몫 구하기
    result += 1 # 결과값에 1씩 더한다

while n > 1: # n이 아직도 1보다 클 경우
    n -= 1 # n에서 1씩 빼준다
    result += 1 # 결과값에 1씩 더한다

print(result)