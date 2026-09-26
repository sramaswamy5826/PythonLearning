#LEETCODE 622. Design Circular Queue

class Node(object):
    def __init__(self, value:int) -> None:
        self.value = value
        self.next = None

class MyCircularQueue:
    def __init__(self, k:int) -> None:
        self.capacity = k
        self.count = 0
        self.head = None
        self.tail = None

    #insert value into the circular queue
    def enQueue(self, value:int)->bool:
        if self.count == self.capacity:#full queue, cannot insert new value
            return False
        new_node = Node(value)
        if self.count == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return True
    #Time complexity of enQueue is O(1) because we are inserting the new value at the end of the queue, which takes constant time.

    #delete value from the circular queue
    def deQueue(self)->bool:
        if self.count == 0:#empty queue, cannot delete value
            return False
        self.head = self.head.next
        self.count -=1

        if self.count == 0:
            self.tail = None
        return True
    #Time complexity of deQueue is O(1) because we are removing the value from the front of the queue, which takes constant time.

    #Return element from front of the queue
    def Front(self)->int:
        if self.count == 0: return -1
        return self.head.value
    #Time complexity of Front is O(1) because we are accessing the value at the front of the queue, which takes constant time.

    #Return element from rear of the queue
    def Rear(self)->int:
        if self.count == 0: return -1
        return self.tail.value
    #Time complexity of Rear is O(1) because we are accessing the value at the rear of the queue, which takes constant time.

    def isEmpty(self)->bool:
        return self.count == 0

    def isFull(self)->bool:
        return self.capacity == self.count

#Testcases
if __name__ == '__main__':
    circularQueue = MyCircularQueue(3) # set the size to be 3
    print(circularQueue.enQueue(1))  # return True
    print(circularQueue.enQueue(2))  # return True
    print(circularQueue.enQueue(3))  # return True
    print(circularQueue.enQueue(4))  # return False, the queue is full
    print(circularQueue.Rear())       # return 3
    print(circularQueue.isFull())     # return True
    print(circularQueue.deQueue())    # return True
    print(circularQueue.enQueue(4))   # return True
    print(circularQueue.Rear())       # return 4
