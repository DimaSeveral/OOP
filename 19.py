class Engineer:
    def __init__(self, name, qualification):
        self.name = name
        self.qualification = qualification

    def __str__(self):
        return f'Инженер: ФИО "{self.name}", квалификация "{self.qualification}"'


class Machine:
    def __init__(self, model, machine_type):
        self.model = model
        self.machine_type = machine_type

    def __str__(self):
        return f'Машина: модель "{self.model}", тип "{self.machine_type}"'


class ComputingCenter:
    def __init__(self, name, engineer, machines):
        self.name = name
        self.engineer = engineer          # агрегация: один инженер
        self.machines = machines          # агрегация: список машин

    def __str__(self):
        machines_str = "\n    ".join(str(m) for m in self.machines) if self.machines else "Нет машин"
        return (f'Вычислительный центр: "{self.name}"\n'
                f'  Ответственный: {self.engineer.name}\n'
                f'  Машины:\n    {machines_str}')


def main():
    centers = []  # реестр объектов первого порядка

    while True:
        print("\n" + "="*50)
        print("Меню:")
        print("1. Создать новый вычислительный центр")
        print("2. Вывести список всех вычислительных центров")
        print("3. Вывести представление конкретного объекта")
        print("4. Завершить работу")
        choice = input("Выберите пункт меню (1-4): ").strip()

        if choice == '1':
            # Создание инженера
            eng_name = input("Введите ФИО инженера: ").strip()
            eng_qual = input("Введите квалификацию инженера: ").strip()
            engineer = Engineer(eng_name, eng_qual)

            # Создание машин
            machines = []
            while True:
                add_machine = input("Добавить машину? (да/нет): ").strip().lower()
                if add_machine in ('нет', 'n', 'no'):
                    break
                model = input("  Модель машины: ").strip()
                mtype = input("  Тип машины: ").strip()
                machines.append(Machine(model, mtype))

            center_name = input("Введите название вычислительного центра: ").strip()
            center = ComputingCenter(center_name, engineer, machines)
            centers.append(center)
            print(f"Вычислительный центр '{center_name}' успешно создан!")

        elif choice == '2':
            if not centers:
                print("Нет созданных вычислительных центров.")
            else:
                print("\nСписок вычислительных центров:")
                for i, center in enumerate(centers, 1):
                    print(f"{i}. {center.name}")

        elif choice == '3':
            if not centers:
                print("Нет объектов для отображения.")
                continue

            print("\nВыберите вычислительный центр (введите номер):")
            for i, center in enumerate(centers, 1):
                print(f"{i}. {center.name}")

            try:
                idx = int(input("Номер центра: ").strip()) - 1
                if idx < 0 or idx >= len(centers):
                    print("Неверный номер.")
                    continue
            except ValueError:
                print("Введите корректное число.")
                continue

            center = centers[idx]
            print("\nЧто вывести?")
            print("1. Представление вычислительного центра")
            print("2. Представление инженера")
            print("3. Представление одной из машин")

            sub_choice = input("Ваш выбор (1-3): ").strip()
            if sub_choice == '1':
                print("\n" + str(center))
            elif sub_choice == '2':
                print("\n" + str(center.engineer))
            elif sub_choice == '3':
                if not center.machines:
                    print("В этом центре нет машин.")
                else:
                    print("\nВыберите машину:")
                    for i, m in enumerate(center.machines, 1):
                        print(f"{i}. {m.model} ({m.machine_type})")
                    try:
                        m_idx = int(input("Номер машины: ").strip()) - 1
                        if 0 <= m_idx < len(center.machines):
                            print("\n" + str(center.machines[m_idx]))
                        else:
                            print("Неверный номер машины.")
                    except ValueError:
                        print("Введите корректное число.")
            else:
                print("Неверный выбор.")

        elif choice == '4':
            print("Завершение работы")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите 1–4.")


if __name__ == "__main__":
    main()
    