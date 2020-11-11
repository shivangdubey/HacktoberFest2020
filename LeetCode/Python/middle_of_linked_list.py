"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        calculate the length of LL n
        Find middle n/2 if n is even else n/2 + 1
        traverse LL to reach middle element
        """
        temp = head
        length = 0
        while temp.next is not None:
            length += 1
            temp = temp.next

        mid = int(length / 2) if length % 2 == 0 else int(length / 2) + 1

        temp = head
        for i in range(mid):
            temp = temp.next

        return temp
