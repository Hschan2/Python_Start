# 자료구조
# List

# x = list()
# y = []
x = [1,2,3,4]
y = ["Hello", "World"]
z = ["Hello", 1,2,3]

#print(x)
#print(y)

print(x + y)
print(x[0]) # 1

x[3] = 10
print(x[3]) # 10

num_len = len(x)
print(num_len) # 4

sort = [4,3,2,1]
num_sort = sorted(sort)
print(num_sort) # [1,2,3,4]

num_sum = sum(x)
print(num_sum) # 16

for n in x:
    print(n) # 1 2 3 10

print(x.index(2)) # 2라는 인덱스가 1번째 자리에 있다 (0,1... 순서)

print(2 in x) # 2라는 인덱스가 x리스트 안에 있어서 true 출력

if 2 in x:
    print("2 인덱스가 있다")
else:
    print("없다")