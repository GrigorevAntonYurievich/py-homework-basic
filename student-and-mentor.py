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

# Пример использования

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.grades = {'Python': [10, 9, 8], 'Git': [9, 8, 10]}

some_lecturer = Lecturer('John', 'Doe')
some_lecturer.courses_attached += ['Python']
some_lecturer.grades = {'Python': [9, 10, 8]}

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

print(some_student)
print(some_lecturer)
print(some_reviewer)

# Сравнение студентов и лекторов
print(some_student > some_lecturer)  # Пример сравнения
