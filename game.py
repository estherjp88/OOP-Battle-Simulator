from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Southlands"

def battle(hero: Hero, enemy: Goblin):
    while hero.isAlive() and enemy.is_alive():
        heroDamage=hero.attack()
        enemy.take_damage(heroDamage)
        if enemy.is_alive():
            enemy_damage=enemy.attack()
            hero.takeDamage(enemy_damage)

    if hero.isAlive():
        print(f"{hero.name} wins")
    else:
        print(f"{enemy.name} wins")
def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Grian")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    goblina = Goblin("Jimmy")
    
    print(f"{goblina.name} enters the arena with {goblina.health} health.")
    print("But no hero has answered the call... yet.")

    hero = Hero("Pearl")

    print(f"{hero.name} enters the arena with {hero.health} health.")

    battle(hero, goblin)

    



if __name__ == "__main__":
    main()
