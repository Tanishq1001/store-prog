'''
class Dog:
    def bark(self):
        print('bark')

    def add(self, x):
        return x + 1

    def __init__(self, name):
        self.name = name
        print(name)
        pass

    def get_name(self):
        return self.name

d = Dog('tanishq')
d.bark()
print(type(d))
print(d.add(23))



class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student('tanishq', 19, 72)
s2 = Student('aarush', 20, 84)
s3 = Student('krish', 19, 93)

course = Course('science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())
'''


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'I am {self.name} and I am {self.age} years')

class Cat(Pet):
    def speak(self):
        print('meow')

class Dog(Pet):
    def speak(self):
        print('bark')


p = Pet('Tim', 19)
p.show_info()
c = Cat('Kitty', 12)
c.show_info()
c.speak