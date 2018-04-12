# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе



class Person():

    def __init__(self, lastname, firstname, middlename):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename

    def get_fullname(self):
        return self.lastname + ' ' + self.firstname + ' ' + self.middlename

    # @property
    def fio(self):
        return self.lastname + ' ' + self.firstname[0] + '.' + self.middlename[0] + '.'


class Student(Person):

    def __init__(self, lastname, firstname, middlename, mother, father):
        Person.__init__(self, lastname, firstname, middlename)
        # self.classroom = classroom
        # self.subject = subjects
        self.mother = mother
        self.father = father

    # получить ФИО родителей ученика
    @property
    def get_parents(self):
        return f'Мама {self.mother} \nПапа {self.father}'


    def get_mama(self):
        return f'Мама {self.mother}'


    def get_papa(self):
        return f'Папа {self.father}'



class Teacher(Person):

    def __init__(self, lastname, firstname, middlename, subject, *classes):
        Person.__init__(self, lastname, firstname, middlename)
        self.subject = subject
        self.classes = classes


class Classroom():

    class_list = []

    def __init__(self, class_name, *students):
        self.class_name = class_name
        self.students = students
        Classroom.class_list.append(class_name)  # получаем список всех классов в школе
        return Classroom.class_list.sort()

    # получить всех учеников класса
    def get_all_class_stds(self):
        print(f'Students of class {self.class_name}:')
        for student in self.students:
            print(student.fio())

    def append_tchs(self, *teachers):
        self.teachers = teachers

    def get_class_tchs(self):
        print(f'Teachers of Class {self.class_name}:')
        for teacher in self.teachers:
            print(teacher.fio())

    def get_subjects(self, student):
        print(f'Subjects of student {student.fio()}:')
        for teacher in self.teachers:
            print(teacher.subject)
    #
    # def get_all_class_tchs(self):
    #     for teacher in self.teachers:
    #         print(teacher.fio())


student = Student('Lastname', 'Name', 'Middle', 'Lastname Maria Vlad', 'Lastname Andr Nik')
student1 = Student('Petrov', 'Petr', 'Petrivich', 'Petrova Irina Ivan', 'Petrov Petr rrr')
class1 = Classroom('9 C', student, student1)
class2 = Classroom('9 B', student1)
teach1 = Teacher('Ivanov', 'Ivan', 'Ivanovich', 'math', class1, class2)
teach2 = Teacher('Borisov', 'Boris', 'Borisovich', 'geography')
class1.append_tchs(teach1, teach2)
print(class1.get_all_class_stds())
print(Classroom.class_list)
print(class1.get_class_tchs())
print(class1.get_subjects(student1))
