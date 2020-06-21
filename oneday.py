# part1과 part2 복습

def sayHello(name, age):
    if age < 10:
        print("안녕 %s" % name)
    elif age >= 10 and age <= 20:
        print("안녕하세요 %s" % name)
    else:
        print("안녕하십니까 %s" % name)


sayHello("홍", 15)