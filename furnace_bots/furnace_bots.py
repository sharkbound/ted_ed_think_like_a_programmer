from dataclasses import dataclass
from random import random, choice


@dataclass(frozen=True)
class Bot:
    __slots__ = 'parent', 'id'

    parent: int
    id: int

    @property
    def is_master(self):
        return not self.id


def generate():
    free_ids = sorted(range(1, 100000), key=lambda _: random())
    id_to_bots = {0: Bot(-1, 0)}
    used_ids = [0]
    bots = [id_to_bots[0]]

    while free_ids:
        bot_id = free_ids.pop()
        bot = Bot(choice(used_ids), bot_id)
        used_ids.append(bot_id)
        id_to_bots[bot.id] = bot
        bots.append(bot)

    def parent(bot: Bot) -> Bot:
        return id_to_bots[bot.parent]

    return bots, parent


bots, parent = generate()
bot = choice(bots)
while not bot.is_master:
    bot = parent(bot)
    print(bot)
