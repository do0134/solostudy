# 프로그래머스 불량사용자

from collections import defaultdict


# 가능한 모든 제재 아이디 조합 만들 dfs
# possible_list : banned_id를 키값으로, 키에 해당할 수 있는 제재 아이디를 value로 가짐
# banned : 이번 dfs에서 제재된 아이디 목록
# idx : possible_list.keys()의 idx
def dfs(possible_list: list, banned: list, idx: int):
    global answer_list

    # idx가 최대에 달하면 answer_list에 정렬된 banned 배열이 있는지 확인하고 append
    if idx >= len(possible_list.keys()):
        banned.sort()
        if banned not in answer_list:
            answer_list.append(banned)
        return

    key = sorted(possible_list.keys())[idx]
    for value in possible_list[key]:
        if value not in banned:
            dfs(possible_list, banned + [value], idx + 1)


# 가능한 제재 아이디 조합을 만드는 함수
# user_id, banned_id를 받아서 banned_id를 key로 가지고 키에 해당하는 제재 아이디 리스트를 value로 가진 possible dict return
# 이중 for문을 돌아 가능한 조합을 모두 뽑아낼 예정
def make_possible(user_id: list, banned_id: list) -> defaultdict:
    possible = defaultdict(list)
    # banned_id에 중복이 있기 때문에 ban_id 뒤에 str(banned_idx)를 붙여 key에 차별점을 둔다
    banned_idx = 0

    for ban in banned_id:
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                l = len(ban)
                cnt = 0
                for i in range(l):
                    if ban[i] == "*":
                        cnt += 1
                    elif ban[i] == user[i]:
                        cnt += 1
                    else:
                        break
                if cnt == l:
                    possible[ban + str(banned_idx)].append(user)

        banned_idx += 1

    return possible


def solution(user_id: list, banned_id: list) -> int:
    global answer_list
    answer_list = []

    possible = make_possible(user_id, banned_id)

    dfs(possible, [], 0)

    return len(answer_list)