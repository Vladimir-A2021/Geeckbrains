class Road:

    def __init__(self, length:int, width:int, massf_1=25, thickness=5):
        self._length = length
        self._width = width
        self.massf_1 = massf_1
        self.thickness = thickness


    def massf(self):
        return (self._length * self._width * self.massf_1 * self.thickness) // 1000

road = Road(5000, 20)
print(f"Масса асфальта = {road.massf()} т.")