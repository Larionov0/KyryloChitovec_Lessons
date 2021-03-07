import random


class Hero:
    def __init__(self, name, hp, attack, armor, speed=3):
        self.name = name
        self.max_hp = self.hp = hp
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.is_alive = True

    def get_damage(self, damage):
        remaining_damage = damage - self.armor
        print(f'Герой {self.name} отримує {remaining_damage}/{damage} урона')
        if remaining_damage > 0:
            self.loose_hp(remaining_damage)

    def loose_hp(self, damage):
        self.hp -= damage
        print(f'Герой {self.name} втратив {damage} HP. Залишилось {self.hp} / {self.max_hp} HP')
        if self.hp <= 0:
            self.is_alive = False
            print(f'{self.name} DIED')

    def normal_attack(self, other_hero):
        print(f'{self.name} атакує {other_hero.name}')
        other_hero.get_damage(self.attack)

    def regen_hp(self, hp):
        self.hp += hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f'{self.name} відновив {hp} HP  ({self.hp} / {self.max_hp} HP)')


class Assasin(Hero):
    def __init__(self, name, hp, attack, armor, speed=3, crit_coef=2):
        super().__init__(name, hp, attack, armor, speed)
        self.crit_coef = crit_coef

    def normal_attack(self, other_hero):
        print(f'{self.name} атакує {other_hero.name}')
        damage = self.attack
        if random.randint(1, 100) <= 30:
            damage *= self.crit_coef
            print("*crit*")
        other_hero.get_damage(damage)


class Archer(Hero):
    def get_damage(self, damage):
        if random.randint(1, 100) <= 30:
            print(f'{self.name} відстрибнув від удару!')
            return
        super().get_damage(damage)


class Tank(Hero):
    pass


class Vampire(Hero):
    def __init__(self, name, hp, attack, armor, speed=3, regen_value=2):
        super().__init__(name, hp, attack, armor, speed)
        self.regen_value = regen_value

    def normal_attack(self, other_hero):
        super().normal_attack(other_hero)
        if random.randint(1, 100) <= 40:
            print('*п`є кров*')
            self.regen_hp(self.regen_value)


h1 = Archer('Archer', 13, 4, 1)
h2 = Assasin('Hunter', 15, 3, 2)
h3 = Hero('Puzan', 25, 2, 2)
h4 = Vampire('Pirlo', 12, 3, 1)


h2.normal_attack(h4)

for _ in range(10):
    h4.normal_attack(h2)
    print()
