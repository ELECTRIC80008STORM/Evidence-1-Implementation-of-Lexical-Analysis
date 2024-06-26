"""
Implementation of Lexical Analysis (Automaton and Regular Expression)

This script checks if a word is part of the defined Elven language subset and performs
manual tests by asking the user to input words and checking if they are part of the language.
"""

import re

def isPartOfLanguage(word):
    """
    Check if a word is part of the defined language.

    Parameters:
    word (str): The word to be checked.

    Returns:
    bool: True if the word is part of the language, False otherwise.
    """

    isPartOfLanguage = re.search("^C(erthas|irth|oirë|oranar|ormallen)$", word, re.IGNORECASE)
    if(isPartOfLanguage):
        return True
    else:
        return False

def manualTests():
    """
    Perform manual tests by asking the user to input words
    and checking if they are part of the language.

    Parameters:
    None

    Returns: 
    Nothing
    """

    # Number of words you want to test
    n = int(input("Write the number of words you want to test: "))

    for x in range(n):
        word = input("Word to be tested: ")
        isPartOfLanguage = re.search("^C(erthas|irth|oirë|oranar|ormallen)$", word, re.IGNORECASE)
        if(isPartOfLanguage):
            print("yes")
        else:
            print("no")

# Calls the manualTests() function only if the script is executed directly
if __name__ == "__main__":
    manualTests()