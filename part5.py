# 자료구조

# Tuple

# x = tuple()
# y = ()
x = (1,2,3)
y = ('a','b','c')
z = (1,"hello", "there")

# print(x)
# print(y)
print(x + y)
print('a' in y)
print(z)

# tuple의 assignment -> 값 변경
# mutable(가변) -> list vs immutable(불변) -> tuple

# x[0] = 10 # tuple에서는 불가

# dictionary -> key와 구조로 이루어져 있음

# d_x = dict()
# d_y = {}
d_x = {
    "name": "홍",
    "age": 20,
    0:"Hello",
    1:"World",
}

# print(d_x)
# print(d_y)

print(d_x["name"]) # 홍
print(d_x["age"]) # 20
# list는 가변이기 때문에 딕셔너리의 key로 사용 불가

print(d_x[0]) # Hello
print(d_x[1]) # World

print(d_x.keys()) # dict_keys(['name', 'age', 0, 1])
print(d_x.values()) # dict_values(['홍', 20, 'Hello', 'World'])

for key in d_x:
    print(key)
    print(d_x[key]) # name 홍 age 20 0 Hello 1 World

d_x[0] = "Hi" # 0의 인덱스를 가진 위치의 값을 Hi로 변경
print(d_x)

d_x[2] = "Hello" # key와 value 추가
print(d_x)