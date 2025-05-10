def findArray(pref):
    for i in range(len(pref)-1,0,-1):
        pref[i] = pref[i] ^ pref[i-1]
    return pref
pref = [5,2,0,3,1]
print(findArray(pref))