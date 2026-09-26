#leetcode 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.

# Can be done in two pass.First pass to get the length of the list, then second pass to remove the nth node from the end.
# Solution is to do it in one-pass. Using two pointers, first and second n distance apart.
# first pointer is n+1 steps ahead, move until first reaches the end, then move both pointers until first reaches the end.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionTwoPass:
    def removeNodes(self, head:ListNode|None, n:int) -> ListNode|None:
        # First pass to get the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        if length < n:
            return head

        # Calculate the position of the node to remove from the start
        position = length - n

        # Create a dummy/sentinel node to simplify edge cases
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        # Second pass to remove the nth node from the end
        for _ in range(position):
            current = current.next

        # Remove the nth node from the end
        tmp = current.next
        current.next = current.next.next
        tmp.next = None # clean up the removed node's next pointer to avoid memory leaks

        return dummy.next

class SolutionOnePass:
    def removeNodes(self, head:ListNode|None, n:int) -> ListNode|None:
        # Create a dummy/sentinel node to simplify edge cases
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            if first is None:
                return head  # n is greater than the length of the list
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        tmp = second.next
        second.next = second.next.next
        tmp.next = None # clean up the removed node's next pointer to avoid memory leaks

        return dummy.next

#Testcases
if __name__ == '__main__':
    solution = SolutionTwoPass()
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    new_head = solution.removeNodes(head, 2)
    # Print the modified linked list: 1 -> 2 -> 3 -> 5
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

    solution = SolutionOnePass()
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    new_head = solution.removeNodes(head, 2)
    # Print the modified linked list: 1 -> 2 -> 3 -> 5
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

#Time complexity: O(L) where L is the length of the linked list.
#Space complexity: O(1) since we are using a constant amount of space.

