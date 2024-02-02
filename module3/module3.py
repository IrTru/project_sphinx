
def funct_division(num_a:int, num_b:int):
    """
    
    Это функция 'Деления'\n
    param num_a (a) : int\n
    param num_b (b) : int\n
    param itog (c) : str\n

    """


    if int(num_b) == 0:
        itog = '-' 
        print('Деление на 0 запрещено!')      
    else:
        itog = str(num_a/num_b)
        print('Деление: ' + itog)
    return itog