# Creating the function
def count_specific_word(text,search_word):
    # converting letters to lowercase
    text = text.lower()
    search_word = search_word.lower()

    # remove punctuation marks
    # char goes through each character
    # .isalpha checks if a letter is of alphabet
    clean_text = ""

    for char in text:
        if char.isalpha() or char == " ":
            clean_text += char

    # splitting the texts into individual words
    words = clean_text.split()

    # count the occurences of a word
    count = words.count(search_word)

    # return the final count
    return count