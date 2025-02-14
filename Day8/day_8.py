#Day 8. Caesar Cipher
import string
import art

alphabet = list(string.ascii_lowercase)
print(art.logo)
looping = True

def ceasar(original_text, shift_amount, direct):
    output_text = ""
    if direct == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
         output_text += letter
         continue
        shifted_position = (alphabet.index(letter) + shift_amount)
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here's you encoded result: {output_text}")
while looping:
    while True:
        direction = input("Type encode to encrypt, type decode to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            break
        else:
            print("You type a wrong command try again.")
    text = input("Type your message:\n").lower()
    while True:
        shift = input("Type how much it shift:\n")
        if shift.isdigit():
            shift = int(shift)
            break
        else:
            print("Please enter a number.")
    ceasar(original_text=text, shift_amount=shift, direct=direction)
    restart = input("Type 'yes' if you keep using, type 'no' to finish:\n")
    if restart.lower() == "no":
        looping = False

