from main import Hero

class MyHero(Hero):
    def __init__(self, name, health, power, skill_points):
        super().__init__(name, health, power)
        self.skill_points = skill_points

    def unique_skill(self):
        if self.skill_points > 0:
            print(f"{self.name} uses a unique skill! Skill points left: {self.skill_points - 1}")
            self.skill_points -= 1
        else:
            print(f"{self.name} has no skill points left to use the unique skill.")

    def action(self):
        super().action()
        self.unique_skill()