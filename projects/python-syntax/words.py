def print_upper_words(words, must_start_with):
    """For each word that matches, print out each word in uppercase on a new line."""
    

    
    for word in words:
        for letter in must_start_with:
            if letter.upper() == word[0].upper():
                print(word.upper())

