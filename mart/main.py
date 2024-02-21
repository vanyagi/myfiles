import lab1
from lab1 import exc1_1, exc1_2



def main():
    choose_lab = int(input("Введите номер лабораторной работы которую хотите выполнить: "))
    if choose_lab == 1:
        choose_exc = int(input("Введите номер задания которое хотите выполнить: "))
        if choose_exc == 1:
            exc1_1()
        elif choose_exc == 2:
            exc1_2()
        else:
            print("Ошибка! Такого задания нет, попробуйте снова")

while 1 > 0:
    main()