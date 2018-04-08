# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os.path


# создание заданного количества папок с именем dir_
def make_dir(x):
    for i in range(1, x + 1):
        new_dir = os.mkdir('dir_{}'.format(i))

# создание папки с заданым именем


def make_dir(*names):
    for name in names:
        new_dir = os.mkdir(name)
        print('Успешно создана папка {}'.format(name))




def remove_dir(*names):
    for name in names:
        os.rmdir(name)
        print('Папка {} успешно удалена'. format(name))
#
# make_dir('a', 'b', 'c')
# print(os.listdir('.'))
# remove_dir('a', 'b', 'c')


def get_listdir(dir):
    file_list = os.listdir(dir)
    return file_list


def copy_curfile():
    open('{}_copy.py'.format(__file__[:-3]), 'w')


# copy_curfile()
