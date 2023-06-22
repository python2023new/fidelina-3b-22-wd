#Создать класс "Игровой персонаж", который будет иметь следующие свойства: имя,
# уровень, здоровье, атака и защита.
# Также необходимо добавить методы для изменения свойств персонажа:
# - метод для применения урона, который будет уменьшать здоровье персонажа на указанное
# значение
# - метод для повышения уровня персонажа, который будет увеличивать уровень и
# увеличивать здоровье и атаку на 10%

class Character:

    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, amount):
        self.health -= amount

    def level_up(self):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1

    def attack_character(self, other):
        damage = self.attack - other.defense
        damage = max(damage, 0)
        other.take_damage(damage)
        print(f"{self.name} attacks {other.name} for {damage} damage.")

def run_battle_round(character1, character2):
    # Character 1 attacks first
    character1.attack_character(character2)
    if character2.health > 0:
        # Character 2 attacks back
        character2.attack_character(character1)
    print(f"{character1.name}: {character1.health} HP")
    print(f"{character2.name}: {character2.health} HP\n")

# Create two characters
character1 = Character("Warrior", 1, 100, 20, 10)
character2 = Character("Wizard", 1, 80, 30, 5)

# Print initial stats
print \
    (f"{character1.name}: Level {character1.level} - {character1.health} HP - {character1.attack} Attack - {character1.defense} Defense")
print \
    (f"{character2.name}: Level {character2.level} - {character2.health} HP - {character2.attack} Attack - {character2.defense} Defense\n")

# Run 3 rounds of battle
for i in range(3):
    print(f"Round { i +1}:\n")
    run_battle_round(character1, character2)

# Print final stats
if character1.health > 0:
    print(f"{character1.name} wins!")
else:
    print(f"{character2.name} wins!")