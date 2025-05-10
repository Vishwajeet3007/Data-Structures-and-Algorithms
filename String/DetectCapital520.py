def detectCapitalUse(word):
    # return (word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()))
    # return (word.isupper() or word.islower() or word.istitle())

    capital_count = 0
    for char in word:
        if 'A'<= char <= 'Z':
            capital_count += 1
    if capital_count == 0 or capital_count == 1 or capital_count == len(word):
        return True
    return False
word = "USA"
print(detectCapitalUse(word))
word = "FlaG"
print(detectCapitalUse(word))