class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name == "":
            pass
        else:
            self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age < 0:
            pass
        else:
            self.__age = age

    def __str__(self):
        return f"Person(name={self.__name}, age={self.__age})"

class Student(Person):
    def __init__(self, name, age, grade=None):
        super().__init__(name, age)
        self.__grade = grade

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        if grade < 0:
            pass
        else:
            self.__grade = grade

    def my_static_method():
        return "my_static_method"

    def __str__(self):
        return f"Student(name={self.__name}, age={self.__age}, grade={self.__grade})"
    


student = Student("John", 20, 90)
student2 = student
student2.set_name("Doe")
print(student.get_name())  # Output: Doe
