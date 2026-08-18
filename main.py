from calculator import calculator
from history import save_record, show_history, clear_history

def main():
    print("ДОБРО ПОЖАЛОВАТЬ В КАЛЬКУЛЯТОР!")
    print("Вам доступны команды:")
    print("  calc      - выполнить вычисление")
    print("  history   - показать историю")
    print("  clear     - очистить историю")
    print("  exit      - выход")
    print()

    while True:
        command = input("Введите команду: ").strip().lower()

        if command == "exit":
            print("До свидания!")
            break

        elif command == "history":
            show_history()

        elif command == "clear":
            clear_history()

        elif command == "calc":
            try:
                first_numbers = float(input("Введите первое число: "))
                second_numbers = float(input("Введите второе число: "))
                operator = input("Введите оператор [+, -, *, /, ^]: ").strip()

                result = calculator(first_numbers, second_numbers, operator)
                expression = f"{first_numbers} {operator} {second_numbers}"

                save_record(expression, result)

                print(f"Ответ: {result}\n")
            except ValueError:
                print("Ошибка! Введите корректное число.\n")
            except Exception as e:
                print(f"Произошла ошибка: {e}\n")
        else:
            print("Неизвестная команда. Доступны: calc, history, clear, exit.\n")

if __name__ == "__main__":
    main()