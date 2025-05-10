def kidsWithExtraCandies(candies,extraCAndies):
    max_candies = max(candies)
    result = []
    for i in range(len(candies)):
        if candies[i] + extraCAndies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result
candies = [2,3,5,1,3]
extraCandies = 3
result = kidsWithExtraCandies(candies,extraCandies)
print(result)