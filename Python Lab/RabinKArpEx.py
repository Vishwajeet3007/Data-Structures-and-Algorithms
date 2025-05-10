def rabin_karp(text,pattern):
    n=len(text)
    m=len(pattern)
    if n<m:
        return []
    matches=[]
    pattern_hash=hash(pattern)
    text_hash=hash(text[:m])
    for i in range(n-m+1):
        if text_hash==pattern_hash and text[i:i+m]==pattern:
            matches.append(i)
        if i<n-m:
            text_hash=hash(text[i+1:i+m+1])
    return matches
text="24364686443453243"
pattern="243"
matches=rabin_karp(text,pattern)
print("PAttern found in text at index:",matches)