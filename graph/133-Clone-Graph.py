'''
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.



Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
'''
# DFS recursively
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None

        self.visited = dict()
        node_copy = Node(node.val, [])
        self.visited[node] = node_copy
        self.dfs(node)
        return node_copy

    def dfs(self, node):
        for neighbor in node.neighbors:
            if neighbor not in self.visited:    # add the neighbor node to visited dict
                neighbor_copy = Node(neighbor.val, [])
                self.visited[neighbor] = neighbor_copy
                self.visited[node].neighbors.append(neighbor_copy)
                self.dfs(neighbor)
            else:   # use the neighbor node in the visited dict
                self.visited[node].neighbors.append(self.visited[neighbor])

# DFS + Stack
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None

        self.visited = dict()
        node_copy = Node(node.val, [])
        self.visited[node] = node_copy
        self.stack = [node]

        while len(self.stack) > 0:
            node = self.stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in self.visited:    # add the neighbor node to visited dict
                    neighbor_copy = Node(neighbor.val, [])
                    self.visited[neighbor] = neighbor_copy
                    self.visited[node].neighbors.append(neighbor_copy)
                    self.stack.append(neighbor)
                else:   # use the neighbor node in the visited dict
                    self.visited[node].neighbors.append(self.visited[neighbor])

        return node_copy

#BFS + Queue
import collections
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None

        self.visited = dict()
        node_copy = Node(node.val, [])
        self.visited[node] = node_copy
        self.queue = collections.deque([node])

        while len(self.queue) > 0:
            node = self.queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in self.visited:    # add the neighbor node to visited dict
                    neighbor_copy = Node(neighbor.val, [])
                    self.visited[neighbor] = neighbor_copy
                    self.visited[node].neighbors.append(neighbor_copy)
                    self.queue.append(neighbor)
                else:   # use the neighbor node in the visited dict
                    self.visited[node].neighbors.append(self.visited[neighbor])

        return node_copy
