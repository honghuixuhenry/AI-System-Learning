# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print("Hello")

# student = Student("Honghui", 35)
# print(student.name)
# print(student.age)
# student.say_hello()

# class Dog:

#     def __init__(self, name):
#         self.name = "Dog"

#     def bark(self):
#         print(self.name, "is barking!")

# dog = Dog("Lucky")

# dog.bark()

class Professor:

    def __init__(self, name, university):
        self.name = name
        self.university = university

    def introduce(self):
        print("My name is", self.name)
        print("I work at", self.university)

professor = Professor("Honghui", "KSU")
professor.introduce()