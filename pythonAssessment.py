

# Creating the function
def count_specific_word(text,search_word):
# converting letters to lowercase
    text = text.lower()
    search_word = search_word.lower()
    # splitting the texts into individual words
    words = text.split()
    # count the occurences of a word
    count = words.count(search_word)
    # return the final count
    return count
## example of the function
article = "AI is powerful. AI is growing fast."

result = count_specific_word(article, "AI")

print(result)

# a function to identify the most common word
def identify_most_common_word(text):
    # if text(string) is empty return none
    if text == "":
        return None
    # splitting the text into words
    words=['Hello', 'world']
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
# .item gives both the key and value
    for word, count in word_count.items():
        if count > highest_count:
            highest_count = count
            most_common_word = word
    
    return most_common_word
# example
text = "Python is fun Python is powerful Python is easy"

result = identify_most_common_word(text)
print(result)
# creating a function to calculate the average words
def calculate_average_length(text):
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

#example
text = "Python is fun"

result = calculate_average_length(text)
print(result)

# counting the number of paragraphs
def count_paragraphs(text):
    # Edge case: empty string
    if text == "":
        return 1

    # Split text wherever there is a blank line
    paragraphs = text.split("\n\n")

    # Return the number of paragraphs
    return len(paragraphs)
# exmple of usage
text = """Python is easy to learn.

It is widely used in data science.

It is also popular for web development."""

print(count_paragraphs(text))

# counting the number of sentences
def count_sentences(text):
    # Edge case: empty string
    if text == "":
        return 1

    count = 0

    # Look at every character
    for char in text:
        # Check if it ends a sentence
        if char == "." or char == "!" or char == "?":
            count += 1

    return count
# example 
text = "Python is fun. It is easy to learn."

print(count_sentences(text))