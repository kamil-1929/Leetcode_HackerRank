# 283. Move Zeroes
# Easy

# Given an integer array nums, move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of 
# the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?


class MoveZero:
    def moveZeroes(self, nums:list[int]) -> None:
        last_non_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero +=1
        return nums 
    
if __name__ == "__main__":
    solve = MoveZero()
    nums = [0,1,0,3,12]
    result = solve.moveZeroes(nums)
    print(result)