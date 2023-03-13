class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self, grades):
        a = 0
        b = 0
        for key in grades:
            a += (len(grades[key]))
            b += (sum(grades[key]))
        return round(b / a, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return {self.average_grade(self.grades)} > {other.average_grade(other.grades)}

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_grade(self.grades)}'
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return {self.average_grade(self.grades)} > {other.average_grade(other.grades)}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def score(self):
        self.grades = {}

    def average_grade(self, grades):
        a = 0
        b = 0
        for key in grades:
            a += (len(grades[key]))
            b += (sum(grades[key]))
        return round(b / a, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return {self.average_grade(self.grades)} > {other.average_grade(other.grades)}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return {self.average_grade(self.grades)} > {other.average_grade(other.grades)}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade(self.grades)} '
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if not isinstance(student,
                          Student) or course not in self.courses_attached or course not in student.courses_in_progress:
            return 'Ошибка'
        else:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


stud_one = Student('Ryan', 'Gosling', 'Man')
stud_one.finished_courses = ['Введение в программирование']
stud_one.courses_in_progress = ['Python', 'Git']
stud_two = Student('Alyson', 'Hannigan', 'Woman')
stud_two.finished_courses = ['Введение в программирование']
stud_two.courses_in_progress = ['Python', 'Git']

lect_one = Lecturer('Steven', 'Buscemi')
lect_one.courses_attached = ['Python']
lect_two = Lecturer('Nikolai', 'Nosov')
lect_two.courses_attached = ['Git']

rev_one = Reviewer('Serj', 'Tankian')
rev_one.courses_attached = ['Python']
rev_two = Reviewer('Mikhail', 'Chernyak')
rev_two.courses_attached = ['Git']

rev_one.rate_hw(stud_one, 'Python', 10)
rev_one.rate_hw(stud_two, 'Python', 9)
rev_two.rate_hw(stud_one, 'Git', 8)
rev_two.rate_hw(stud_two, 'Git', 7)

stud_one.rate_lecturer(lect_one, 'Python', 6)
stud_one.rate_lecturer(lect_two, 'Git', 5)
stud_two.rate_lecturer(lect_one, 'Python', 4)
stud_two.rate_lecturer(lect_two, 'Git', 3)

print('Ревьюеры: ')
print(rev_one)
print(rev_two)
print()

print('Лекторы:')
print(lect_one)
print(lect_two)
print()

print('Студенты:')
print(stud_one)
print(stud_two)
print()

print('Лучший лектор по средней оценке за лекций:')
if lect_one.average_grade(lect_one.grades) > lect_two.average_grade(lect_two.grades):
    print(f'{lect_one.name} {lect_one.surname} - {lect_one.average_grade(lect_one.grades)}')
else:
    print(f'{lect_two.name} {lect_two.surname} - {lect_two.average_grade(lect_two.grades)}')
print()
print('Лучший студент по средней оценке за домашнее задание:')
if stud_one.average_grade(stud_one.grades) > stud_two.average_grade(stud_two.grades):
    print(f'{stud_one.name} {stud_one.surname} - {stud_one.average_grade(stud_one.grades)}')
else:
    print(f'{stud_two.name} {stud_two.surname} - {stud_two.average_grade(stud_two.grades)}')
print()


def avg_course(list_avg, course):
    sum_g = 0
    len_g = 0
    for instance in list_avg:
        if course in instance.grades.keys():
            sum_g += sum(list(map(int, instance.grades[course])))
            len_g += len(list(map(int, instance.grades[course])))
    avg = round(sum_g / len_g, 1)
    return avg


print(
    f'Средняя оценка за курс Git среди студентов: {avg_course(Student.student_list, "Git")}')
print(
    f'Средняя оценка за курс Git среди лекторов: {avg_course(Lecturer.lecturer_list, "Git")}')
print(
    f'Средняя оценка за курс Python среди студентов: {avg_course(Student.student_list, "Python")}')
print(
    f'Средняя оценка за курс Python среди лекторов: {avg_course(Lecturer.lecturer_list, "Python")}')
