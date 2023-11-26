#2942. Find Words Containing Character
class Solution:
    def findWordsContaining(self, words, x):
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result


solution = Solution()

words1 = ["leet", "code"]
x1 = "e"
print(solution.findWordsContaining(words1, x1))

words2 = ["abc", "bcd", "aaaa", "cbc"]
x2 = "a"
print(solution.findWordsContaining(words2, x2))

words3 = ["abc", "bcd", "aaaa", "cbc"]
x3 = "z"
print(solution.findWordsContaining(words3, x3))