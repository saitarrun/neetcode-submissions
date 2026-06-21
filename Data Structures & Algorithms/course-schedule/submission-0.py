class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # topological sort - dfs

        """ 
        0 -> 1
        """

        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)

        UNVISITED, VISITING, VISITED = 0,1,2
        state = [UNVISITED] * numCourses
        def dfs(start):
            state[start] = VISITING
            
            for neig in graph[start]:
                if state[neig] == VISITING:
                    return True 
                if state[neig] == UNVISITED:
                    if dfs(neig):
                        return True

            state[start] = VISITED
            return False
        
        for v in range(numCourses):
            if state[v] == UNVISITED:
                if dfs(v):
                    return False

        return True 


        
        