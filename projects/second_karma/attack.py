import random


player_hp: int = 260
enemy_attack_low: int = 60
enemy_attack_high: int = 90


while player_hp > 0:
    damage: int = random.randrange(
        enemy_attack_low,
        enemy_attack_high
    )
    player_hp -= damage

    print({
        "damage": damage,
        "player_hp": player_hp
    })

    if player_hp <= enemy_attack_low:
        player_hp = 0
        break
    else: 
        continue

