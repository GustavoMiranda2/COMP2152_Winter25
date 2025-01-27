import random


weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

def main():
    try:

        weaponRoll = random.randint(1, 6)
        print(f"You rolled a dice and got: {weaponRoll}")


        hero_weapon = weapons[weaponRoll - 1]
        print(f"The hero's weapon is: {hero_weapon}")


        combat_strength = weaponRoll * 10
        print(f"The hero's combat strength is now: {combat_strength}")


        if weaponRoll <= 2:
            print("Oh no! You rolled a weak weapon, friend. Better luck next time.")
        elif weaponRoll <= 4:
            print("Hmm... Your weapon is decent but not amazing.")
        else:
            print("Fantastic roll! Nice weapon, friend!")


        if hero_weapon != "Fist":
            print("Thank goodness you didn't roll the Fist... That's the weakest weapon!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
