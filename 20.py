from abc import ABC
from abc import abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def info(self) -> str:
        pass

    def __str__(self):
        return self.info()



class Mammal(Animal):
    def __init__(self, name: str, habitat: str):
        super().__init__(name)
        self.habitat = habitat

    def make_sound(self) -> str:
        return "Издает звук млекопитающего"

    def info(self) -> str:
        return f"Млекопитающее: {self.name}, обитает в {self.habitat}"


class Ungulate(Mammal):
    def __init__(self, name: str, habitat: str, weight_kg: float):
        super().__init__(name, habitat)
        self.weight_kg = weight_kg

    def make_sound(self) -> str:
        return "Мууу!" if "корова" in self.name.lower() else "Иго-го!" if "лошадь" in self.name.lower() else "Ууу!"

    def info(self) -> str:
        return f"Парнокопытное: {self.name}, обитает в {self.habitat}, вес ≈ {self.weight_kg} кг"


class Bird(Animal):
    def __init__(self, name: str, can_fly: bool):
        super().__init__(name)
        self.can_fly = can_fly

    def make_sound(self) -> str:
        return "Чирик!" if self.can_fly else "Ко-ко!"

    def info(self) -> str:
        flight = "может летать" if self.can_fly else "не летает"
        return f"Птица: {self.name}, {flight}"


# Реестр животных
class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Животное '{animal.name}' добавлено в реестр.")

    def list_all(self):
        if not self.animals:
            print("Реестр пуст.")
            return
        print("\nСодержимое реестра:")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal}")

    def demonstrate_polymorphism(self):
        if not self.animals:
            print("Нет животных для демонстрации полиморфизма.")
            return
        print("\nДемонстрация полиморфизма:")
        for animal in self.animals:
            print(f"- {animal.name}: {animal.make_sound()}")


# Основное меню
def main():
    registry = AnimalRegistry()

    while True:
        print("\n" +"========================================")
        print("РЕЕСТР ЖИВОТНЫХ")
        print("=============================================")
        print("1. Добавить млекопитающее")
        print("2. Добавить парнокопытное")
        print("3. Добавить птицу")
        print("4. Просмотреть все животные")
        print("5. Продемонстрировать полиморфизм")
        print("6. Завершить работу")
        choice = input("Выберите действие (1–6): ").strip()

        if choice == '1':
            name = input("Введите имя млекопитающего: ").strip()
            habitat = input("Где он обитает? ").strip()
            registry.add_animal(Mammal(name, habitat))

        elif choice == '2':
            name = input("Введите имя парнокопытного: ").strip()
            habitat = input("Где он обитает? ").strip()
            try:
                weight = float(input("Вес в килограммах: "))
                registry.add_animal(Ungulate(name, habitat, weight))
            except ValueError:
                print("Животное не добавлено.")

        elif choice == '3':
            name = input("Введите имя птицы: ").strip()
            fly = input("Может летать? (да/нет): ").strip().lower()
            can_fly = fly in ('да', 'yes', 'y', 'д')
            registry.add_animal(Bird(name, can_fly))

        elif choice == '4':
            registry.list_all()

        elif choice == '5':
            registry.demonstrate_polymorphism()

        elif choice == '6':
            print("Выход")
            break

        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()