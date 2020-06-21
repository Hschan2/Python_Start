# 문자 출력
print("Hello World")
# 숫자 더하기 출력
print(1+1)
# 변수로 더하기 출력
x = 1
print(x+1)

# 1. 변수
x1 = 1
y1 = 2

print(x1)
print(y1)

z1 = "안녕"

print(z1)

# 2. 타입
# 숫자
x2 = 1
y2 = 2
z2 = 1.2

print(x2 + y2)
print(x2 - y2)
print(x2 * y2)
print(x2 / y2)
print(x2 ** y2)
print(x2 % y2)

#문자열
x3 = "Hello"
y3 = "Bye"
z3 = """
안녕하세요. 반갑습니다.
"""

print(x3 + " " + y3)
print(z3)

# print("안녕하세요?" + 0) # 다른 타입을 사칙연산(+)을 사용해서 이용할 수 없다
print("안녕하세요? " + str(0)) # 위의 문제를 해결하기 위해서는 str()을 사용

x4 = 4
y4 = "4"

print(x4 + int(y4)) # 반대로 문자열을 숫자 타입으로 바꾸기 위해서는 int()를 사용