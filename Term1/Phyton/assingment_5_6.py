'''
Student: Valmir de Barros Pedro
Student Number: C0808675
Course: 2022F CSD 1233 Python Programming

Planing the class

Class: Student
Para:
    fist Name (pub)
    last name (pub)
    course enrolled (pub)
    assignment1 (Priv)
    assignment2 (Priv)
    test (Priv)
func:
    average (Priv)
    approved (Priv)

'''


class Student:
    def __init__(self, fName, lName, courseEnroll, assignment1, assignment2, test):

        self.fName = fName
        self.lName = lName
        self.courseEnroll = courseEnroll
        self.__assignment1 = float(assignment1)
        self.__assignment2 = float(assignment2)
        self.__test = float(test)

    def average(self):
        return (self.__assignment1 + self.__assignment2 + self.__test)/3

    def approved(self):
        avg = self.average()
        if avg >= 5:
            return 'approved'
        else:
            return 'reproved'

    def __str__(self):
        return f'Name: {self.fName} {self.lName}\n Course: {self.courseEnroll}\n Grades\n Assignment 1: {self.__assignment1}\n Assignment 2: {self.__assignment2}\n Test: {self.__test}\n So the average of the grades is {self.average()}\n this student is {self.approved()} '


students = []
for i in range(2):

    print('---------')
    FirstName = input("Enter the fist name: ").capitalize().strip()
    LastName = input("Enter the last name: ").capitalize().strip()
    Course = input("Enter the course name: ").upper().strip()
    gradeAss1 = input("Enter the fist Assignment grade: ").strip()
    gradeAss2 = input("Enter the second Assignment grade: ").strip()
    gradeTest = input("Enter the test grade: ")
    objStudent = Student(FirstName, LastName, Course,
                         gradeAss1, gradeAss2, gradeTest)
    students.append(objStudent)


for student in students:
    print('---------')
    print(student)
