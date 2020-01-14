"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0]and thus will not appear together in edges.
"""
# DFS
class Solution(object):
    def validTree(self, n, edges):
        lookup = collections.defaultdict(list)
        for edge in edges:
            lookup[edge[0]].append(edge[1])
            lookup[edge[1]].append(edge[0])
        visited = [False] * n

        if not self.helper(0, -1, lookup, visited):
            return False

        for v in visited:
            if not v:
                return False

        return True

    def helper(self, curr, parent, lookup, visited):
        print curr, visited
        if visited[curr]:
            return False
        visited[curr] = True
        for i in lookup[curr]:
            if (i != parent and not self.helper(i, curr, lookup, visited)):
                return False

        return True

if __name__ == '__main__':
    print Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])　

#  BFS, Time: O(|V| + |E|), Space: O(|V| + |E|)

class Solution(object):
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        if len(edges) != n - 1:  # Check number of edges.
            return False

        # init node's neighbors in dict
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        # BFS to check whether the graph is valid tree.
        visited = {}
        q = collections.deque([0])
        while q:
            curr = q.popleft()
            visited[curr] = True
            for node in neighbors[curr]:
                if node not in visited:
                    visited[node] = True
                    q.append(node)

        return len(visited) == n

# Union Find
class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        root = [i for i in range(n)]
        for i in edges:
            root1 = self.find(root, i[0])
            root2 = self.find(root, i[1])
            if root1 == root2:
                return False
            else:
                root[root1] = root2
        return len(edges) == n - 1

    def find(self, root, e):
        if root[e] == e:
            return e
        else:
            root[e] = self.find(root, root[e])
            return root[e]　　
