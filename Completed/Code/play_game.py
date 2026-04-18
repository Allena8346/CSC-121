"""
Game Launcher for Text-Based RPG
Created by: Alexander Allen
Date: December 2024

This file starts the game and imports all necessary classes from the main game file.
"""

# Import the Game class from your main file
# Make sure myFinalProject(Complete).py is in the same directory
from myFinalProjectV3 import Game


def main():
    """
    Main function to start the game.
    Creates a Game instance and displays the main menu.
    """
    # Create game instance
    game = Game()
    
    # Show main menu (handles new game, load game, and exit)
    game.main_menu()


if __name__ == "__main__":
    # This ensures the game only runs when this file is executed directly
    main()