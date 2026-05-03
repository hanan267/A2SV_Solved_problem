class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for course, pre_req in prerequisites[0:]:
            graph[course].append(pre_req)

        order = []
        state = [0]*numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            elif state[node] == 2:
                return True
            
            state[node] = 1
            for adj in graph[node]:
                if not dfs(adj):
                    return False
            
            state[node] = 2
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
        



        

        
        