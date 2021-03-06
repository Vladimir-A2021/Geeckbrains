class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"{self.name} {self.surname}, {self.position}")

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


a = Position("Вася", "Крюков", "механик", 100, 20)
a.get_full_name()
print(f"Доход с учетом премии: {a.get_total_income()}")
