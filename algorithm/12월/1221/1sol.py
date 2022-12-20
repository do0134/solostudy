class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = [0] * len(rooms)
        q = deque()
        q.append(0)
        v[0] = 1 
        while q :
            c_idx = q.popleft()
            for idx in rooms[c_idx] :
                if not v[idx] :
                    v[idx] = 1
                    q.append(idx)
        
        return not 0 in v