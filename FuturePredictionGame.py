def main():
    # Introduction
    print("Welcome to 'A Day in the Life of Tech'!")
    print("You will make choices about how much technology to use throughout the day.")
    print("Let's see how tech-heavy your day will be!\n")

    # Initialize tech score
    tech_score = 0

    # Question 1
    print("You wake up in the morning. How do you start your day?")
    print("1. Meditate in silence")
    print("2. Check your phone for sleep data")
    print("3. Watch YouTube videos")
    print("4. Browse social media")
    choice1 = int(input("Choose an option (1-4): "))
    if choice1 == 2:
        tech_score += 1
    elif choice1 == 3:
        tech_score += 2
    elif choice1 == 4:
        tech_score += 3
    print()

    # Question 2
    print("You're having breakfast. How do you prepare it?")
    print("1. No Breakfast")
    print("2. Cook a meal from scratch")
    print("3. Use a blender for a smoothie")
    print("4. Microwave some frozen food")
    print("5. Order food via an app")
    choice2 = int(input("Choose an option (1-5): "))
    if choice2 == 2:
        tech_score += 1
    elif choice2 == 3:
        tech_score += 2
    elif choice2 == 4:
        tech_score += 3
    elif choice2 == 5:
        tech_score += 4
    print()

    # Question 3
    print("You're going to school. How do you travel?")
    print("1. You walk")
    print("2. You go by bike")
    print("3. You go by car")
    print("4. You go by public transport")
    choice3 = int(input("Choose an option (1-4): "))
    if choice3 == 2:
        tech_score += 1
    elif choice3 == 3:
        tech_score += 2
    elif choice3 == 4:
        tech_score += 3
    print()

    # Question 4
    print("You are now in school. How do you keep notes?")
    print("1. You remember it")
    print("2. You write it down")
    print("3. You record it")
    print("4. You take notes on your laptop")
    choice4 = int(input("Choose an option (1-4): "))
    if choice4 == 2:
        tech_score += 1
    elif choice4 == 3:
        tech_score += 2
    elif choice4 == 4:
        tech_score += 3
    print()

    # Question 5
    print("It is lunch time now. What is for lunch?")
    print("1. No lunch for you")
    print("2. The lunch you made this morning")
    print("3. Buy lunch from a store")
    print("4. Order food via an app")
    choice5 = int(input("Choose an option (1-4): "))
    if choice5 == 2:
        tech_score += 1
    elif choice5 == 3:
        tech_score += 2
    elif choice5 == 4:
        tech_score += 3
    print()

    # Question 6
    print("Your school is finished for today. What will you go do?")
    print("1. Go home")
    print("2. Go for a nice bike ride")
    print("3. Go to the arcade")
    choice6 = int(input("Choose an option (1-3): "))
    if choice6 == 2:
        tech_score += 1
    elif choice6 == 3:
        tech_score += 2
    print()

    # Sub-question for Question 6 (if bike ride chosen)
    if choice6 == 2:
        print("What kind of bike will you use?")
        print("1. A normal bike")
        print("2. An electric bike")
        bike_choice = int(input("Choose an option (1-2): "))
        if bike_choice == 1:
            tech_score += 1
        elif bike_choice == 2:
            tech_score += 2
    print()
    
    # Sub-question for Question 6 (if arcade chosen)
    if choice6 == 3:
        print("How many games are you going to play?")
        amount_of_games = int(input("Choose an amount between (1-20): "))
        
        tech_score += amount_of_games
    print()

    # Question 7
    print("You're going home. How do you travel?")
    print("1. You walk")
    print("2. You go by bike")
    print("3. You go by car")
    print("4. You go by public transport")
    choice7 = int(input("Choose an option (1-4): "))
    if choice7 == 2:
        tech_score += 1
    elif choice7 == 3:
        tech_score += 2
    elif choice7 == 4:
        tech_score += 3
    print()

    # Question 8
    print("You're finally home and it's time for dinner. What will you do?")
    print("1. Cook a meal from scratch")
    print("2. Microwave some frozen food")
    print("3. Order food via an app")
    choice8 = int(input("Choose an option (1-3): "))
    if choice8 == 2:
        tech_score += 1
    elif choice8 == 3:
        tech_score += 2
    print()

    # Question 9
    print("You're finished with dinner, what will you do now?")
    print("1. Go to sleep")
    print("2. Listen to some music")
    print("3. Do your homework")
    print("4. Play a videogame")
    choice9 = int(input("Choose an option (1-4): "))
    if choice9 == 2:
        tech_score += 1
    elif choice9 == 3:
        tech_score += 2
    elif choice9 == 4:
        tech_score += 3
    print()

    # Final Result
    print(f"Your tech score is {tech_score} out of 28.")
    if tech_score < 3:
        print("You're living an almost tech-free life! A digital monk.")
    elif tech_score < 5:
        print("You’re not quite off the grid, but you definitely know how to unplug!")
    elif tech_score < 7:
        print("You're a casual tech user; just enough to be interesting!")
    elif tech_score < 10:
        print("You're in the tech zone but not overboard yet.")
    elif tech_score < 14:
        print("You're definitely riding the tech wave. Enjoy it while you're still there!")
    elif tech_score < 18:
        print("You're officially a tech enthusiast! Maybe consider some screen detox?")
    elif tech_score < 21:
        print("Wow! You're basically on a first-name basis with your devices.")
    elif tech_score < 24:
        print("Tech overload! You're a true digital native!")
    elif tech_score < 28:
        print("Are you human, or just a walking smartphone? You're deep in the tech zone!")
    else:
        print("Congratulations! You are 100% tech! Are you sure you're not AI? You are aren't you....")

if __name__ == "__main__":
    main()
