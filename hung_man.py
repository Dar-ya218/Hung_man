import random
import time

class Hangman:
    def __init__(self):
        # List of words to choose from
        self.words = [
            "python", "programming", "computer", "development",
            "technology", "videogame", "keyboard", "internet"
        ]
        self.word = ""
        self.guessed_letters = set()
        self.max_attempts = 6
        self.attempts = 0
        
    def get_hangman_art(self):
        # ASCII art for different stages of the game
        stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |
               |
               |
               -
            """,
            """
               --------
               |      |
               |
               |
               |
               |
               -
            """
        ]
        return stages[self.attempts]
        
    def start_game(self):
        # Initialize a new game
        self.word = random.choice(self.words)
        self.guessed_letters = set()
        self.attempts = 0
        
    def display_word(self):
        # Show the word with guessed letters revealed
        return ' '.join(letter if letter in self.guessed_letters else '_' 
                       for letter in self.word)
        
    def make_guess(self, letter):
        # Process the player's guess
        if letter in self.guessed_letters:
            return "You already guessed that letter! Having memory issues? 🤔"
            
        self.guessed_letters.add(letter)
        
        if letter not in self.word:
            self.attempts += 1
            return "Oops! Wrong letter... One step closer to doom! 💀"
            
        return "Well done! Correct letter! 🎉"

def main():
    game = Hangman()
    
    print("🎮 Welcome to the Hangman Game! 🎮")
    print("Where every mistake brings you closer to your fate... dramatic! 😱")
    
    while True:
        print("\n1. 🎲 Play new game")
        print("2. 🚪 Exit")
        
        choice = input("\nChoose an option (1-2): ").strip()
        
        if choice == '2':
            print("\nGoodbye! Remember: practice makes perfect! 👋")
            break
            
        elif choice == '1':
            game.start_game()
            
            while game.attempts < game.max_attempts:
                # Display game state
                print("\n" + game.get_hangman_art())
                print("\nWord:", game.display_word())
                print(f"Used letters: {', '.join(sorted(game.guessed_letters))}")
                print(f"Remaining attempts: {game.max_attempts - game.attempts}")
                
                guess = input("\nGuess a letter: ").lower()
                
                # Validate input
                if not guess.isalpha() or len(guess) != 1:
                    print("Please enter a single letter! 🤦")
                    continue
                    
                print("\n" + game.make_guess(guess))
                
                # Check win condition
                if all(letter in game.guessed_letters for letter in game.word):
                    print("\nYOU WIN! 🎉🎊🎈")
                    print(f"The word was: {game.word}")
                    break
                    
            # Check lose condition
            if game.attempts >= game.max_attempts:
                print("\n" + game.get_hangman_art())
                print("\nGAME OVER! 💀")
                print(f"The word was: {game.word}")
                
        else:
            print("Invalid option! Was it really that hard to choose between 1 and 2? 😅")

if __name__ == "__main__":
    main()