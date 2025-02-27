class Student:
    #Class attribute - shared by all instances of student
    #this is the same for every student

    school = "Shiz University"

    def __init__(self, name, age, grade):
        self.name = name #each student may have a different name
        self.grade = grade #each student may have a different grade
        self.age = age #each student may have a different age

    #Method to get information about the student
    def get_info(self):
        return f"{self.name} is {self.age} in grade {self.grade} at {self.school}"
    
#create two student instances
student1 = Student("Alice", 22, "senior")
student2 = Student("Elphaba", 19, "freshman")
student3 = Student("Glinda", 20, "sophomore")

#print the information about the students
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

    