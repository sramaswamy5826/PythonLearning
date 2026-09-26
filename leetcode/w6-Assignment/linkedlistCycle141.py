#leetcode 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#testcases
if __name__ == '__main__':
    #create a linked list with a cycle
    #head = [3, 2, 0, -4] p=1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next # create a cycle

    sol = Solution()
    print("output1 > ", sol.hasCycle(head))

    #create a linked list with a cycle,node 2 points to node 1
    #head = [1, 2] p=0
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head # create a cycle
    print("output2 > ", sol.hasCycle(head))

    #create a linked list with no cycle, node 1 points to None
    #head = [1] p=-1
    head = ListNode(1)
    print("output3 > ", sol.hasCycle(head))

    #create a linked list with a cycle, node 3 points to node 2
    #head = [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next = head.next # create a cycle
    print("output4 > ", sol.hasCycle(head))

#Timecomplexity: O(n) where n is the number of nodes in the linked list.
#Space complexity: O(1)