#Day 7. A basic Hangman game.
import hangman
import random

print(hangman.title)
chosen_word = random.choice(hangman.words)
print(chosen_word)
placeholder = ""
control = True
for letter in chosen_word:
    placeholder += "_"
print(f"Here's your word: {placeholder}")
placeholder_list = list(placeholder)
i = 0
lives = 6
while control:
    print(f"************<{lives}/6> LIVES LEFT************")
    guess = input("Guess a letter: ").lower()
    if guess in placeholder.lower():
        print("You have already guessed that letter. Try again.")
        continue
    for letter in chosen_word:
        if letter == guess:
            placeholder_list[i] = guess.upper()
        i += 1
    if guess in chosen_word:
        print(hangman.the_man[lives])
        print(f"You guessed right.")
    else:
        lives -= 1
        print(hangman.the_man[lives])
        print(f"You guessed {guess} but that's not in the word. You lose a life.")
    i = 0
    placeholder = ''.join(placeholder_list)
    print(placeholder)
    if '_' not in placeholder:
        print(hangman.Win)
        control = False
    elif lives == 0:
        print(f"It was {chosen_word}")
        print(hangman.Lose)
        control = False