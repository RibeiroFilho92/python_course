secret_word = "mandalorian"
blanket_secret_word = list(secret_word)
tries =  0

for ind, val in enumerate(blanket_secret_word):
    
    blanket_secret_word[ind] = "_"

while blanket_secret_word != secret_word:

    print()
    print(f"Actual word: {blanket_secret_word}")
    print(f"Tries: {tries}")

    letter_turn = input("Inform a letter: ").lower()

    if len(letter_turn) > 1:
        
        print("You should put a single letter.")
        continue


    for ind, letter in enumerate(secret_word):
        
        if letter == letter_turn:

            blanket_secret_word[ind] = letter

    tries += 1

