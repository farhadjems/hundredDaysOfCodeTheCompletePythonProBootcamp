import random, hangmanArt, dic

print(hangmanArt.logo)

#choosing word
word_list = dic.words
# print(word_list)

chosen_word = random.choice(word_list)
print(f"Psssst, the word is: {chosen_word}")

list_answer = []
for char in chosen_word:
    list_answer.append('-')

hangman_life = len(hangmanArt.HANGMANPICS)


answer = ""
while hangman_life > 0 and  answer != chosen_word:
    is_guess_correct = False
    user_guess = input("Enter a letter: ").lower()

    for i in range (0, len(chosen_word)):
        if chosen_word[i] == user_guess:
            # print(char)
            list_answer[i] = user_guess
            is_guess_correct = True

    answer = ""
    for char in list_answer:
        answer += char
    
    print(answer)

    if not is_guess_correct:
        hangman_life -= 1
    print(hangmanArt.HANGMANPICS[-hangman_life])

if hangman_life == 0 or answer != chosen_word:
    print("You Lost!")
else:
    print(f"You Won the game! the word is: {answer}")
