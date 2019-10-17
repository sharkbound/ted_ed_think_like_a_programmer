from random import randint
from statistics import mean

from stringutil import auto_str_filtered


def rand_dial_position():
    return randint(1, 100)


def sign(i):
    return -1 if i < 0 else 0 if not i else 1


@auto_str_filtered('correct_position'.__ne__)
class Lock:
    POSITION_COUNT = 100

    def __init__(self):
        self.reset()

    def reset(self):
        self.correct_position = rand_dial_position()
        self.current_position = rand_dial_position()
        self.recorded_dial_position = self.current_position
        self.step_count = 0

    def _inc_step(self):
        self.step_count += 1

    def spin(self, rotation: int):
        if not rotation:
            return

        self.current_position = (self.current_position + rotation) % (self.POSITION_COUNT + 1)

        if not self.current_position:
            self.current_position = 100 if rotation < 0 else 1

        if rotation:
            self._inc_step()

    def record(self):
        self.recorded_dial_position = self.current_position
        self._inc_step()

    @property
    def recorded(self):
        return self.recorded_dial_position

    @property
    def is_green(self):
        return self.current_position == self.correct_position

    @property
    def is_red(self):
        return not self.is_green

    def solve_using(self, solver, times=1000):
        solve_step_counts = []

        for _ in range(times):
            while self.is_red:
                solver(self)

            solve_step_counts.append(self.step_count)
            self.reset()

        return mean(solve_step_counts), solve_step_counts


def solver(lock: Lock):
    lock.spin(1)


average, step_counts = Lock().solve_using(solver)
print(f'STEP COUNTS: {step_counts}\n\nMEAN: {average}')
