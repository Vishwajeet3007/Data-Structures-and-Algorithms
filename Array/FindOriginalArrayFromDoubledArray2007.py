from collections import Counter
def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return  []
    changed.sort()
    count = Counter(changed)
    original = []
    for num in changed:
        if count[num] == 0:
            continue
        if count[2 * num] == 0:
            return []
        original.append(num)
        count[num] -= 1
        count[2 * num] -= 1
    return original
changed = [1,3,4,2,6,8]
print(findOriginalArray(changed))
changed = [6,3,0,1]
print(findOriginalArray(changed))
