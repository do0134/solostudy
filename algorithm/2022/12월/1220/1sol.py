# leetcode 1971. Find if Path Exists in Graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        v = defaultdict(set)
        keys = set()
        if source == destination :
            return True
        
        for i,j in edges :
            v[i].add(j)
            v[j].add(i)
            keys.add(i)
            keys.add(j)
        keys = list(keys)
        for i in keys :
            v[i] = list(v[i])
        
        q = deque()
        for i in v[source] :
            if i == destination :
                return True
            q.append(i)
        v[source] = []

        while q :
            ce = q.popleft()
            if not v[ce] :
                continue
            for ne in v[ce] :
                if ne == destination :
                    return True
                q.append(ne)
            v[ce] = []

        return False