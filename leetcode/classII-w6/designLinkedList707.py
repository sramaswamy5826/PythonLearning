#leetcode 707. Design Linked List
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.

class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = LinkedListNode()
        self.size = 0

    def addAtHead(self, val):
        node = LinkedListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val):
        node = LinkedListNode(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        node = LinkedListNode(val)
        current = self.head
        for _ in range(index):
            current = current.next
        node.next = current.next
        current.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1

# testcases
if __name__ == '__main__':
    myLinkedList = SingleLinkedList()
    myLinkedList.addAtHead(1)
    print(myLinkedList.head.val)

# Doubly linked list implementation
class doubleLinkedListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = doubleLinkedListNode()
        self.tail = doubleLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addAtHead(self, val):
        node = doubleLinkedListNode(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def addAtTail(self, val):
        node = doubleLinkedListNode(val)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        node = doubleLinkedListNode(val)
        node.next = current.next
        node.prev = current
        current.next.prev = node
        current.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        current.next.prev = current






