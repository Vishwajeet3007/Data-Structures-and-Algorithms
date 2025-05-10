

def rabin_karp(text,pattern):
    n=len(text)
    m=len(pattern)
    if n < m :
        return []
    
# Calculate the hash value of the pattern and the first window of text
    pattern_hash=hash(pattern)
    text_hash=hash(text[:m])
    matches=[]
    for i in range (n-m+1):
        if text_hash == pattern_hash and text[i:i+m]==pattern:
            matches.append(i)
        if i <n-m:
            text_hash =hash(text[i+1:i+m+1])
    return matches
text="AABACBAABAABAB"
pattern="AABA"
prime=10
matches=rabin_karp(text,pattern)
print("Pattern found at index : ",matches)