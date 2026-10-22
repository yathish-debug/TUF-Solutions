from collections import deque
from typing import List

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()
        for i in range(V):
            if i not in visited:
                visited.add(i)
                q = deque([(i,i)])
                while q:
                    node, parent = q.popleft()
                    for n in adj[node]:
                        if n in visited and n != parent:
                            return True
                        if n not in visited:
                            visited.add(n)
                            q.append((n,node))
        return False

        