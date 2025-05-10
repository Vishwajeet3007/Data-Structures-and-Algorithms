def naive_string_matching(text,pattern):
    n=len(text)
    m=len(pattern)
    if n<m:
        return []
    matches=[]
    for i in range(n-m+1):
        matches_found=True
        for j in range(m):
            if text[i+j]!=pattern[j]:
                matches_found=False
                break
        if matches_found:
            matches.append(i)
    return matches
text="234542143853242413"
pattern="4243"
matches=naive_string_matching(text,pattern)
print("Pattern fount in text at index:",matches)
        