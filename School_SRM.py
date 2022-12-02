class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Human):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.exp = experience


class Student(Human):
    def __init__(self, name, age, grade, address):
        super().__init__(name, age)
        self.grade= grade
        self.address = address


def register():
    ans = input("Register choose one( Teacher, Student) ").lower()
    if ans == "teacher":
        teacher = Teacher(input("your name: "), int(input("your age: ")), input("your subject: "), input("your experience, year: "))
        print(teacher.name)
        print(teacher.age,' years old')
        print(teacher.subject)
        print(teacher.exp, "years of experience")
    elif ans == "student":
        student = Student(input("your name: "), int(input("your age: ")), int(input("your grade: ")), input("your address: "))
        print(student.name)
        print(student.age, " years old")
        print(student.grade, "'s grade")
        print(student.address)
register()