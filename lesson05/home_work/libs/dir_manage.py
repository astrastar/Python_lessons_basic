import os.path
import shutil


# создание заданного количества папок с именем dir_
# def make_dir(x):
#     for i in range(1, x + 1):
#         new_dir = os.mkdir('dir_{}'.format(i))
#
# создание папки с заданым именем
def make_dir(*names):
    try:
        for name in names:
            os.mkdir(name)
            print('Успешно создана папка {}'.format(name))
    except FileExistsError:
        print('Такая папка уже существует')


def remove_dir(*names):
    try:
        for name in names:
            os.rmdir(name)
            print('Папка {} успешно удалена'. format(name))
    except FileNotFoundError:
        print('Такой папки не существует')


def get_listdir():
    file_list = os.listdir()
    return file_list


def copy_curfile(dst_dir):
    shutil.copy(__file__, dst_dir)


def change_dir(dirname):
    try:
        os.chdir(dirname)
        print('Переход в директорию успешно осуществлен')
    except FileNotFoundError:
        print('Такой директории не существует')

# print(os.getcwd())
# make_dir('new1', 'new2', 'new')
# remove_dir('new', 'new2')


# def menu():
#     print('Привет, я умею делать такие штуки:')
#     print('1. Перейти в папку')
#     print('2. Посмотреть содержимое текущей папки')
#     print('3. Удалить папку')
#     print('4. Создать папку')
#     print('5. Выход из программы')
#     user_input = int(input('Введите желаемую команду: '))
#     if user_input == 1:
#         dirname = input('Введите нужную папку: ')
#         return dirname
#     # elif user_input == 2:
#     #     print(get_listdir())








