class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def action(self):
        print(f"{self.name} is taking action with power {self.power}.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage, health is now {self.health}.")

    def is_alive(self):
        return self.health > 0



