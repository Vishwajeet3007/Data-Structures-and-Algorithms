def naive_sort_algorithm(text,pattern):
    n=len(text)
    m=len(pattern)
    matches=[]
    for i in range(n-m+1):
        j=0
        while j<m and text[i+j]==pattern[j]:
            j+=1
        if j==m:
            matches.append(i)
    return matches
text="AABACBAABAABA"
pattern="AABA"
matches=naive_sort_algorithm(text,pattern)
if matches:
    print("String found at index: ",matches)
else:
     print("String not found in the text.")
    
            