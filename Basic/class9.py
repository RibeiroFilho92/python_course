secret_word = "mandalorian"
blanket_secret_word_list = list(secret_word)
tries =  0

for ind, val in enumerate(secret_word):
    
    blanket_secret_word_list[ind] = "_"

blanket_secret_word = "".join(blanket_secret_word_list)

while blanket_secret_word != secret_word:

    print()
    print(f"Actual word: {blanket_secret_word_list}")
    print(f"Tries: {tries}")

    letter_turn = input("Inform a letter: ").lower()

    if len(letter_turn) > 1:
        
        print("You should put a single letter.")
        continue


    for ind, letter in enumerate(secret_word):
        
        if letter == letter_turn:

            blanket_secret_word_list[ind] = letter

    tries += 1
    blanket_secret_word = "".join(blanket_secret_word_list)

