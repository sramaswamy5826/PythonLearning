#leetcode 933. Number of Recent Calls
# You have a RecentCounter class which counts the number of recent requests within a certain time frame
# Implement the RecentCounter class:
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time
# in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
# Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value
# of t than the previous call.

# using sliding window technique to store the timestamps of the requests
# and remove the requests that are outside the 3000 milliseconds range.

class RecentCounter:
    def __init__(self):
        self.requests = [] # array to store the timestamps of the requests

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0) #O(n) time complexity for pop(0) operation, can be optimized using deque
        return len(self.requests)

#Time complexity: O(n) for pop(0) operation
#Space complexity: O(n) for storing the timestamps of the requests

# dequeue is used to optimize the pop(0) operation to O(1) time complexity instead of O(n) time complexity.
class RecentCounterDeque:
    def __init__(self):
        from collections import deque
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

#Time complexity: O(1) for pop(0) operation
#Space complexity: O(n) for storing the timestamps of the requests

#Testcases
if __name__ == '__main__':
    recentCounter = RecentCounter()
    print(recentCounter.ping(1))
    print(recentCounter.ping(100))
    print(recentCounter.ping(3001))
    print(recentCounter.ping(3002))

    print('Testcase 2')
    recentCounterDeque = RecentCounterDeque()
    print(recentCounterDeque.ping(10))
    print(recentCounterDeque.ping(50))
    print(recentCounterDeque.ping(3000))

