# Leetcode 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 수가 비어있다면 return
        if not digits:
            return []
        # 숫자에 해당하는 알파벳 연결하기
        idx = 97
        num_dict = defaultdict(list)

        for i in range(2,10):
            if i == 7 or i == 9:
                value = 4
            else:
                value = 3
            for _ in range(value):
                num_dict[str(i)].append(chr(idx))
                idx += 1

        # BFS로 완전탐색을 돌며, 가능한 모든 조합을 뽑아내기
        answer = list()

        q = deque()

        q.append((list(digits), []))

        while q:
            now, word = q.popleft()
            # 입력받은 digits와 만든 word의 길이가 같다면 answer에 넣어준다.
            if len(word) == len(digits):
                answer.append("".join(word))
            else:
                # 아니라면 now[1:]과 word에 알파벳을 더한 것을 넣어준다.
                # 순서대로 순회하기 때문에 중복은 없다.
                for i in num_dict[now[0]]:
                    q.append((now[1:],word+[i]))

        return answer