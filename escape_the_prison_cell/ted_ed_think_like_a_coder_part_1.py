from collections import namedtuple
from random import randint
from statistics import mean
from typing import Callable, Any

from stringutil import auto_str_filtered, auto_str


def rand_dial_position():
    return randint(1, 100)


def sign(i):
    return -1 if i < 0 else 0 if not i else 1


class Lock:
    POSITION_COUNT = 100

    def __init__(self):
        self.reset()

    def reset(self):
        self.correct_pin = rand_dial_position()
        self.current_pin = rand_dial_position()
        self.recorded_pin = self.current_pin
        self.step_count = 0

    def _inc_step(self):
        self.step_count += 1

    def spin(self, rotation: int):
        if not rotation:
            return

        self.current_pin = (self.current_pin + rotation) % (self.POSITION_COUNT + 1)

        if not self.current_pin:
            self.current_pin = 100 if rotation < 0 else 1

        if rotation:
            self._inc_step()

    def spin_to(self, pin):
        offset = abs(self.current_pin - pin) * (-1 if pin < self.current_pin else 1)
        self.spin(offset)

    def record(self):
        self.recorded_pin = self.current_pin
        self._inc_step()

    @property
    def recorded(self):
        return self.recorded_pin

    def __bool__(self):
        return self.current_pin == self.correct_pin

    def __str__(self):
        return f'<LOCK pin={self.current_pin}>'


def solve_lock(solver, setup: Callable[[Lock], Any] = lambda lock: None):
    lock = Lock()
    setup(lock)

    for i in range(1, 101):
        solver(lock)

    return lock


Result = namedtuple('Result', 'mean counts')


def solve_with_mean(solver, times):
    step_counts = []
    lock = Lock()
    for _ in range(times):
        solver(lock)
        step_counts.append(lock.step_count)
        lock.reset()

    return Result(mean(step_counts), step_counts)


def solver(lock: Lock):
    def check_range(initial, size, step):
        if lock:
            return lock

        lock.spin_to(initial)
        for _ in range(size):
            if lock:
                break
            lock.spin(step)

        return lock

    return check_range(0, 100, 1)


print(solve_with_mean(solver, 100))
