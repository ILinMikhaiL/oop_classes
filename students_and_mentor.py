class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#Создание дочернего класса Lecturer и Reviewer от Mentor:
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    #Метод выставление оценки студентам курса
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and course in student.courses_in_progress):
            if (grade >= 1 and grade <= 10):
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Оценка вне 10-бальной шкалы'
        else:
            return 'Error'
    #Перегрузка магического метод __str__
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0

    def get_name_surname(self):
        return f"{self.name} {self.surname}"

    #Метод получения средней оценки по всем курсам
    def get_average_rating(self):
        if self.grades:
            __grade = 0
            __num = 0
            for grade_list in self.grades.values():
                for grade_course in grade_list:
                    __grade +=grade_course
                    __num +=1
            return __grade/__num
        return 0

    # Перегрузка магического метод __str__
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} '
                f'\nСредняя оценка за лекции: {self.get_average_rating()}')

    #Методы сравнения
    def __gt__(self, other):
        return self.get_average_rating() > other.get_average_rating()

    def __lt__(self, other):
        return self.get_average_rating() < other.get_average_rating()

    def __ge__(self, other):
        return self.get_average_rating() >= other.get_average_rating()

    def __le__(self, other):
        return self.get_average_rating() <= other.get_average_rating()

    def __eq__(self, other):
        return self.get_average_rating() == other.get_average_rating()

    def __ne__(self, other):
        return self.get_average_rating() != other.get_average_rating()


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод получения средней оценки по всем курсам
    def get_average_rating(self):
        if self.grades:
            __grade = 0
            __num = 0
            for grade_list in self.grades.values():
                for grade_course in grade_list:
                    __grade += grade_course
                    __num += 1
            return __grade/__num
        return 0

    def get_name_surname(self):
        return f"{self.name} {self.surname}"

    # Перегрузка магического метод __str__
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.get_average_rating()}'
                f'\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {', '.join(self.finished_courses)}')

        # Методы сравнения
        def __gt__(self, other):
            return self.get_average_rating() > other.get_average_rating()

        def __lt__(self, other):
            return self.get_average_rating() < other.get_average_rating()

        def __ge__(self, other):
            return self.get_average_rating() >= other.get_average_rating()

        def __le__(self, other):
            return self.get_average_rating() <= other.get_average_rating()

        def __eq__(self, other):
            return self.get_average_rating() == other.get_average_rating()

        def __ne__(self, other):
            return self.get_average_rating() != other.get_average_rating()

    # Метод выставление оценки лектору курса
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer,Lecturer) and
        course in self.courses_in_progress and
        course in lecturer.courses_attached
        ):
            if (grade >= 1 and grade <=10):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценка вне 10-бальной шкалы'
        else:
            return 'Error'

# Метод сравнения по средней оценки
def compare_by_average_rating(self,other):
    str =''
    #выполнение сравнения двух объектов
    if (isinstance(self, Student) and isinstance(other, Student)) or (isinstance(self, Lecturer) and isinstance(other, Lecturer)):
        if self.get_average_rating() == other.get_average_rating():
            str = f' {self.name} {self.surname}: {self.get_average_rating()} == {other.name} {other.surname}: {other.get_average_rating()}'
        elif self.get_average_rating() < other.get_average_rating():
            str = f' {self.name} {self.surname}: {self.get_average_rating()} < {other.name} {other.surname}: {other.get_average_rating()}'
        else:
            str = f' {self.name} {self.surname}: {self.get_average_rating()} > {other.name} {other.surname}: {other.get_average_rating()}'
    else:
        print(f'Объекты разных классов')

    #Вывод результата
    if (isinstance(self, Student)):
        print(f'Средняя оценка за домашние задания: {str}')
    elif(isinstance(self, Lecturer) and isinstance(other, Lecturer)):
        print(f'Средняя оценка за лекции: {str}')


# Метод получения средней оценки за курс
def get_average_rating_course(course,students_or_lecturers):
    __sum_grades = 0
    __num_grades = 0
    return_str =''

    for student_or_lecturer in students_or_lecturers:

        for grade in student_or_lecturer.grades.get(course):
            __sum_grades += grade
            __num_grades += 1
    if (isinstance(student_or_lecturer, Lecturer)):
        return_str = f"Средняя оценка лекторов за курс {course}: {__sum_grades/__num_grades}"
    elif (isinstance(student_or_lecturer, Student)):
        return_str = f"Средняя оценка студентов за курс {course}: {__sum_grades/__num_grades}"
    print(return_str)


