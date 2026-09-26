#Leetcode 21. Merge Two Sorted Lists
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode|None, list2:ListNode|None) -> ListNode|None:
        #create a sentinelNode node to hold the merged list
        sentinelNode = ListNode()
        #create a pointer to the current node in the merged list
        current = sentinelNode
        #while both lists are not empty
        while list1 and list2:
            #compare the values of the current nodes in both lists
            if list1.val < list2.val:
                #if list1's value is smaller, add it to the merged list
                current.next = list1
                #move to the next node in list1
                list1 = list1.next
            else:
                #if list2's value is smaller or equal, add it to the merged list
                current.next = list2
                #move to the next node in list2
                list2 = list2.next
            #move to the next node in the merged list
            current = current.next
        #if one of the lists is empty, append the other list to the merged list
        #append any remaining nodes from either list
        current.next = list1 or list2
        #return the merged list, which starts at sentinelNode.next
        return sentinelNode.next

    def print_linked_list(self, head: ListNode | None):
        current = head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

#Testcases
if __name__ == '__main__':
    #create two sorted linked lists
    #list1 = [1, 2, 4]
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    #list2 = [1, 3, 4]
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    sol = Solution()
    mergedList = sol.mergeTwoLists(list1, list2)
    sol.print_linked_list(mergedList)

    l1 = None
    l2 = None
    mergedList = sol.mergeTwoLists(l1, l2)
    sol.print_linked_list(mergedList)

    l1 = None
    l2 = None
    mergedList = sol.mergeTwoLists(l1, l2)
    sol.print_linked_list(mergedList)

    l1 = None
    l2 = ListNode(0)
    mergedList = sol.mergeTwoLists(l1, l2)
    sol.print_linked_list(mergedList)

    #negative node values
    l1 = ListNode(-10)
    l1.next = ListNode(-5)
    l2 = ListNode(-7)
    mergedList = sol.mergeTwoLists(l1, l2)
    sol.print_linked_list(mergedList)

    #Time complexity: O(n + m), where n and m are the lengths of two linked lists.
    #Space complexity: O(1)

