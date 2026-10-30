class Solution:
    def findCity(self, n, m, edges, distanceThreshold):
        adj_mat = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            adj_mat[i][i] = 0
        for u, v, w in edges:
            adj_mat[u][v] = w
            adj_mat[v][u] = w 
        print(adj_mat)
        
        rows = len(adj_mat)
        cols = len(adj_mat[0])
        matrix = adj_mat
        for via in range(n):
            for i in range(rows):
                for j in range(cols):
                    matrix[i][j] = min(matrix[i][j], (adj_mat[i][via] + adj_mat[via][j]) )

        dic = {i: [] for i in range(n)}
        mini = float('inf')
        for a in range(len(matrix)):
            for b in range(len(matrix[0])):
                if matrix[a][b]<= distanceThreshold and a!=b:
                    dic[a].append(b)
            mini = min( mini, len(dic[a]))
        array=[]
        for key, value in dic.items():
            if len(value)==mini:
                array.append(key)
        return array[-1]

'''
dictionary = i need to find the distance of all cities from all vertices under threshold and keep track of minimum connectivity
mini = minimum connectivity
maintain a min variable = 1
loop through dictionary: to find the vertices with minimum value 
    return the last element


loop through all the vertices:
    loop through all the rows:
        loop through all the cols:
            matrix(v) = min(cost(v), (cost(u) + edge(uv))) 

mini=1
dic=[[]*n]
loop through rows:
    loop through cols:
        if matrix[i][j]<threshold:
            dic[i].append(j)
    mini = min( mini,  len(dic[i])

minimum_connectivity=[]
loop through dic:
    minimum_connectivity.append(i)

    return minimum_connectivity[-1]

TC = O(n^3 + (n-1)*m + n)
SC = O((n-1)*m + (n-1)*m )

'''