# 클래스

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print("안녕! " + self.name + "이고" + str(self.age) + "살이야")




# 상속

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다," + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지?" + to_program)

jju = Person('주영',28)
jenny = Police("제니", 20)
michael = Programmer("마이클", 24)

jju.introduce()
jenny.introduce()
michael.introduce() 
michael.program("앱")