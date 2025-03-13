import random

# 🎲 Welcome message
print("\n🎲 Welcome to the Number Guessing Game! 🎯\n")
print("**** Difficulty Levels ****")
print("1. Very Easy (1-10)\n2. Easy (1-30)\n3. Normal (1-50)\n4. Hard (1-100)\n5. Very Hard (1-500)")
print("*" * 40)

# Get difficulty level from the user
try:
    game_level = int(input("Please choose a game level (1-5): "))
except ValueError:
    game_level = 3  # Default to Normal if input is invalid

# Set range and allowed attempts based on difficulty level
difficulty_settings = {
    1: (10, 10),
    2: (30, 8),
    3: (50, 8),
    4: (100, 7),
    5: (500, 5)
}

# Assign values based on user choice or default to Normal
a, allowed_attempts = difficulty_settings.get(game_level, (50, 8))

# Generate a random number within the selected range
random_number = random.randint(1, a)
remaining_attempts = allowed_attempts  # Tracks remaining chances
used_attempts = 0  # Tracks the number of attempts used
bonus_used = False  # Tracks if the bonus chance has been used

print(f"\n🔢 A number between 1 and {a} has been chosen. Try to guess it!\n")

# Game loop
while remaining_attempts > 0:
    try:
        user_guess = int(input("Enter your guess: "))
        used_attempts += 1
        remaining_attempts -= 1  # Reduce remaining attempts after each guess

        # If the guess is correct, the game ends
        if user_guess == random_number:
            print(f"\n🎉 Congratulations! You found the number {random_number} in {used_attempts} attempts! 🎯")
            break  # Exit the loop

        # Easter Egg: If the player enters 23, they get an extra attempt (only once)
        elif user_guess == 23 and not bonus_used:
            remaining_attempts += 2
            bonus_used = True  # Mark the bonus as used
            print(f"\n🎁 Wow! You found my favorite number, so you get one extra chance!")
            print(f"Now you have {remaining_attempts} attempts left.")

        # Provide hints for incorrect guesses
        else:
            hint = "⬆️ Try a higher number!" if user_guess < random_number else "⬇️ Try a lower number!"
            print(f"❌ Incorrect guess. {hint}")
            print(f"You have {remaining_attempts} attempts left.\n")

    except ValueError:
        print(f"⛔ Invalid input! Please enter a number between 1 and {a}.\n")

# If no attempts are left and the user hasn't guessed correctly
if remaining_attempts == 0:
    print(f"\n💀 Game Over! The correct number was {random_number}. Better luck next time! 🎲\n")
