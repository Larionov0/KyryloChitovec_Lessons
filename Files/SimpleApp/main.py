from random import randint
from time import sleep
from os import system


FILENAME = 'savings.txt'


def save_data(money, satiety, things):
    file = open(FILENAME, 'wt', encoding='utf-8')

    file.write(f"{money}\n{satiety}\n")
    last_line = ''
    for item in things:
        last_line += item + ', '
    last_line = last_line[:-2]
    file.write(last_line)

    file.close()


def load_data():
    file = open(FILENAME, 'rt', encoding='utf-8')

    line1 = file.readline().rstrip()
    line2 = file.readline().rstrip()
    line3 = file.readline()  # 'штани, кепка, ...'

    file.close()

    money = int(line1)
    satiety = int(line2)
    things = line3.split(', ')
    return money, satiety, things


DEBUG = True
is_autosave = True

try:
    money, satiety, things = load_data()
except:   # (FileNotFoundError, ValueError)
    things = ['штани', "кепка"]
    money = 10
    satiety = max_satiety = 10

store = [
    ['тапки', 40],
    ['футболка', 100]
]

while True:
    if is_autosave:
        save_data(money, satiety, things)
    system('cls')
    text = "--= Головне меню =--\n" \
           f"Ваші гроші: {money}  Ситість: {satiety} \n" \
           f"Ваші речі: {things}\n\n" \
           "1 - магазин\n" \
           "2 - піти на заробітки\n" \
           "3 - побитися з іншим бомжем\n" \
           "4 - вихід з програми\n"
    if DEBUG:
        text += '999 - чіти (нікому не кажіть)\n'
    text += "Ваш вибір: "

    choice = input(text)
    if choice == '1':
        while True:
            system('cls')
            text = "--= Вибір магазину =--\n" \
                   "0 - вихід\n" \
                   "1 - гастроном\n" \
                   "2 - Епіцентр\n" \
                   "Ваш вибір: "
            choice = input(text)
            if choice == '0':
                break
            if choice == '1':
                pass
            elif choice == '2':
                while True:
                    system('cls')
                    text = "--= Магазин =--\n" \
                           f"Ваші гроші: {money}  Ситість: {satiety} \n" \
                           f"Ваші речі: {things}\n\n" \
                           "0 - вихід з магазину\n" \
                           "1 - тапки (40 грн)\n" \
                           "2 - телефон (200 грн)\n" \
                           "3 - спортивний костюм (300 грн)\n" \
                           "Ваш вибір: "
                    choice = input(text)

                    if choice == '0':
                        break

                    if choice == '1':
                        if money >= 40:
                            money -= 40
                            things.append('тапки')
                            print(f"Ви купили: тапки. Було витрачено 40 грн.")
                        else:
                            print('У вас недостатньо грошей')
                        input("\n\n<Enter>")

                    elif choice == '2':
                        if money >= 200:
                            money -= 200
                            things.append('телефон')
                            print(f"Ви купили: телефон. Було витрачено 200 грн.")
                        else:
                            print('У вас недостатньо грошей')
                        input("\n\n<Enter>")

                    elif choice == '3':
                        if money >= 300:
                            money -= 300
                            things.append('спортивний костюм')
                            print(f"Ви купили: спортивний костюм. Було витрачено 300 грн.")
                        else:
                            print('У вас недостатньо грошей')
                        input("\n\n<Enter>")

    elif choice == '2':
        while True:
            system('cls')
            text = "--= На заробітках =--\n" \
                   f"Ваші гроші: {money}  Ситість: {satiety} \n" \
                   f"Ваші речі: {things}\n\n" \
                   "0 - назад до головного меню\n" \
                   "1 - збирати пляшки (4 - 15 грн)\n" \
                   "2 - ритися в смітниках (пошук речей)\n" \
                   "3 - працювати гружчиком (40 грн) (потрібне взуття)\n" \
                   "4 - працювати менеджером (150 грн) (потрібні: костюм, телефон)\n" \
                   "Ваш вибір: "
            choice = input(text)

            if choice == '0':
                break
            if choice == '1':
                print('Бомж шукає пляшки...')
                sleep(3)
                zar = randint(4, 15)
                money += zar
                print(f"Ви нашукали пляшок на {zar} грн. Тепер у вас {money} грн")
                input("\n\n<Enter>")
            elif choice == '2':
                pass
            elif choice == '3':
                if 'тапки' in things:
                    input('Перетаскуємо ящики...')
                    input("Тягаємо мішки...")
                    input("Таскаємо машини...")
                    input('Мішаємо ящики...')
                    print("Чистимо взуття начальнику")
                    sleep(2)
                    zar = 40
                    money += zar
                    print(f"Ви заробили {zar} грн")
                else:
                    print("У вас не вистачає речей.")
                input("\n\n<Enter>")
            elif choice == '4':
                if 'спортивний костюм' in things and 'телефон' in things:
                    print("Ви подзвонили клієнту. Привітайтесь:")
                    answer = input()
                    if answer in ['привіт', "добрий день", "доброго дня", "доброго ранку"]:
                        print("Клієнт думає над покупкою...")
                        answer = input("Переконайте його: ")
                        if 'акція' in answer or 'вигідно' in answer or 'пропозиція' in answer:
                            print("Клієнт приймає остаточне рішення...")
                            sleep(2)
                            if randint(1, 100) <= 70:
                                print('Успішна операція')
                                zar = 250
                                money += zar
                                print(f'Ви заробили {zar} грн')
                            else:
                                zar = 50
                                money += zar
                                print(f'Клієнт зірвався... Ваша ставка {zar}')
                        else:
                            print("Клієнт приймає остаточне рішення...")
                            sleep(2)
                            if randint(1, 100) <= 30:
                                print('Успішна операція')
                                zar = 250
                                money += zar
                                print(f'Ви заробили {zar} грн')
                            else:
                                zar = 50
                                money += zar
                                print(f'Клієнт зірвався... Ваша ставка {zar}')
                    elif 'пішов ти' in answer or 'дурень' in answer:
                        print("Ви нагрубили клієнту!!!!")
                        shtraf = 100
                        print(f"Штраф: {shtraf} грн")
                        money -= shtraf
                    else:
                        print("Клієнт приймає остаточне рішення...")
                        sleep(2)
                        if randint(1, 100) <= 10:
                            print('Успішна операція')
                            zar = 250
                            money += zar
                            print(f'Ви заробили {zar} грн')
                        else:
                            zar = 50
                            money += zar
                            print(f'Клієнт зірвався... Ваша ставка {zar}')
                else:
                    print("У вас не вистачає речей.")
                input("\n\n<Enter>")

    elif choice == '3':
        pass
    elif choice == '4':
        save_data(money, satiety, things)
        break
    elif choice == '999' and DEBUG:
        while True:
            system('cls')
            text = "--= Чіти =--\n" \
                   f"Ваші гроші: {money}  Ситість: {satiety} \n" \
                   f"Ваші речі: {things}\n\n" \
                   "0 - назад\n" \
                   "1 - підняти грошей\n"
            choice = input(text)

            if choice == '0':
                break
            elif choice == '1':
                u_money = int(input('Скільки грошей потрібно: '))
                money += u_money
    else:
        pass

