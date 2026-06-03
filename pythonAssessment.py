def count_specific_word(text, search_word):
    # converting letters to lowercase
    text = text.lower()
    search_word = search_word.lower()

    # remove punctuation
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


# a function to identify the most common word
def identify_most_common_word(text):
    # if text(string) is empty return none
    if text == "":
        return None

    # splitting the text into words
    words = text.lower().split()

    # A dictionary to store counts
    word_count = {}

    # counting each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # finding the word with the highest count and looping through the dictionary
    most_common_word = None
    highest_count = 0

    # .items gives both the key and value
    for word, count in word_count.items():
        if count > highest_count:
            highest_count = count
            most_common_word = word

    return most_common_word


# creating a function to calculate the average words
def calculate_average_word_length(text):
    # handling empty string
    if text == "":
        return 0

    # remove punctuation marks
    # char goes through each character
    # .isalpha checks if a letter is of alphabet
    clean_text = ""

    for char in text:
        if char.isalpha() or char == " ":
            clean_text += char

    # splitting into words
    words = clean_text.split()

    if not words:
        return 0

    # counting total words
    total_length = 0

    # looping through each word
    for word in words:
        total_length += len(word)

    # calculating average
    number_of_words = len(words)

    # average words
    average = total_length / number_of_words

    return average


# counting the number of paragraphs
def count_paragraphs(text):
    # Edge case: empty string
    if text == "":
        return 1

    # Split text wherever there is a blank line
    paragraphs = text.split("\n\n")

    # Return the number of paragraphs
    return len(paragraphs)


# counting the number of sentences
def count_sentences(text):
    # Edge case: empty string
    if text == "":
        return 1

    count = 0
    i = 0

    # Look at every character using a while loop
    while i < len(text):
        # Check if it ends a sentence
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            count += 1

        i += 1

    return count