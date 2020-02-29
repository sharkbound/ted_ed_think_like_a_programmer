from collections import Counter, deque
from enum import Enum, auto
from random import shuffle, randint, choice


class Type(Enum):
    A = auto()
    B = auto()
    C = auto()
    E = auto()
    D = auto()

    def __repr__(self):
        return self.name


def generate_data():
    values = list(Type)
    out = []
    added = 0
    while added < 12:
        r = choice((2, 4, 6))
        out.extend([choice(values)] * r)
        added += r

    out.append(choice(values))
    shuffle(out)
    return out


data = generate_data()
left = deque()
right = deque()
mid = next((v for v in data if data.count(v) & 1))

data.remove(mid)
while data:
    value = data.pop()
    data.remove(value)
    left.append(value)
    right.appendleft(value)

print(left + deque([mid]) + right)
