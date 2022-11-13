class FightActions:
    def fight(self, defender):
        defender.power_level -= spiderman.hit_points
        print("taking a hit")


class CharacterAttributes:
    def set_stats(self, power_level, hit_points):
        self.power_level = power_level
        self.hit_points = hit_points


class Batman(FightActions, CharacterAttributes):
    def __init__(self):
        self.set_stats(60, 12)

    def call_alfred(self):
        self.power_level += 10
        print("protection gadget delivered")


class SpiderMan(FightActions, CharacterAttributes):
    def __init__(self):
        self.set_stats(80, 9)

    def go_web_go(self):
        self.hit_points += 9
        print("spidey hit points increased")


batman = Batman()
spiderman = SpiderMan()

batman.call_alfred()
spiderman.go_web_go()

print("batman power lever:", batman.power_level)
print("spiderman hitpoints:", spiderman.hit_points)

spiderman.fight(batman)
print("batman power lever:", batman.power_level)



# duck typing
"""
class Duck:
    def walk_and_talk(self):
        print("duck walk and quack")


class Bird:
    def walk_and_talk(self):
        print("bird fly and twitter")


class Frog:
    def jump_and_talk(self):
        print("frog jump and quack")


def animal_action(animal):
    animal.walk_and_talk()


duck = Duck()
bird = Bird()
frog = Frog()

animal_action(duck)
animal_action(bird)

try:
    animal_acrion(frog)
except AttributeError as error:
    print(error)
"""
