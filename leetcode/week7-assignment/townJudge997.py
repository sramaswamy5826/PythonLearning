#leetcode 997. Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# 1. The town judge trusts nobody.
# 2. Everybody (except for the town judge) trusts the town judge.
# 3. There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

#example: trust = [[1,3],[2,3],[4,3],[4,1],[5,3],[5,1],[5,4]] n = 5

class Solution:
    def findJudge(self, n:int, trust:list[list[int]]) -> int:
         #Graph, using indegree and outdegree to find the judge

         if len(trust) < n-1:  # If there are fewer trust relationships than n-1, the judge cannot exist
             return -1

         indegree = [0] * (n + 1)  # Count of people who trust each person.
         outdegree = [0] * (n + 1)  # Count of people each person trusts
         # doing n+1 because we want to use 1-based indexing for people labels

        # Count indegree and outdegree for each person
         for a, b in trust:
             outdegree[a] += 1
             indegree[b] += 1

         #iterate through all people to find the judge
         for i in range(1, n + 1):
             if indegree[i] == n - 1 and outdegree[i] == 0:
                 return i #found the judge

         return -1 #no judge found

#testcases
if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(5, [[1,3],[2,3],[4,3],[4,1],[5,3],[5,1],[5,4]]))  # Output: 3
    print(s.findJudge(3, [[1,2],[2,3]]))  # Output: -1
    print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))  # Output: 3
    print(s.findJudge(2, [[1,2]]))  # Output: 2
    print(s.findJudge(1, []))  # Output: 1

#TIME COMPEXITY: O(n + m) where n(nodes) is the number of people and m(edges) is the number of trust relationships
#space complexity: O(2n) =~ O(n) for indegree and outdegree arrays
