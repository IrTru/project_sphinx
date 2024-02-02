from module1 import funct_sum
from module2 import funct_diff
from module3 import funct_division
from module4 import funct_multiplication
from module5 import funct_degree

def main():

    """
    
    Это главная функция 'main'\n
    Отсюда начинает выполняться программа - "Калькулятор"

    В начале только надо будет ввести логин/пароль.

    """

    User_Name = input('Введите логин: ')
    if User_Name == 'ik':
        Password = input('Введите пароль: ')
        if Password == '1234':
            print('Вход выполнен успешно')
            calculator = input('Ты хочешь сделать вычисления ? ("yes"/"no"):')
            while calculator == 'yes':
                while True:
                    try:
                        num_a = int(input('Введите число A: '))
                        break
                    except:
                        print("Add Integer Value")
                while True:
                    try:
                        num_b = int(input('Введите число B: '))
                        break
                    except:
                        print("Add Integer Value")

                list_actions = {
                    '+' : 'Сложение', 
                    '-' : 'Разность',
                    '/' : 'Деление',
                    '*' : 'Умножение',
                    '**' : 'Степень',
                }
                print(' -------------------- ')
                for elem in list_actions:
                    print(elem,'-', list_actions.get(elem))
                print(' -------------------- ')

                vibor = input('Выберите нужное действие:')
                if vibor == '+':
                    itog = funct_sum(num_a, num_b)
                elif vibor == '-':
                    itog = funct_diff(num_a, num_b)
                elif vibor == '/':
                    itog = funct_division(num_a, num_b)
                elif vibor == '*':
                    itog = funct_multiplication(num_a, num_b)
                elif vibor == '**':
                    itog = funct_degree(num_a, num_b)
                calculator = input('Ты хочешь еще сделать вычисления?("yes"/"no"):')  
            print('Программа завершена!')
        else:
            print('Неверный пароль!')
    else:
        print('Неверный логин!')


if __name__ == '__main__':
    main()