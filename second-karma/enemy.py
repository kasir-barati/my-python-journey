class Enemy:
    hp: int = 100
    # AttributeError: 'Enemy' object has no attribute 'attack_low'
    # This error occurs when we do not initialize these properties and also does not have __init__
    attack_low: int = 180
    attack_high: int = 360

    def __init__(
            self, 
            attack_low: int,
            attack_high: int) -> None: 
        self.attack_low = attack_low
        self.attack_high = attack_high

    def getAttackPower(
            self) -> {"attack_low": int, "attack_high": int}:
        return {
            "attack_low": self.attack_low,
            "attack_high": self.attack_high
        }

    def get_hp(self) -> int:
        return self.hp


enemy = Enemy(15, 98)
print(enemy.getAttackPower())
print(enemy.get_hp())

"""
Wrong usage:
NameError: name 'Enemy' is not defined
- def getAttackPower(self: Enemy):
"""