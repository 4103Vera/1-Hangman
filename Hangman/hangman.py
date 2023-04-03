tries = 0
found_letters = []
# Get a random word from the word list
def get_word():
    global word
    import random
    with open("wordlist.txt") as word_file:
        words = word_file.readline().split() #This splits by whitespace, if you used some other delimiter specify the delimiter here as an argument.
    word = random.choice(words)
    print("Play the H A N G M A N game")

    

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

def get_letter(guessed_letters):
    global guess
    while True:
        guess = input("Enter a letter: ").strip().lower()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. " +
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess
# Draw the display


# Get next letter from user

        


# The input/process/draw technique is common in game programming
def play_game():
    global guess
    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""
    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 10 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"              
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remaining_letters == 0:
        print("Congratulations! You got it in", 
               num_guesses, "guesses.")   
    else:    
        print("Sorry, you lost.")
        print("The word was:", word)


def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))
    if num_wrong == 1:
        print ("------------\n"
              "|    |      \n"
              "|           \n"
              "|           \n"
              "|           \n"
              "|           ")
    elif num_wrong == 2:
        print ("------------\n"
              "|    |      \n"
              "|    O      \n"
              "|           \n"
              "|           \n"
              "|           ")
    elif num_wrong == 3:
        print ("------------\n"
              "|    |      \n"
              "|    O      \n"
              "|    I      \n"
              "|           \n"
              "|           ")
    elif num_wrong == 4:
         print ("------------\n"
               "|    |      \n"
               "|    O      \n"
               "|   \I      \n"
               "|           \n"
               "|           ")   
    elif num_wrong == 5:
         print ("------------\n"
               "|    |      \n"
               "|    O      \n"
               "|   \I/     \n"
               "|           \n"
               "|           ")        
    elif num_wrong == 6:
         print ("------------\n"
               "|    |      \n"
               "|    O      \n"
               "|   \I/     \n"
               "|   /       \n"
               "|           ")  
               
    elif num_wrong == 7:
         print ("------------\n"
               "|    |      \n"
               "|    O      \n"
               "|   \I/     \n"
               "|   / \     \n"
               "|           ")  
         print("The answer was", word)
         while True:
             print()
             again = input("Do you want to play again (y/n)?: ").lower()
             if again != "y":
                 break
    



get_word()
play_game()





