from os import system
import random
import msvcrt

n = 18
m = 18
sym = '-'

# Створення матриці
matrix = []
i = 0
while i < n:
    row = []
    j = 0
    while j < m:
        row.append(sym)
        j += 1
    matrix.append(row)
    i += 1


hero_face = '+'
hero_hp = hero_max_hp = 100
hero_coords = [1, 1]
hero_details = 0


animals = [
    ['курка', 'Ryaba', 'k', 3, [1, 5]],
    ['курка', 'Boba', 'k', 3, [1, 6]],
    ['курка', 'Biba', 'k', 3, [2, 5]]
]


while True:
    # кладемо всіх істот на нові позиції в матриці
    matrix[hero_coords[0]][hero_coords[1]] = hero_face
    for animal in animals:  # ['курка', 'Ryaba', 'k', 3, [1, 5]]
        animal_coords = animal[4]
        matrix[animal_coords[0]][animal_coords[1]] = animal[2]

    # виведення матриці на екран
    system('cls')
    for row in matrix:  # [4, 2, 5, 4]
        text = '|'
        for el in row:
            text += str(el) + " "
        text = text[:-1] + "|"
        print(text)

    # затирання минулих позицій
    matrix[hero_coords[0]][hero_coords[1]] = '-'
    for animal in animals:  # ['курка', 'Ryaba', 'k', 3, [1, 5]]
        animal_coords = animal[4]
        matrix[animal_coords[0]][animal_coords[1]] = '-'

    # Хід гравця
    print("--= Головне меню =--")
    print(f"Здоров'я: {hero_hp}/{hero_max_hp}. Деталі: {hero_details}")
    print("WASD: ")
    choice = msvcrt.getch().decode().upper()
    if choice == 'W':
        if hero_coords[0] != 0:
            hero_coords[0] -= 1
    elif choice == 'A':
        if hero_coords[1] != 0:
            hero_coords[1] -= 1
    elif choice == 'S':
        if hero_coords[0] != n - 1:
            hero_coords[0] += 1
    elif choice == 'D':
        if hero_coords[1] != m - 1:
            hero_coords[1] += 1

    # Чи зловив курку
    dead_kurki = []
    for animal in animals:
        if animal[0] == 'курка':
            if animal[4] == hero_coords:
                hero_details += 3
                dead_kurki.append(animal)
    for kurka in dead_kurki:
        animals.remove(kurka)

    # Хід тварин
    for animal in animals:
        if animal[0] == 'курка':
            choice = random.choice(['W', 'A', 'S', 'D'])  # курка вибирає випадкову сторону зі списку
            animal_coords = animal[4]
            if choice == 'W':
                if animal_coords[0] != 0:
                    animal_coords[0] -= 1
            elif choice == 'A':
                if animal_coords[1] != 0:
                    animal_coords[1] -= 1
            elif choice == 'S':
                if animal_coords[0] != n - 1:
                    animal_coords[0] += 1
            elif choice == 'D':
                if animal_coords[1] != m - 1:
                    animal_coords[1] += 1
        elif animal[0] == 'качка':
            pass

    # Чи зловив курку
    dead_kurki = []
    for animal in animals:
        if animal[0] == 'курка':
            if animal[4] == hero_coords:
                hero_details += 3
                dead_kurki.append(animal)
    for kurka in dead_kurki:
        animals.remove(kurka)
