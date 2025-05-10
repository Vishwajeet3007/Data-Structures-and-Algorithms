def partitionLables(s):
    last_index = {char : i for i , char in enumerate(s)}
    result = []
    start = end = 0
    for i , char in enumerate(s):
        end = max(end,last_index[char])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result
s = "ababcbacadefegdehijhklij"
print(partitionLables(s))
s = "eccbbbbdec"
print(partitionLables(s))