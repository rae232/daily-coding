# Learning Objective:
# This tutorial will guide you through building a simple text-based adventure game in Python.
# You will learn how to use conditional logic (if, elif, else statements) to create branching narratives
# based on user input. This is a fundamental concept for creating interactive stories and games.

# --- Game Setup ---

def start_game():
    # This function initializes and starts the adventure.
    # It's good practice to have a main function or entry point for your game.
    print("Welcome, brave adventurer, to the Whispering Woods!")
    print("Your quest begins now...\n")
    forest_path() # Call the first location in our game.

# --- Game Locations/Scenes ---

def forest_path():
    # This function represents a specific location or scene in our game.
    # It presents the player with a situation and asks for input.

    print("You stand at a fork in the forest path.")
    print("To your left, a dimly lit trail disappears into dense trees.")
    print("To your right, a sunlit path leads towards a distant meadow.")

    # Prompt the user for input.
    # .lower() converts the input to lowercase, making comparisons easier (case-insensitive).
    choice = input("Which path will you choose? (left/right): ").lower()

    # --- Conditional Logic: Branching Narratives ---
    # Here's where we use 'if', 'elif', and 'else' to decide what happens next.

    if choice == "left":
        # If the player types "left", we execute this block.
        print("\nYou cautiously step onto the left path.")
        dark_forest() # Move to the next scene.
    elif choice == "right":
        # If the player types "right", we execute this block.
        print("\nSunlight warms your face as you head towards the meadow.")
        sunny_meadow() # Move to the next scene.
    else:
        # If the player types anything else, this block is executed.
        # This handles invalid input and guides the player.
        print("\nThat's not a valid path. The forest is confusing!")
        print("You hesitate, and the choice is made for you...\n")
        # For simplicity, we'll force them down one path if they give invalid input.
        # In a more complex game, you might loop back to ask again.
        dark_forest() # Defaulting to the dark forest.

def dark_forest():
    # A new scene with more choices.
    print("The trees press in, and strange sounds echo around you.")
    print("You see a gnarled, old tree with a small, glowing mushroom at its base.")
    print("Further ahead, you hear the faint sound of running water.")

    choice = input("Do you investigate the mushroom or follow the water? (mushroom/water): ").lower()

    if choice == "mushroom":
        print("\nYou reach out to touch the mushroom. It pulses with light!")
        print("Suddenly, you feel a strange energy surge through you. You feel invigorated!")
        print("Your adventure continues, with newfound energy.\n")
        # For this tutorial, we'll just end after this beneficial event.
        print("To be continued...\n")
    elif choice == "water":
        print("\nYou follow the sound of water and find a clear stream.")
        print("As you drink, you feel refreshed, but a rustle in the bushes nearby startles you.")
        print("A wild boar charges! You narrowly escape with a scratch.\n")
        print("Your adventure continues, with a minor setback.\n")
        print("To be continued...\n")
    else:
        print("\nIndecision paralyzes you. The forest seems to swallow you whole.")
        print("You lose your way completely.")
        print("Game Over.\n") # This path leads to a game over.

def sunny_meadow():
    # Another scene with different choices.
    print("The meadow is alive with colorful flowers and buzzing insects.")
    print("In the center, a small, abandoned hut stands with its door ajar.")
    print("On the edge of the meadow, you spot a farmer tending to a flock of sheep.")

    choice = input("Will you explore the hut or speak to the farmer? (hut/farmer): ").lower()

    if choice == "hut":
        print("\nYou cautiously enter the hut. It's dusty and smells of old wood.")
        print("You find a weathered map tucked under a loose floorboard.")
        print("This map might be useful for future quests!\n")
        print("Your adventure continues, with a valuable find.\n")
        print("To be continued...\n")
    elif choice == "farmer":
        print("\nYou approach the farmer, who looks up with a friendly smile.")
        print("He tells you tales of the woods and warns of a grumpy troll in the nearby caves.")
        print("Armed with this knowledge, you feel more prepared.\n")
        print("Your adventure continues, with valuable information.\n")
        print("To be continued...\n")
    else:
        print("\nYou wander aimlessly, the beauty of the meadow overwhelming you.")
        print("You stumble and twist your ankle, unable to go further.")
        print("Game Over.\n") # This path leads to a game over.

# --- Game Execution ---

# This is the standard way to run Python code when the script is executed directly.
# It ensures that start_game() is called only when you run this file.
if __name__ == "__main__":
    start_game()

# --- Example Usage ---
# To play this game, save the code as a .py file (e.g., adventure.py)
# and then run it from your terminal:
#
# python adventure.py
#
# You will be prompted to make choices by typing 'left' or 'right', 'mushroom' or 'water', etc.
# Your choices will determine the story's path.
# This demonstrates how conditional logic (`if`, `elif`, `else`) creates branching narratives.