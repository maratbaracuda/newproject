class Car:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

if __name__ == '__main__':
    car1 = Car('Porsche', 'white', 'automat')
    car2 = Car('Mitsubishi', 'Blue', 'mechanics')
    print(car1)
    print(car2)