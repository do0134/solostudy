# leetcode 472. Concatenated Words
# https://leetcode.com/problems/concatenated-words/
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        answer = list()
        words_set = set(words)
        for word in words :
            check = 0
            words_set.remove(word)
            for i in range(len(word),0,-1) :
                if word[:i] in words_set :
                    print(word, word[:i])
                    check += 1
                if check == 2 :
                    answer.append(word)
                    break
            words_set.add(word)
        return answer