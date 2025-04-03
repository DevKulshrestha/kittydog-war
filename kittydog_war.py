# Kittyland vs Doggieland: The Territorial War
kitty_land = 50
doggy_land = 50
kitty_science = 0
doggy_science = 0

print("Welcome to Kittyland vs Doggieland: The Territorial War!")
while kitty_land > 0 and doggy_land > 0:
    # Kittyland’s Turn
    print(f"\nKittyland: {kitty_land}%  Doggieland: {doggy_land}%")
    print("Kittyland’s Turn:")
    print("1. Attack with Claw Brigade (+5% land if successful)")
    print("2. Build Purr Defenses (block enemy attack)")
    print("3. Spy on Doggieland (gain info)")
    print("4. Science Tab")
    print("5. Intelligence Agency Tab")
    kitty_choice = input("Enter 1-5: ")

    if kitty_choice == "1":
        print("\nDoggieland’s Reaction:")
        print("1. Counter with Woof Infantry")
        print("2. Retreat")
        print("3. Deploy Slobber Mines")
        doggy_reaction = input("Enter 1-3: ")
        if doggy_reaction == "1":
            print("Woof Infantry holds ground. No change.")
        elif doggy_reaction == "2":
            kitty_land += 5
            doggy_land -= 5
            print("Doggieland retreats! Kittyland gains land.")
        elif doggy_reaction == "3":
            kitty_land -= 10
            doggy_land += 10
            print("Slobber Mines trap the cats! Kittyland loses land.")
    
    elif kitty_choice == "4":
        print(f"\nScience Tab (Points: {kitty_science}):")
        print("1. Research Laser Pointer Drones (10 points)")
        science_choice = input("Enter 1 or 0 to skip: ")
        if science_choice == "1" and kitty_science >= 10:
            kitty_science -= 10
            print("Laser Pointer Drones researched!")
        else:
            print("Not enough points or invalid choice.")
    
    elif kitty_choice == "5":
        print(f"\nIntelligence Agency Tab (Points: {kitty_science}):")
        print("1. Steal 5 science points (5 points)")
        intel_choice = input("Enter 1 or 0 to skip: ")
        if intel_choice == "1" and kitty_science >= 5:
            kitty_science -= 5
            doggy_science -= 5
            kitty_science += 5
            print("Stole 5 science points!")
        else:
            print("Not enough points or invalid choice.")

    # Science Points
    kitty_science += int(input("\nScore Kittyland’s logic (1-5): "))
    doggy_science += int(input("Score Doggieland’s logic (1-5): "))

if kitty_land <= 0:
    print("\nDoggieland wins!")
else:
    print("\nKittyland wins!")
