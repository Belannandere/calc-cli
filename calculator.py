def calculator(first_numbers, second_numbers, operator):

    match operator:
        case '+':
            return first_numbers + second_numbers
        case '-':
            return first_numbers - second_numbers
        case '*':
            return first_numbers * second_numbers
        case '/':
            if second_numbers == 0:
                return "Ошибка: деление на ноль"
            return first_numbers / second_numbers
        case '^' | '**':
            return first_numbers ** second_numbers
        case _:
            return "Неизвестный оператор"