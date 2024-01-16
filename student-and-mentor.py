class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades) if self.grades else 0
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"{super().__str__()}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        return self.__str__() < other.__str__()

    def __le__(self, other):
        return self.__str__() <= other.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __ne__(self, other):
        return self.__str__() != other.__str__()

    def __gt__(self, other):
        return self.__str__() > other.__str__()

    def __ge__(self, other):
        return self.__str__() >= other.__str__()

class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"{super().__str__()}\nУ {self.__class__.__name__}а"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades) if self.grades else 0
        return f"{super().__str__()}\nСредняя оценка за лекции: {average_grade:.1f}"

    def __lt__(self, other):
        return self.__str__() < other.__str__()

    def __le__(self, other):
        return self.__str__() <= other.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __ne__(self, other):
        return self.__str__() != other.__str__()

    def __gt__(self, other):
        return self.__str__() > other.__str__()

    def __ge__(self, other):
        return self.__str__() >= other.__str__()

class Reviewer(Mentor):
    pass

def average_hw_grade(students, course):
    total_grades = 0
    total_students = 0

    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])

    return total_grades / total_students if total_students > 0 else 0

def average_lecture_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0

    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])

    return total_grades / total_lecturers if total_lecturers > 0 else 0

# Создаем экземпляры классов
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.grades = {'Python': [10, 9, 8], 'Git': [9, 8, 10]}

some_lecturer = Lecturer('John', 'Doe')
some_lecturer.courses_attached += ['Python']
some_lecturer.grades = {'Python': [9, 10, 8]}

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

# Создаем дополнительные экземпляры классов
student2 = Student('Alice', 'Smith', 'female')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Введение в программирование']
student2.grades = {'Python': [8, 7, 9], 'Java': [10, 9, 8]}

lecturer2 = Lecturer('Jane', 'Doe')
lecturer2.courses_attached += ['Java']
lecturer2.grades = {'Java': [8, 7, 9]}

reviewer2 = Reviewer('Another', 'Person')
reviewer2.courses_attached += ['Java']

# Вызываем методы
print(some_student)
print(student2)
print(some_lecturer)
print(lecturer2)
print(some_reviewer)
print(reviewer2)

# Сравнение студентов и лекторов
print(some_student > student2)
print(some_lecturer > lecturer2)

# Вызываем функции для подсчета средней оценки за домашние задания и за лекции
avg_hw_grade = average_hw_grade([some_student, student2], 'Python')
avg_lecture_grade = average_lecture_grade([some_lecturer, lecturer2], 'Python')

print(f'Средняя оценка за домашние задания по Python: {avg_hw_grade:.2f}')
print(f'Средняя оценка за лекции по Python: {avg_lecture_grade:.2f}')
