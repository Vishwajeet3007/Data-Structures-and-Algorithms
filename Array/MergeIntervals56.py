def mergeIntervals(intervals):
    intervals.sort()
    ans = []
    for [x,y] in intervals:
        if not ans or ans[-1][1] < x:
            ans.append([x,y])
        elif ans[-1][1] < y:
            ans[-1][1] = y
    return ans
intervals = [[1,3],[2,6],[8,16],[15,18]]
print(mergeIntervals(intervals))
