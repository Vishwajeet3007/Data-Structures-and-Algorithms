from typing import List
class Solution:
    def max_length(self,arr: List[str]):
        def getBitsMasks(s):
            mask = 0
            for ch in s :
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit :
                    return -1
                mask |= bit
            return mask
        def backtrack(index,curr_mask):
            nonlocal max_len
            max_len = max(max_len,bin(curr_mask).count('1'))
            for i in range(index,len(masks)):
                if masks[i] == -1 or (curr_mask & masks[i]) != 0:
                    continue
                backtrack(i+1,curr_mask | masks[i])
        masks = [getBitsMasks(s) for s in arr]
        max_len = 0
        backtrack(0,0)
        return max_len
    
# Create an instance of Solution
solution = Solution()

# Example test cases
arr = ["un", "iq", "ue"]
print(solution.max_length(arr))  # Output: 4

arr = ["cha", "r", "act", "ers"]
print(solution.max_length(arr))  # Output: 6

arr = ["abcdefghijklmnopqrstuvwxyz"]
print(solution.max_length(arr))  # Output: 26