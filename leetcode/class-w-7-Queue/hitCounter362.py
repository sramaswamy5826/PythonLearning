#leetcode 362. Design Hit Counter
# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
# Your system should accept a timestamp parameter (in seconds  granularity) and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# Implement the HitCounter class:
# HitCounter() Initializes the hit counter system.
# void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits   may happen at the same timestamp.
# int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

class HitCounter:
    def __init__(self):


    def hit(self, timestamp: int) -> None:
        pass

    def getHits(self, timestamp: int) -> int:
        pass


#testcases
if __name__ == '__main__':
    hit = HitCounter()
    hit.hit(1)
    hit.hit(2)
    hit.hit(3)

    print(hit.getHits(4))  # Output: 3



