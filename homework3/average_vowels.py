# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(string):
    vowels = 0
    consonants = 0
    for i in range(0,len(string)):
        if string[i] in ["a","e","i","o","u","A","E","I","O","U"]:
            vowels += 1
        elif string[i] in ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]:
            consonants += 1
    return (vowels,consonants)

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(para):
    para = para.replace("!",".")
    para = para.replace("?",".")
    sentences = para.split(". ")
    VT = 0
    CT = 0
    for i in range(0,len(sentences)):
        V,C = counting_vowels_and_consonants(sentences[i])
        VT += V
        CT += C
    return len(sentences), VT/len(sentences), CT/len(sentences)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

S,V,C = average_vowels_and_consonants(paragraph)

print(S,V,C)