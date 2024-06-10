# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и
# методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).


# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и
# методы (`make_sound()`, `eat()`) для всех животных.
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Bird(Animal):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def make_sound(self):
        print("Кря-кря!")

    def eat(self):
        print("Ест зернышки")

class Mammal(Animal):
    def __init__(self, name, age, area):
        super().__init__(name, age)
        self.food = area

    def make_sound(self):
        print("ррррррр!")

    def eat(self):
        print("Ест мясо")

class Reptile(Animal):
    def __init__(self, name, age, life):
        super().__init__(name, age)
        self.life = life

    def make_sound(self):
        print("ррррррр!")

    def eat(self):
        print("Ест мясо")

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

def animal_sound(animals):
    print(f"{animals.make_sound()}")


animals = [Bird("Лебедь Гоша", "1 год", "Белый"), Mammal("Тигрица Мая", "2 года", "Лес"),
           Reptile("Черепаха Тесс", "6 лет", "В воде")]
for animal in animals:
    animal_sound(animal)


# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Staff():
    def __init__(self, name, job):
        self.name = name
        self.job = job

class Zoo():
    def __init__(self, title = "Зоопарк"):
        self.title = title
        self.animal_list = []
        self.staff_list = []


    def add_bird(self, name, age, colour):
        new_bird = Bird(name, age, colour)
        self.animal_list.append(new_bird)
        print(f"В список добавлено новое животное - {new_bird.name}")

    def add_mammal(self, name, age, area):
        new_mammal = Mammal(name, age, area)
        self.animal_list.append(new_mammal)
        print(f"В список добавлено новое животное - {new_mammal.name}")

    def add_reptile(self, name, age, life):
        new_reptile = Reptile(name, age, life)
        self.animal_list.append(new_reptile)
        print(f"В список добавлено новое животное - {new_reptile.name}")

    def add_staff(self, name, job):
        new_staff = Staff(name, job)
        self.staff_list.append(new_staff)
        print(f"В список добавлен новый сотрудник - {new_staff.name}")


zoo = Zoo()
zoo.add_bird("Птица", "2 года", "черный")
zoo.add_staff("Иван", "Ветеринар")


# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).

class Zookeeper(Staff):
    def __init__(self, name, job):
        super().__init__(name, job)

    def feed_animal(self):
        print(f"{self.name}, {self.job}, кормит животное")


class Vet(Staff):
    def __init__(self, name, job):
        super().__init__(name, job)

    def heal_animal(self):
        print(f"{self.name}, {self.job}, лечит животное")


vet1 = Vet("Вика", "ветеринар")
vet1.heal_animal()

zookeeper1 = Zookeeper("Антон", "кипер")
zookeeper1.feed_animal()

