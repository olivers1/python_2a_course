class FightActions:
    def fight(self, defender):
        defender.power_level -= self.hit_points


class CharacterAttributes:
    def set_stats(self, power_level, hit_points):
        self.power_level = power_level
        self.hit_points = hit_points


class Batman(CharacterAttributes, FightActions):
    def __init__(self):
        self.set_stats(60, 10)

    def ability(self):
        self.hit_points += 5


class SpiderMan(CharacterAttributes, FightActions):
    def __init__(self):
        self.set_stats(80, 22)

    def ability(self):
        self.power_level += 10

character_attributes = CharacterAttributes()
spider_man, batman = SpiderMan(), Batman()

batman.ability()
spider_man.ability()
batman.fight(spider_man)
print("batman health:", batman.hit_points)
print("spider_man health:", spider_man.power_level)
