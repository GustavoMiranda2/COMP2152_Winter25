"""
Autor: Gustavo Miranda 101488574
Assignment: #1

"""

# part B: 
gym_member = "Alex Alliton"       # string
preferred_weight_kg = 20.5        # float
highest_reps = 25                 # integer
membership_active = True          # boolean

# part C:
workout_stats = {
    "Caio": (30, 45, 20),
    "yuri": (40, 30, 35),
    "Rafaela": (25, 55, 15),
    "Isa": (60, 40, 30)
    
}

# part D: 
original_friends = list(workout_stats.keys())
for friend in original_friends:
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes

# part E:
workout_list = [list(workout_stats[friend]) for friend in original_friends]

# part F:

print("Check out the mix of stretching and sprinting durations:")
for row in workout_list:
    print(row[0:2])


print("\nHere are the powerlifting minutes for our final duo:")
for row in workout_list[-2:]:
    print(row[2])

# part G:
print("\nShout out to anyone who rocked 120 minutes or more:")
for friend in original_friends:
    if workout_stats[friend + "_Total"] >= 120:
        print(f"Awesome energy, {friend}! You logged {workout_stats[friend + '_Total']} minutes!")

# part H:
friend_input = input("\nEnter a friend's name to see their workout journey: ")
if friend_input in original_friends:
    print(f"\nHere's the breakdown for {friend_input}: {workout_stats[friend_input]}")
    print(f"All in all, that's {workout_stats[friend_input + '_Total']} minutes!")
else:
    print(f"\nLooks like {friend_input} isn't in our records.")

# I: Identify and print the friend with the highest and lowest total workout minutes
totals = {friend: workout_stats[friend + "_Total"] for friend in original_friends}
max_friend = max(totals, key=totals.get)
min_friend = min(totals, key=totals.get)

print("\nThe most active superstar is:")
print(f"{max_friend} with {totals[max_friend]} minutes!")

print("\nAnd the friend with the quietest routine is:")
print(f"{min_friend} with only {totals[min_friend]} minutes.")

