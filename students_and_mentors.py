class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
            course in lecturer.courses_attached):
            if grade < 1 or grade > 10:
                return 'Ошибка'
            else:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average_grade(self):
        total_grade = 0
        num_courses = 0
        if len(self.grades) != 0:
            for grades in self.grades.values():
                total_grade += sum(grades)
                num_courses += len(grades)
        if num_courses > 0:
            self.average_grade = total_grade / num_courses
        else:
            return 0

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade:.1f}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}\n')

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0

    def calc_average_grade(self):
        total_grade = 0
        num_courses = 0
        if len(self.grades) != 0:
            for grades in self.grades.values():
                total_grade += sum(grades)
                num_courses += len(grades)
        if num_courses > 0:
            self.average_grade = total_grade / num_courses
        else:
            return 0

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade:.1f}\n')

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

student1 = Student('Сергей', 'Сергеев', 'М')
student2 = Student('Ольга', 'Алёхина', 'Ж')
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Михаил', 'Соколов')
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Павел', 'Павлов')

student1.add_courses('Введение в программирование')
student2.add_courses('Git')

student1.courses_in_progress += ['Python', 'Java', 'C++']
student2.courses_in_progress += ['C++', 'Python', 'Java']
lecturer1.courses_attached += ['Python', 'C#']
lecturer2.courses_attached += ['Java', 'Python', 'C++']
reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Java', 'C#', 'C++']

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer2, 'Java', 8)
student2.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'C++', 7)
student2.rate_lecture(lecturer2, 'Java', 10)

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'C++', 10)
reviewer1.rate_hw(student2, 'C++', 8)
reviewer2.rate_hw(student1, 'Java', 7)
reviewer2.rate_hw(student2, 'C++', 10)

print(student1.rate_lecture(lecturer1, 'C#', 10))
print(student2.rate_lecture(lecturer2, 'C#', 7))
print(reviewer2.rate_hw(lecturer1, 'Python', 9))
print(reviewer1.rate_hw(student2, 'Java', 8))
print()

student1.calc_average_grade()
student2.calc_average_grade()
lecturer1.calc_average_grade()
lecturer2.calc_average_grade()

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]


def average_tasks(students, course):
    total_grade = 0
    num_students = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            num_students += 1
    if num_students > 0:
        return round(total_grade / num_students, 1)
    else:
        return 0

def average_lectures(lecturers, course):
    total_grade = 0
    num_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            num_lecturers += 1
    if num_lecturers > 0:
        return round(total_grade / num_lecturers, 1)
    else:
        return 0

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(average_tasks(students_list, 'C++'))
print(average_lectures(lecturers_list, 'Java'))
print()
print(student1 == student2)
print(student1 > student2)
print(student1 < student2)
print(lecturer1 == lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)
