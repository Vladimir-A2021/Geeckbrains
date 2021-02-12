class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.title}")


stationery = Stationery("")
stationery.draw()

a = Pen("ручкой")
a.draw()

b = Pencil("карандашом")
b.draw()

c = Handle("маркером")
c.draw()
