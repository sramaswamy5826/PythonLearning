#leetcode 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperaturesBruteForce(self, temperatures:list[int])->list[int] :
        # Brute force approach
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
        return answer

    #timeComplexity: O(n^2) where n is the length of the temperatures array, since we have a nested loop.
    #spaceComplexity: O(n) where n is the length of the temperatures array, since we are using an additional array to store the answer.

    def dailyTemperatures(self  , temperatures:list[int])->list[int] :

        # Since the ask of this problem is to find the next greater element for each element in the temperatures array,
        # we can use a stack to keep track of the indices of the temperatures array.
        # idea is to use a Monotonic stack to keep track of the indices of the temperatures array.
        # Iterate through the temperatures array and for each temperature,
        # check if it is greater than the temperature at the index stored at the top of the stack.
        # If it is, we will pop the index from the stack and calculate the number of days to wait for a warmer temperature.
        # Continue this process until we find a temperature that is not greater than the temperature at the index stored at the top of the stack or until the stack is empty.
        # Finally, we will push the current index onto the stack.
        #* monotonic Increasing stack -  values are kept in increasing order, so that we can find the next greater element for each element in the temperatures array.

        n = len(temperatures)
        answer = [0] * n
        stack = []

        for current_day, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                previous_day = stack.pop()
                answer[previous_day] = current_day - previous_day #how many days to wait for a warmer temperature
            stack.append(current_day)

        return answer

#timeComplexity: O(n) where n is the length of the temperatures array.
#spaceComplexity: O(n) where n is the length of the temperatures array.

#Testcases
if __name__ == '__main__':
    solution = Solution()

    # Testcase 1: Example case
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = solution.dailyTemperatures(temperatures)
    print(result)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

    # Testcase 2: All temperatures are the same
    temperatures = [70, 70, 70]
    result = solution.dailyTemperatures(temperatures)
    print(result)  # Output: [0, 0, 0]

    # Testcase 3: Decreasing temperatures
    temperatures = [80, 75, 70]
    result = solution.dailyTemperatures(temperatures)
    print(result)  # Output: [0, 0, 0]

    # Testcase 4: Increasing temperatures
    temperatures = [60, 65, 70]
    result = solution.dailyTemperatures(temperatures)
    print(result)  # Output: [1, 1, 0]

