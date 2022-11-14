from abc import ABC, abstractmethod

class CharacterAttributes(ABC):
    def set_stats(self, power_level, hit_points):
        self.power_level = power_level
        self.hit_points = hit_points

    @property
    @abstractmethod
    def use_power(self):
        pass


class Batman(CharacterAttributes):
    def __init__(self):
        self.set_stats(60, 12)

    @property
    def use_power(self):
        self.power_level += 10
        print("protection gadget delivered")


class SpiderMan(CharacterAttributes):
    def __init__(self):
        self.set_stats(80, 9)

    @property
    def use_power(self):
        self.hit_points += 9
        print("spidey hit points increased")


class Arena:
    def __init__(self):
        self._fighters = []

    def enter(self, fighter):
        self._fighters.append(fighter)

    def fight(self):
        for item in self._fighters:
            item.use_power



batman = Batman()
spiderman = SpiderMan()
arena = Arena()
tuple_list = (batman, spiderman)

for item in tuple_list:
    arena.enter(item)

arena.fight()

print(arena._fighters)
print(f"batman (power/hit): {batman.power_level}/{batman.hit_points}")
print(f"spiderman (power/hit): {spiderman.power_level}/{spiderman.hit_points}")