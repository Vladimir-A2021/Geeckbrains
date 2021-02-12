class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            return f"Машина поехала"

    def stop(self):
        if self.speed == 0:
            return f"Машина остановилась"

    def turn_rith(self):
        return f"Поворо направо"

    def turn_left(self):
        return f"Поворот налево"

    def show_speed(self):
        return f"Скорость - {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f"Автомобиль - {self.name}, {self.color}, скорость - {self.speed}")


    def show_speed(self):
        if self.speed > 60:
            return f"Превышение скорости"
        else:
            return f"Превышения скорости нет"

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f"Автомобиль - {self.name}, {self.color}, скорость - {self.speed}")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f"Автомобиль - {self.name}, {self.color}, скорость - {self.speed}")

    def show_speed(self):
        if self.speed > 40:
            return f"Превышение скорости"
        else:
            return f"Превышения скорости нет"

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f"Автомобиль - {self.name}, {self.color}, скорость - {self.speed}")



t_c = TownCar(30, "green", "Kia")
t_c.show_speed()
print(t_c.go())
print(t_c.show_speed())


w_c = WorkCar(50, "black", "Toyota")
print(w_c.go())
w_c.show_speed()
print(w_c.show_speed())

p_c = PoliceCar(0, "white", "Lada")
print(p_c.stop())

s_c = SportCar(200, "yellow", "Ferrari")
print(s_c.turn_left())