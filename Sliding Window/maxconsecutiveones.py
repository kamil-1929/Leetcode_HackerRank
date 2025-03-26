# Max Consecutive Ones III


# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        max_len = 0
        zeros = 0
        
        for right in range(k, len(nums)):
            if nums[right] == 0:
                zeros +=1
            
            while zeros > k:
                if nums[left] ==0:
                    zeros -=1
                left +=1
            max_len = max(max_len, right -left + 1)
        return max_len
            

if __name__ == "__main__":
    solve = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    result = solve.longestOnes(nums, k)
    print(result)
    