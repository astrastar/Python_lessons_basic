import os.path
import shutil


def make_dir():
    try:
        dir_name = input('Введите название папки')
        os.mkdir(dir_name)
        print('Успешно создана папка {}'.format(dir_name))
    except FileExistsError:
        print('Такая папка уже существует')


def change_dir(dirname):
    try:
        os.chdir(dirname)
        print('Переход в директорию успешно осуществлен')
    except FileNotFoundError:
        print('Такой директории не существует')


def copy_file():
    try:
        file_name = input('Какой файл копировать?')
        dst_dir = input('Куда следует скопировать?')
        shutil.copy(file_name, dst_dir)
        print('Файл {} успешно скопирован'.format(file_name))
    except FileNotFoundError:
        print('Такого файла не существует')


def remove_file():
    try:
        file_name = input('Какой файл нужно удалить?')
        agree = input('Вы уверены, что хотите удалить файл {}, да/нет?'.format(file_name))
        if agree == 'да':
            os.remove(file_name)
        elif agree == 'нет':
            print('Файл {} не будет уален'.format(file_name))
        else:
            print('Введена неверная команда, введите да или нет')
    except FileNotFoundError:
        print('Такого файла не существует')


def change_dir():
    try:
        new_dir = input('Ведите новую директорию')
        os.chdir(new_dir)
        print('Директория успешно изменена')
    except FileNotFoundError:
        print('Такой папки не существует')



def curdir():
    print('Текущая директоря: {}'.format(os.getcwd()))

def ping():
    print('pong')



