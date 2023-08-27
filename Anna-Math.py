import msvcrt
import random
import time
import keyboard


def emulate_print_cat(delay=0.05):

    text1 = '  ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n  ⠄⠄⠄⠄⠄⠄⢰⣷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n  ⠄⠄⠄⠄⣠⣾⣿⣿⣷⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n  ⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n'
    text2 = '  ⠄⠄⠄⠄⠛⠿⣿⣿⣿⣿⣿⣆⠄⠄⠄⠄⠄⣴⣿⣿⣆⠄⠄⠄\n  ⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣿⣿⣷⣄⠄⠄⠄⣿⣿⠛⠉⠄⠄⠄\n  ⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠄⠘⣿⡆⠄⠄⠄⠄\n  ⠄⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠸⣿⡀⠄⠄⠄\n'
    text3 = '  ⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⣿⡇⠄⠄⠄\n  ⠄⠄⠄⠄⠄⠄⢸⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣿⠇⠄⠄⠄\n  ⠄⠄⠄⠄⠄⢀⣸⡿⢁⣘⣿⣿⣿⣿⣿⣿⣿⣇⣼⠋⠄⠄⠄⠄\n  ⠄⠄⠄⠄⠄⠻⠿⠓⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠄⠄⠄⠄⠄\n'
    text4 = '  ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'

    text = text1 + text2 + text3 + text4

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def check_input(user_input):
    if user_input.isdigit():
        return True
    else:
        return False


def main():
    # Зададим количество решаемых примеров
    amount1 = 10

    start_time = time.time()
    amount_right_answers = 0
    amount_wrong_answers = 0
    while amount_right_answers < amount1:
        num1 = random.randint(11,99)
        num2 = random.randint(3,9)

        sign = random.randint(0,1)
        if sign:
            arithmetic_operator = "+"
            k = 1
        else:
            arithmetic_operator = "-"
            k = -1

        # ждем ввод и проверяем, что введено
        Stat1 = True

        while Stat1:
            print(f'{num1} {arithmetic_operator} {num2} = ', end='', flush=True)

            input_item2 = input()
            if check_input(input_item2):
                input_item = int(input_item2)
                Stat1 = False
            else:
                print('Вводи цифры, а не символы!')

        if input_item == num1 + num2 * k:
            amount_right_answers += 1
            print(f"Всего правильных ответов {amount_right_answers} из {amount1}\n")
        else:
            print("Ошибка! Правильный ответ =", num1 + num2 * k)
            amount_wrong_answers += 1
            if  amount_right_answers > 0:
                amount_right_answers -= 1
            print(f"Всего правильных ответов {amount_right_answers} из {amount1}\n")


    end_time = time.time()

    print('********************************')
    print('*        Аня, ты умничка!      *')
    print('*     Ты решила все задания!   *')


    # Вычислить время выполнения в секундах
    execution_time_seconds = end_time - start_time

    # Перевести время выполнения в минуты и секунды
    minutes = int(execution_time_seconds // 60)
    seconds = int(execution_time_seconds % 60)

    print(f"*   Время выполнения задания:  *")
    print(f"*        {minutes:>{2}} мин. {seconds:>{2}} сек.       *")
    print(f'*    Правильных ответов = {amount_right_answers:>{2}}   *')
    print(f'*    Количество  ошибок = {amount_wrong_answers:>{2}}   *')
    print('********************************')
    time.sleep(5)
    print()
    emulate_print_cat(0.01)


if __name__ == '__main__':
    main()


