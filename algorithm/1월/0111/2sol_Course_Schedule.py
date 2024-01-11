# Leetcode 207.Course Schedule
# https://leetcode.com/problems/course-schedule/description/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        v = [0]*numCourses

        for target, prereq in prerequisites:
            graph[prereq].append(target)
            v[target] += 1

        q = deque()

        for i in range(numCourses):
            if not v[i]:
                q.append(i)

        while q:
            now = q.popleft()

            for next_class in graph[now]:
                if v[next_class] > 0:
                    v[next_class] -= 1
                    if not v[next_class]:
                        q.append(next_class)

        return all(not i for i in v)