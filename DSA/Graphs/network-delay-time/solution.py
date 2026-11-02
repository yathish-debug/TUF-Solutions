import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        adj = [[] for _ in range(n+1)]
        for u,v,weight in times:
            adj[u].append((v,weight))
            
        print(adj)
        dist = [float('inf')]*(n+1)
        print(dist)
        dist[k]=0
        q=[(0,k)]
        while q:
            current_dist, node = heapq.heappop(q)
            if current_dist > dist[node]:
                continue
            for next_node, weight in adj[node]:
                new_dist = current_dist + weight
                if new_dist < dist[next_node]:
                    dist[next_node] = new_dist
                    heapq.heappush(q, (new_dist, next_node))
        print(dist)
        for i in dist[1:]:
            if i == float('inf'):
                return -1
            
        return max(dist[1:])
        

'''
visited is an array of length n
start with k, t=0

    if not visited 
    visit all the outgoing nodes from k
    update t = t+wi
visited = [0,0,0,0]
q = [(k,0)]

iteration 1:
    node = k
    time = 0
    loop through times:
        if an edge is starting from node:
            update time = time + w of new edge
            add that new node to q
            visited = [0,0,1,0]
    t = 0

'''