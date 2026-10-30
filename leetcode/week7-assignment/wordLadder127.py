#leetcode 127. Word Ladder
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Return 0 if there is no such transformation sequence.

class Solution:
    def ladderLength(self, beginword:str, endword:str, wordlist:list[str])->int:
        from collections import deque
        wordset = set(wordlist)
        if endword not in wordset:
            return 0

        queue = deque([(beginword, 1)])  # (current_word, current_length)

        while queue:
            current_word, current_length = queue.popleft()
            if current_word == endword:
                return current_length

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in wordset:
                        wordset.remove(next_word)  # mark as visited
                        queue.append((next_word, current_length + 1))

        return 0

    #time complexity: O(M*N) where M is the length of each word and N is the number of words in the word list
    #space complexity: O(N) for the queue and the word set

