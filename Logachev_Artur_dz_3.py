word = 'процент'
end_of_word_1 = 'ов'
end_of_word_2 = 'а'
for i in range (1, 101  ):
    remnant = i % 10

    if remnant == 1 and not (11 <= i <= 14):
        print(i, word)


    elif 5 <= remnant <= 9  or remnant == 0 or (11 <= i <= 14):
        print(i, word + end_of_word_1)

    elif 2 <= remnant <= 4 and not (11 <= i <= 14):
        print(i, word + end_of_word_2)
