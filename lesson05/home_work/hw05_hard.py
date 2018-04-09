# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import sys
import os
import shutil
from libs import dir_manage_2 as dm


print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')
    print("ping - тестовый ключ")
    print('exit - выход из программы')
#
# do = {
#     "help": print_help(),
#     "mkdir": dm.make_dir(),
#     "cp": dm.copy_file(),
#     "rm": dm.remove_file(),
#     "cd": dm.change_dir(),
#     "ls": dm.curdir(),
#     "ping": dm.ping()
# }
# print_help()

# не до конца разобрался в задании, в итоге получилось почти копия normal, да еще и цикл неправильно работает

def main():

    while True:
        try:
            if sys.argv[1] == 'help':
                print_help()
            elif sys.argv[1] == 'mkdir':
                dm.make_dir()
            elif sys.argv[1] == 'cp':
                dm.copy_file()
            elif sys.argv[1] == 'rm':
                dm.remove_file()
            elif sys.argv[1] == 'cd':
                dm.change_dir()
            elif sys.argv[1] == 'ls':
                dm.curdir()
            elif sys.argv[1] == 'ping':
                dm.ping()
            elif sys.argv[1] == 'exit':
                print('Программа завершена')
                break
        except ValueError:
            print('Введена неверная команда')


main()
