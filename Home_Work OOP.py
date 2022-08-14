class Student:

    '''класс Студенты с Именем, Фамилией и полом; пройденные курсы; курсы на изучении;оценка '''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_rates = []

    def rate_lecturer(self, lecturer, course, grade):
        '''оценка Лекторам от студентов за начитанные лекции'''
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def stud_average_rating(self):
        n = 0
        for k, v in self.grades.items():
            self.all_rates.extend(v)

        return sum(self.all_rates) / len(self.all_rates)

    def __str__(self):
        res = f"  Имя: {self.name}\n   Фамилия: {self.surname}\n   " \
              f"Пол: {self.gender}\n   Завершенные курсы: {self.finished_courses[0]}\n   " \
              f"Изучаемые курсы: {self.courses_in_progress[0]}\n   Средняя оценка по курсу за ДЗ {self.stud_average_rating()}"
        return res

    def __lt__(self, other):
        if not isinstance(other ,Student):
            print('Не верно')
            return
        return self.stud_average_rating() < other.stud_average_rating()

    # def Add_students(self, name, surname,courses_in_progress):
    #     list_students = []
    #     list_students.append(self.name)
    #     print(Add_students)

class Mentor:
    '''класс Наставник. Имя, Фамилия наставника и список читаемых курсов'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    '''класс Лектор. Имя, Фамилия лектора. Оценка студентов за начитанные лекции????'''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.student_list = []
        self.all_rates = []

    def __str__(self):
        res = f"  Имя: {self.name}\n   Фамилия: {self.surname} \n   Средняя оценка за лекции = {self.average_rating()}"
        return res

    def average_rating(self):
        n = 0
        for k, v in self.grades.items():
            self.all_rates.extend(v)

        return sum(self.all_rates) / len(self.all_rates)

    def __lt__(self, other):
        if not isinstance(other ,Lecturer):
            print('Не верно')
            return
        return self.average_rating() < other.average_rating()

class Reviewer(Mentor):
    '''класс Проверяющего. Имя, Фамилия проверяющего, оценка за предмет и прочтенный курс'''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_stud(self, student, course, grade):
        '''оценка студентам от Проверяющего'''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"  Имя: {self.name}\n   Фамилия: {self.surname}"

student_1 = Student("Семен", "Слепаков", "м")
student_2 = Student("Сергей", "Светлаков", "м")

student_1.courses_in_progress = ['Git']
student_2.courses_in_progress = ['Python']

student_1.finished_courses = ['Python']
student_2.finished_courses = ['Git']

student_1.grades['Git'] = [9, 10, 9, 10, 9]
student_2.grades['Python'] = [8, 10, 9, 9, 10]

first_lector = Lecturer("Аркадий", "Укупник")
first_lector.courses_attached += ["Git"]
first_lector.grades['Git'] = [9, 9, 8, 10, 9]
first_lector.average_rating()

second_lector = Lecturer("Олег", "Газманов")
second_lector.courses_attached += ["Python"]
second_lector.grades['Python'] = [10, 9, 10, 10, 9]
second_lector.average_rating()

first_reviewer = Reviewer("Дональд", "Дак")
first_reviewer.rate_stud = [student_1, "Python", 9]

second_reviewer = Reviewer("Майк", "Вазовски")
second_reviewer.rate_stud = [student_2, "Java", 8]

print('Список Ревьюеров: ')
print('Первый Ревьюер', '\n', first_reviewer)
print('Второй Ревьюер', '\n',second_reviewer)
print()
print('Список Лекторов: ')
print('Первый Лектор', '\n',first_lector)
print('Второй Лектор', '\n',second_lector)
print(f'Рейтинг 1 лектора выше рейтинга 2 лектора: {first_lector.__lt__(second_lector)}')
print()
print('Список Студентов: ')
print('Первый Студент', '\n', student_1)
print('Второй Студент', '\n', student_2)
print(f'Рейтинг 1 студента выше рейтинга 2 студента: {student_1.__lt__(student_2)}')

# def all_students(student, course):
#     sum_grades = 0
#     len = 0
#     for key, value in student.grade.items():
#         if course in key:
#             len += 1
#             sum_grades += sum(value) / len(value)
#         return  sum_grades
# all_students(student_1, 'Python')