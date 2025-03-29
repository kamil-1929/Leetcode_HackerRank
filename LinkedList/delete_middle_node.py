# 2095. Delete the Middle Node of a Linked List

# Hint
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

# Example 1:


# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 
# Example 2:


# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
# Example 3:


# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 1 <= Node.val <= 105

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        
        slow = head 
        fast = head 
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next 
            
        prev.next = slow.next
        
        return head
            
#helper to build LinkedList for testing
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head 
        
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_ll(head):
    while head:
        print(head.val, end="-> " if head.next else "\n")
        head = head.next


       
if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1,2,3,4,5])
    new_head = sol.deleteMiddle(head)
    print_ll(new_head)