from collections import deque
from random import choice

CAR, HEAD, ENERGY_CUBE = range(3)


class Train:
    def __init__(self):
        self.cars = deque([])
        self.cars.extend([CAR, CAR, ENERGY_CUBE, *[CAR] * 9, CAR, HEAD])

    current = property(lambda self: self.cars[-1])

    def press_the_button(self):
        if self.current != ENERGY_CUBE:
            print(f'you pressed it early :(')
        else:
            print(f'you pressed it right on time :D')
        exit()

    def __iter__(self):
        while True:
            self.cars.rotate(-1 if self.current == HEAD else choice([-1, 1]))
            yield

    def __repr__(self):
        visualization = '-'.join('HEAD' if it == HEAD else 'CAR' if it == CAR else 'ENERGY_CUBE' for it in self.cars)
        return f'<TRAIN: {visualization}>'


train = Train()

for _ in train:
    if train.current == ENERGY_CUBE:
        print(f'{train}')
        train.press_the_button()
