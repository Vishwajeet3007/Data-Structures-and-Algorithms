def RabinKarp(text,pattern,prime):
    n=len(text)
    m=len(pattern)
    p=0
    t=0
    h=1
    d=256
 # Calculate h = d^(m-1) % prime
    for i in range(m-1):
        h=(h*d)%prime
#Calculate hash value for pattern and the first window of text
    for i in range(m):
        p=(d*p+ord(pattern[i]))%prime
        t=(d*t+ord(text[i]))%prime
    matches=[]
    for i in range(n-m+1):
        if p==t:
            match=True
            for j in range(m):
                if pattern[j]!=text[i+j]:
                    match=False
                    break
            if match:
                matches.append(i)
        if i<n-m:
            t=(d*(t-ord(text[i])*h)+ord(text[i+m]))%prime
        if t<0:
            t+=prime
    return matches
text="AABACBAABAABAB"
pattern="AABA"
prime=101
matches=RabinKarp(text,pattern,prime)
if matches:
    print("String found at index: ",matches)
else:
     print("String not found in the text.")
  