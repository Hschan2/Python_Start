# Boolean
x = True
y = False

print(x)
print(y)

# 조건문
if 2 > 1: # True일 경우
    print("Hello")
if not 1 > 2: # True가 아닐 경우 (False)
    print("Not Hello")
if 1 > 0 and 2 > 1: # 둘 다 True여야 성공. 둘 다 True이기 때문에 실행, 만약 0 > 0 and 2 > 1일 경우 앞이 False이기 때문에 오류
    print("And Hello")
if 0 > 0 or 2 > 1: # 둘 중 하나만 True이면 성공
    print("Or Hello")

x2 = 3

if x > 5:
    print("True")
elif x2 == 3:
    print(x2)
else:
    print("False")

# 함수
def chat():
    print("안녕? 반가워")
    print("너는 누구니?")

chat()

def chat2(name1, name2, age):
    print("안녕? 반가워 %s야" % name1)
    print("너는 누구니? 나는 %s야 나는 %d살이야" % (name2, age))

chat2("홍", "박", 20)

def dsum(a, b):
    result = a + b
    return result
d = dsum(1, 2)
print(d)