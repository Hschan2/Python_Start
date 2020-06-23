# Animal Package
# dog, cat modules
# dog, cat modules can say "hi"

from animal import dog # animal 패키지에서 dog 라는 모듈을 가져온다
from animal import cat
from animal import * # animal 패키지의 모든 모듈을 가져와라

d = dog.Dog()
c = cat.Cat()

d.hi()
c.hi()