print(' КАЛЬКУЛЯТОР '.center(30, '*'))

while True:
    try:
        a, b = map(int ,input('Введіть два числа через пропуск: ').split(' '))
    except:
        print('Не коректне введення.')
        continue
    print(f'''
Оберіть дію для чисел {a} та {b}:
    0. Вихід:
    1. Додавання:   {a} + {b}
    2. Віднімання:  {a} - {b}
    3. Множення:    {a} * {b}
    4. Ділення:     {a} : {b}
    5. Піднесення числа {a} до степеня {b}
    6. Сума квадратів чисел {a} та {b}
    7. Різниця квадратів чисел {a} та {b}
    8. Квадрат суми чисел {a} та {b}
    9. Квадрат різниці чисел {a} та {b}
    10. Усі парні числа між {a} та {b}
    11. Усі не парні числа між {a} та {b}
    ''')
    user_choice = input('> Ваш вибір: ')

    if user_choice == '0':
        break








