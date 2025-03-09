# написать класс октагон найти радиус площядь описаной окружности
# написать радиус площадь вписаной окружности 
# найти площадь октагона и периметр всех фигур
# отрисовать все фигуры


import matplotlib.pyplot as plt
import math
import numpy as np

class Octagon:

    def __init__(self, side):  # Конструктор
        self.side = side
        self.R = side / ((2 - (2 ** (1 / 2))) ** (1 / 2))  # Радиус описанной окружности
        self.r = side / (2 * (2 ** (1 / 2) - 1))  # Радиус вписанной окружности

    def described(self):  # Описанная окружность
        area = math.pi * (self.R ** 2)  # Площадь описанной окружности
        print(f"Радиус описанной: {self.R}")
        print(f"Площадь описанной: {area}")

    def inscribed(self):  # Вписанная окружность
        area = math.pi * (self.r ** 2)  # Площадь вписанной окружности
        print(f"Радиус вписанной: {self.r}")
        print(f"Площадь вписанной: {area}")

    def square_octagon(self):  # Площадь и периметр октагона
        area = (2 * (self.side ** 2)) * (1 + (2 ** (1 / 2)))
        perimeter = 8 * self.side
        print(f"Площадь октагона: {area}")
        print(f"Периметр октагона: {perimeter}")

    def draw(self):  # рисовка
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect('equal')
        ax.set_xlim(-self.R * 1.5, self.R * 1.5)
        ax.set_ylim(-self.R * 1.5, self.R * 1.5)

        # Вершины октагона
        angle = np.linspace(0, 2 * np.pi, 9)
        x = self.R * np.cos(angle)
        y = self.R * np.sin(angle)

        ax.fill(x, y, label='Октагон')

        # Вписанная и описанная окружности
        ax.add_patch(plt.Circle((0, 0), self.r, color='blue', fill=False, label="Вписанная окружность"))
        ax.add_patch(plt.Circle((0, 0), self.R, color='red', fill=False, label="Описанная окружность"))

        plt.legend()
        plt.show()

    def __del__(self):  # Деструктор
        print("Объект удален")

def main():
    side = int(input("Введите длину стороны октагона: "))
    octagon = Octagon(side)

    octagon.described()
    octagon.inscribed()
    octagon.square_octagon()
    octagon.draw()

if __name__ == "__main__":
    main()
