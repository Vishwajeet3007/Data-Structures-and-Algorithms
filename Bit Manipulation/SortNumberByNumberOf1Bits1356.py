def sortingNumberBy1Bits(arr):
    return sorted(arr,key=lambda x:(x.bit_count(),x))
arr =  [0,1,2,3,4,5,6,7,8]
print(sortingNumberBy1Bits(arr))