import re
from dataclasses import dataclass
from enum import Flag, auto
from typing import Tuple


class Flags(Flag):
    none = 0
    GLASSES = auto()
    GREEN_EYES = auto()
    RED_HAIR = auto()
    NO_GLASSES = auto()


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
    if not person & Flags.GREEN_EYES:
        return False

    bools = [True]

    if person & Flags.GLASSES:
        bools.append(len(re_vowel.findall(person.name)) == 2)
    if person & Flags.RED_HAIR:
        bools.append(bool(re_consecutive.search(person.name)))
    if person & Flags.NO_GLASSES:
        bools.append(len(re_consecutive.findall(person.name)) == 3)

    return all(bools)


people = [
    Person('timmy', Flags.NO_GLASSES),
    Person('james', Flags.NO_GLASSES),
    Person('none', Flags.GLASSES | Flags.RED_HAIR),
    Person('just greaen', Flags.GREEN_EYES | Flags.RED_HAIR),
    Person('vaal', Flags.GLASSES | Flags.GREEN_EYES | Flags.RED_HAIR),
]

for person in people:
    if is_leader(person):
        print(f'found leader "{person.name}" with flags "{person.flags}"')
