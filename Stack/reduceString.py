# 💡 Problem Summary
# You’re given a string made up of letters like "X", "Y", or "Z".
# The task is to:

# Remove all adjacent duplicates — like "XX", "YY" or "ZZ".
# If, after removing, new duplicates are formed, repeat the 
# process until no more adjacent duplicates exist.

# 🧠 Step-by-Step Thinking Process
# 🔹 Step 1: Understand with Examples
# Let’s try it manually to understand the behavior:

# Example 1:
# Input:  "XYYXX"
# Step 1:  X[Y Y]XX  →  X__XX  →  "X  X  X"
# Step 2:  [X X]X    →  __X    →  "X"
# Output: "X"

# Example 2:
# Input: "XYZYX"
# No adjacent duplicates → Output: "XYZYX"

# So we’re dealing with adjacent duplicates — and this should be 
# applied recursively, 
# because new pairs can form after removing previous ones.

# 🔹 Step 2: What Data Structure Helps?
# We need something that allows:
# Peeking the previous element (to check if current == previous)
# Pushing and popping

# ✅ A stack is perfect for this.
# Why?
# If current char == top of stack → pop it (i.e. remove pair)
# Else → push it
# This naturally simulates the recursive process, but iteratively.

# 🔹 Step 3: Pseudocode
# Here’s the logic before we code:

# initialize empty stack
# for each character in the string:
#     if stack is not empty and top of stack == character:
#         pop the stack (duplicate found)
#     else:
#         push the character onto the stack
# return joined stack as final string

# ⏱ Time & Space Complexity
# Time: O(n), each character is pushed/popped once

# Space: O(n) in worst case (no duplicates)

class Solution:
    def reduce_double_string(self, s):
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
                
        return ["".join(stack)]

solve = Solution()
s = "XYZZYX"
print(solve.reduce_double_string(s))
print(solve.reduce_double_string("XYZ")) 

# 🧠 Step-by-Step Trace: "XYZZYX"
# stack = []

# 'X' → push → ['X']

# 'Y' → push → ['X', 'Y']

# 'Z' → push → ['X', 'Y', 'Z']

# 'Z' → matches top → pop → ['X', 'Y']

# 'Y' → matches top → pop → ['X']

# 'X' → matches top → pop → []

# ✅ Final result: ''