from collections import deque
from random import randint, randrange

import numpy as np


class Picture:
    def __init__(self):
        self.width = self.height = randint(11, 201)
        self.grid = np.zeros((self.height, self.width))
        self._valid_range = range(self.width)

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __contains__(self, item):
        return item in self._valid_range


class Bot:
    def __init__(self):
        self.picture = Picture()
        self.y = randrange(self.picture.height)
        self.x = randrange(self.picture.width)

    def move(self, xoff, yoff):
        valid = all(v in self.picture for v in (xoff + self.x, yoff + self.y))
        if not valid:
            return False

        self.x += xoff
        self.y += yoff
        return True

    def up(self, times=1):
        return self.move(0, -1 * times)

    def down(self, times=1):
        return self.move(0, 1 * times)

    def left(self, times=1):
        return self.move(-1 * times, 0)

    def right(self, times=1):
        return self.move(1 * times, 0)

    def paint(self, new_value=1):
        self.picture[self.y, self.x] = new_value

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.x=} {self.y=}>'


def graph(bot: Bot):
    import matplotlib.pyplot as plt
    plt.imshow(bot.picture.grid)
    plt.show()


def paint_x(bot: Bot):
    # get to 0,0
    while bot.up(): pass
    while bot.left(): pass

    grids = deque((bot.picture.grid,))
    while grids:
        grid = grids.popleft()
        if grid.shape == (1, 1):
            bot.paint()
            break

        bot.paint()
        bot.right(grid.shape[1] - 1)
        bot.paint()
        bot.down(grid.shape[0] - 1)
        bot.paint()
        bot.left(grid.shape[1] - 1)
        bot.paint()
        bot.up(grid.shape[0] - 2)
        bot.right()
        grids.append(grid[1:-1, 1:-1])

    # alternative solution:
    #
    # while bot.up(): pass
    # while bot.left(): pass
    #
    # bot.paint()
    # while bot.down() and bot.right():
    #     bot.paint()
    #
    # while bot.up(): pass
    #
    # bot.paint()
    # while bot.down() and bot.left():
    #     bot.paint()

    graph(bot)


paint_x(Bot())
