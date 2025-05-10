def naive_string_pattern(text,pattern):
    n=len(text)
    m=len(pattern)
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
text="ABCHEHSCCHBSDDVV"
pattern="HBSDD"
matches=naive_string_pattern(text,pattern)
print("Pattern found in text at index:",matches)