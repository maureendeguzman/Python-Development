



import random

def hangman_game():
    words = ["avenue", "awkward", "bandwagon", "numbskull"]
    word = random.choice(words)
    guessed = set()
    turns = 7

    while turns > 0:
        for letter in word:
            if letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input("Enter a letter: ")
        guessed.add(guess)

        if guess not in word:
            turns -= 1
            print(f"Wrong! {turns} turns left")
            if turns == 0:
                print("Game over!")
                print(f"The word was {word}")
                return

        if all(letter in guessed for letter in word):
            print("Congratulations, you won!")
            return

hangman_game()
    