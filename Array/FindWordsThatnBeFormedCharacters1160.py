from collections import Counter
def total_length(words,chars):
    chars_count = Counter(chars)
    total_len = 0
    for word in words:
        word_count = Counter(word)
        if all(word_count[c] <= chars_count[c] for c in word_count):
            total_len += len(word)
    return total_len
words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(total_length(words,chars))