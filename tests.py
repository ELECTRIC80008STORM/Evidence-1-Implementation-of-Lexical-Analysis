"""
Tests For The Lexical Analysis Script

This script tests the lexical analysis with
sets of words to test all scenarios
"""

import regex

count = 0

# Test 1 - Should not pass (not part of the language)
ans = regex.isPartOfLanguage("Catar")
if not ans:
    print("Test 1 passed")
    count += 1
else:
    print("Test 1 not passed")

# Test 2 - Should pass (part of the language)
ans = regex.isPartOfLanguage("coirë")
if ans:
    print("Test 2 passed")
    count += 1
else:
    print("Test 2 not passed")

# Test 3 - Should pass (part of the language)
ans = regex.isPartOfLanguage("Cormallen")
if ans:
    print("Test 3 passed")
    count += 1
else:
    print("Test 3 not passed")

# Test 4 - Should pass (part of the language)
ans = regex.isPartOfLanguage("Certhas")
if ans:
    print("Test 4 passed")
    count += 1
else:
    print("Test 4 not passed")

# Test 5 - Should not pass (not part of the language)
ans = regex.isPartOfLanguage("Lorem")
if not ans:
    print("Test 5 passed")
    count += 1
else:
    print("Test 5 not passed")

# Test 6 - Should pass (part of the language)
ans = regex.isPartOfLanguage("coranar")
if ans:
    print("Test 6 passed")
    count += 1
else:
    print("Test 6 not passed")

# Test 7 - Should not pass (not an exact match with any words)
ans = regex.isPartOfLanguage("Cormall")
if not ans:
    print("Test 7 passed")
    count += 1
else:
    print("Test 7 not passed")

# Test 8 - Should pass (part of the language)
ans = regex.isPartOfLanguage("Cirth")
if ans:
    print("Test 8 passed")
    count += 1
else:
    print("Test 8 not passed")

# Test 9 - Should pass (part of the language)
ans = regex.isPartOfLanguage("Coirë")
if ans:
    print("Test 9 passed")
    count += 1
else:
    print("Test 9 not passed")

# Test 10 - Should not pass (extra characters at the end)
ans = regex.isPartOfLanguage("Certhasabc")
if not ans:
    print("Test 10 passed")
    count += 1
else:
    print("Test 10 not passed")

# Test 11 - Should not pass (extra characters at the beginning)
ans = regex.isPartOfLanguage("abcCirth")
if not ans:
    print("Test 11 passed")
    count += 1
else:
    print("Test 11 not passed")

# Test 12 - Should not pass (not an exact match with any words)
ans = regex.isPartOfLanguage("Cor")
if not ans:
    print("Test 12 passed")
    count += 1
else:
    print("Test 12 not passed")

# Test 13 - Should pass (part of the language)
ans = regex.isPartOfLanguage("cOrAnAr")
if ans:
    print("Test 13 passed")
    count += 1
else:
    print("Test 13 not passed")

# Test 14 - Should not pass (not an exact match with any words)
ans = regex.isPartOfLanguage("Cermallen")
if not ans:
    print("Test 14 passed")
    count += 1
else:
    print("Test 14 not passed")

# Test 15 - Should not pass (not an exact match with any words)
ans = regex.isPartOfLanguage("Cormalln")
if not ans:
    print("Test 15 passed")
    count += 1
else:
    print("Test 15 not passed")

# Test 16 - Should pass (part of the language)
ans = regex.isPartOfLanguage("Cormallen")
if ans:
    print("Test 16 passed")
    count += 1
else:
    print("Test 16 not passed")

# Test 17 - Should not pass (not part of the language)
ans = regex.isPartOfLanguage("Elanor")
if not ans:
    print("Test 17 passed")
    count += 1
else:
    print("Test 17 not passed")

# Test 18 - Should not pass (empty string)
ans = regex.isPartOfLanguage("")
if not ans:
    print("Test 18 passed")
    count += 1
else:
    print("Test 18 not passed")

# Test 19 - Should not pass (not an exact match with any words)
ans = regex.isPartOfLanguage("C")
if not ans:
    print("Test 19 passed")
    count += 1
else:
    print("Test 19 not passed")

# Test 20 - Should not pass (not part of the language)
ans = regex.isPartOfLanguage("Xyz")
if not ans:
    print("Test 20 passed")
    count += 1
else:
    print("Test 20 not passed")

print("Passed", count, "of 20 tests")
