class Human:
    name = 'Newman'
    sex = 'm'
    skin_color = 'yellow'
    age = 0
    money = 0

    def say_hi(self):
        print(f'{self.name}: Hello')

    def say_hi_to_other_human(self, other_human):
        print(f'{self.name}: Hello, {other_human.name}')

    def grow_up(self):
        self.age += 1
        if self.sex == 'm':
            print(f"{self.name} підріс на рік. Тепер йому {self.age} років")
        else:
            print(f"{self.name} підросла на рік. Тепер їй {self.age} років")


hum1 = Human()
hum1.name = 'Bob'
hum1.age = 21
hum1.sex = 'm'
hum1.skin_color = 'white'

hum2 = Human()
hum2.name = 'Alise'
hum2.sex = 'f'
hum2.age = 18


hum1.grow_up()
hum2.grow_up()
