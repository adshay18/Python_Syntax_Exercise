#Part 1 & 2

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

#Part 3

def print_upper_e_words(words_list):
    """
    Given a list of words print each word that starts with 'e'.
    The words printed must be converted to UPPERCASE letters!
    Ex:    print_upper_words(["elephant", "wow"])
            ELEPHANT
    """
    for word in words_list:
        if word.startswith('e'):
            print(word.upper())