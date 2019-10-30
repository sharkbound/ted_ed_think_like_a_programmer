import re
from dataclasses import dataclass
from enum import Flag, auto
from typing import Tuple


class Flags(Flag):
    none = 0
    glasses = auto()
    green_eyes = auto()
    red_hair = auto()
    no_glasses = auto()


all_flags: Tuple[Flags] = tuple(Flags)
vowels = 'aeiouy'
re_consecutive = re.compile(r'(?P<char>\w)(?P=char)', flags=re.I)
re_vowel = re.compile(r'[aeiouy]', flags=re.I)


@dataclass
class Person:
    name: str
    flags: Flags

    def __and__(self, flags):
        return self.flags & flags == flags


def is_leader(person: Person):
    if not person & Flags.green_eyes:
        return False

    bools = [True]

    if person & Flags.glasses:
        bools.append(len(re_vowel.findall(person.name)) == 2)
    if person & Flags.red_hair:
        bools.append(bool(re_consecutive.search(person.name)))
    if person & Flags.no_glasses:
        bools.append(len(re_consecutive.findall(person.name)) == 3)

    return all(bools)


people = [
    Person('timmy', Flags.no_glasses),
    Person('james', Flags.no_glasses),
    Person('none', Flags.glasses | Flags.red_hair),
    Person('just greaen', Flags.green_eyes | Flags.red_hair),
    Person('vaal', Flags.glasses | Flags.green_eyes | Flags.red_hair),
]

for person in people:
    if is_leader(person):
        print(f'found leader "{person.name}" with flags "{person.flags}"')
