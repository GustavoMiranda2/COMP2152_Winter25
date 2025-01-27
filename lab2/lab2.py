import random

def adventure_game():
    # Define the weapons array
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
    
    
    try:
        hero_strength = int(input("Hero's combat strength: "))
        monster_strength = int(input("Monster's combat strength: "))
    except ValueError:
        print("Combat strength must be a number.")
        return

    
    try:
        dice_roll = int(input("Roll the dice (1-6) for your weapon: "))
        if dice_roll < 1 or dice_roll > 6:
            print("Dice roll must be between 1 and 6.")
            return
    except ValueError:
        print("Invalid input. Enter a number between 1 and 6.")
        return

    
    selected_weapon = weapons[dice_roll - 1]
    print(f"Rolled: {dice_roll}, Weapon: {selected_weapon}")
    
    
    hero_strength += dice_roll
    print(f"Updated combat strength: {hero_strength}")

    
    if dice_roll <= 2:
        print("Weak weapon.")
    elif dice_roll <= 4:
        print("Average weapon.")
    else:
        print("Strong weapon.")

    
    if selected_weapon != "Fist":
        print("Avoided Fist.")

    
    input("Roll for health points (Press Enter)")
    hero_health = random.randint(1, 6)
    print(f"Hero health points: {hero_health}")

    
    input("Roll for monster's health points (Press Enter)")
    monster_health = random.randint(1, 6)
    print(f"Monster health points: {monster_health}")

    
    input("Roll for healing potion (Press Enter)")
    found_potion = random.choice([True, False])
    print(f"Healing potion found: {'Yes' if found_potion else 'No'}")

    
    print("\nCombat begins.")
    input("Hero attacks first (Press Enter)")
    print(f"Hero ({hero_strength}) attacks Monster ({monster_health})")
    
    if hero_strength >= monster_health:
        print("Monster defeated.")
    else:
        remaining_monster_health = monster_health - hero_strength
        print(f"Monster health left: {remaining_monster_health}")
        print("Monster retaliates.")
        print(f"Monster ({monster_strength}) attacks Hero ({hero_health})")
        if monster_strength >= hero_health:
            print("Hero defeated.")
        else:
            remaining_hero_health = hero_health - monster_strength
            print(f"Hero health left: {remaining_hero_health}")

# Run the game
adventure_game()
