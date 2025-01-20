class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        if self.first_name == self.last_name:
            return f"{self.first_name}"
        else:
            return f"{self.first_name} {self.last_name}"

students = []
while True:
    try:
        first_name, last_name = input().split()
        students.append(Student(first_name, last_name))
    except EOFError:
        break

students.sort(key=lambda student: (student.last_name, student.first_name))

for student in students:
    print(student)