'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
Accepted
'''

"""
visualize the list to graph and the process
N =6
p = [[2,1],[4,1],[3,2],[5,4]]

0
     1
   /   \
  2     4
 /       \
3         5

todo = {0: set(), 1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
graph =  {1: {2, 4}, 2: {3}, 4: {5}})
todo = {0: set(), 1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
node 0
todo = {1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
node 1
todo = {2: set(), 3: {2}, 4: set(), 5: {4}}
node 2
todo = {3: set(), 4: set(), 5: {4}}
node 4
todo = {3: set(), 5: set()}
node 3
todo = {5: set()}
node 5
todo= {}
N =6
p = [[2,1],[4,1],[3,2],[5,4],[2,3]]

0
     1
   /   \
  2     4
 //       \
3         5

# initial
todo = {0: set(), 1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
graph =  {1: {2, 4}, 2: {3}, 4: {5}, 3: {2}})

# processing
todo = {0: set(), 1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
node 0
todo = {1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
node 1
todo = {2: {3}, 3: {2}, 4: set(), 5: {4}}
node 4
todo ={2: {3}, 3: {2}, 5: set()}
node 5
todo ={2: {3}, 3: {2}}

# No nodes' indegree equals 0, so nothing will be append to the queue.
# Queue becomes empty, the while loop stop. If the indegree_item has items,it means it has cycle.
"""
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]

        for i in prerequisites:
            indegree[i[0]] += 1
            graph[i[1]].append(i[0])

        queue = deque()
        for i in range(len(indegree)):
            if not indegree[i]:
                queue.append(i)

        counter = 0
        while len(queue) > 0:
            cur = queue.popleft()
            counter += 1

            for i in range(len(graph[cur])):
                indegree[graph[cur][i]] -= 1
                if indegree[graph[cur][i]] == 0:
                    queue.append(graph[cur][i])

        return numCourses == counter
