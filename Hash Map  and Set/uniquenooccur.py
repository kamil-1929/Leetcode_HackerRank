# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 

# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        frequency = Counter(arr)
        values = frequency.values()
        return len(set(values)) == len(values)
        
solve = Solution()
arr = [1,2,2,1,1,3]
print(solve.uniqueOccurrences(arr))


class Solution:
    def uniqueOccurrences1(self, arr: list[int]) -> bool:
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        
        freq_values = freq.values()
        
        return len(freq_values) == len(set(freq_values))
    
solve = Solution()
arr = [1,2,2,1,1,3]
print(solve.uniqueOccurrences1(arr))