# Class

class Person():
    # name = "홍"

    # name 변수를 고정하지 않고 오브젝트로 만들 때 새로 이름을 짓고 싶을 때
    def __init__(self, name, age): # initialize(초기화) -> init
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("Hello " + to_name + ". 나는 %s" % self.name)

    def iam(self):
        print("안녕하세요. 저는 " + self.name + "입니다. 그리고 나이는 " + str(self.age) + "살입니다.")

class Police(Person): # Police(Person) -> Police는 Person을 상속받겠다
    def arrest(self, to_arrest):
        print("넌 체포됐다 " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음에는 %s 만들어야지" % to_program)

# p = Person("홍")
p = Person("홍", 20) # 숫자 타입을 사용할 때 위 iam에서 age를 문자 타입으로 변경해야
# p.say_hello("김")
p.iam()

po = Police("김", 21)
po.iam()
po.arrest("이")

pro = Programmer("박", 22)
pro.iam()
pro.program("테트리스")
