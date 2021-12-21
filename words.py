# Part 1 & 2
words = ['light', 'neat']
for word in words:
    print(word.upper())

def print_upper_words(words_list):
    """
    Given a list of words print each word.
    The words printed must be converted to UPPERCASE letters!
    Ex:    print_upper_words(["hi", "wow"])
            HI
            WOW
    """

    for word in words_list:
        print(word.upper())

# Part 3

def print_upper_e_words(words_list):
    """
    Given a list of words print each word that starts with 'e'.
    The words printed must be converted to UPPERCASE letters!
    Ex:    print_upper_e_words(["elephant", "wow"])
            ELEPHANT
    """
    for word in words_list:
        if word.startswith('e'):
            print(word.upper())

# Part 4

def print_upper_by_letters(words_list, must_start_with):
    """
    Given a list of words and a set of letters, print only words that starts with the given letters.
    The words printed must be converted to UPPERCASE letters!
    Ex:    print_upper_by_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with = {"h", "y"})
            HELLO
            HEY
            YO
            YES
    """

    #nested loops to run through each word and test it against each letter
    for word in words_list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