def compare(self,other):
        if self.get_average_rating() == other.get_average_rating():
            print(f' {self.name} {self.surname}: {self.get_average_rating()} == {other.name} {other.surname}: {other.get_average_rating()}')
        elif self.get_average_rating() < other.get_average_rating():
            print(f' {self.name} {self.surname}: {self.get_average_rating()} < {other.name} {other.surname}: {other.get_average_rating()}')
        else: print(f' {self.name} {self.surname}: {self.get_average_rating()} > {other.name} {other.surname}: {other.get_average_rating()}')

# Создание объекта класса Student
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['С++']

student_2 = Student('Ivan', 'Eman', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['С#']


# Создание объекта класса Lecturer
lector_1 = Lecturer('Ivan', 'Ivanov')
lector_1.courses_attached +=['Python']
lector_1.courses_attached +=['C++']

lector_2 = Lecturer('Alex', 'Ivanov')
lector_2.courses_attached +=['Python']
lector_2.courses_attached +=['C#']

# Создание объекта класса Reviewer
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['С++']

reviewer_2 = Reviewer('Some', 'Buddy')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['С#']

# Выставление оценки студенту за выполнение ДЗ
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'С++', 6)

reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'С#', 6)

# Получение оценки лектора курса
student_1.rate_lecturer(lector_1,'Python', 8)
student_1.rate_lecturer(lector_2,'Python', 6)

print(f'\n Задание 3.1 Перегрузите магический метод __str__ у всех классов. ')
print(f'***Вывод метода __str__ class Student***')
print(student_1)
print(f'\n***Вывод метода __str__ class Lecturer***')
print(lector_1)
print(f'\n***Вывод метода __str__ class Reviewer***')
print(reviewer_1)

print(f'\n Задание 3.2 Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.')
compare_by_average_rating(student_1,student_2)
compare_by_average_rating(lector_1,lector_2)

print("---Сравнение с помощью магических методов---")
print(f"Сравнение лекторов:\n\tСредняя оценка за лекции: {lector_1.get_name_surname()} > {lector_2.get_name_surname()}: {lector_1 > lector_2}")
print(f"\tСредняя оценка за лекции: {lector_1.get_name_surname()} < {lector_2.get_name_surname()}: {lector_1 < lector_2}")
print(f"\tСредняя оценка за лекции: {lector_1.get_name_surname()} >= {lector_2.get_name_surname()}: {lector_1 >= lector_2}")
print(f"\tСредняя оценка за лекции: {lector_1.get_name_surname()} <= {lector_2.get_name_surname()}: {lector_1 <= lector_2}")
print(f"\tСредняя оценка за лекции: {lector_1.get_name_surname()} == {lector_2.get_name_surname()}: {lector_1 == lector_2}")
print(f"\tСредняя оценка за лекции: {lector_1.get_name_surname()} != {lector_2.get_name_surname()}: {lector_1 != lector_2}")

print(f"Сравнение студентов:\n\tСредняя оценка за домашние задания: {lector_1.get_name_surname()} > {lector_2.get_name_surname()}: {lector_1 > lector_2}")
print(f"\tСредняя оценка за домашние задания: {lector_1.get_name_surname()} < {lector_2.get_name_surname()}: {lector_1 < lector_2}")
print(f"\tСредняя оценка за домашние задания: {lector_1.get_name_surname()} >= {lector_2.get_name_surname()}: {lector_1 >= lector_2}")
print(f"\tСредняя оценка за домашние задания: {lector_1.get_name_surname()} <= {lector_2.get_name_surname()}: {lector_1 <= lector_2}")
print(f"\tСредняя оценка за домашние задания: {lector_1.get_name_surname()} == {lector_2.get_name_surname()}: {lector_1 == lector_2}")
print(f"\tСредняя оценка за домашние задания: {lector_1.get_name_surname()} != {lector_2.get_name_surname()}: {lector_1 != lector_2}")

print(f'\n Задание 4.2 '
      f'для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);'
      f'для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).')
students = [student_1,student_2]
lectors = [lector_1,lector_2]

get_average_rating_course('Python', students)
get_average_rating_course('Python', lectors)


