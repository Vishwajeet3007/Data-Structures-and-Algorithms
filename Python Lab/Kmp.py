def kmp_table(pattern):
    # Initialize the table with zeros
    table = [0] * len(pattern)
    j = 0
    
    # Build the table using the KMP algorithm
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j
    return table

def kmp_search(pattern, text):
    if not pattern or not text:
        return -1  # Either pattern or text is empty
    
    table = kmp_table(pattern)
    j = 0
    
    # Iterate through the text using the KMP algorithm
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - len(pattern) + 1  # Pattern found at index i - len(pattern) + 1
    
    return -1  # Pattern not found in the text

# Example usage
pattern = "abc"
text = "ababcabcab"
index = kmp_search(pattern, text)
if index != -1:
    print(f"Pattern found at index {index}")
else:
    print("Pattern not found in the text")
