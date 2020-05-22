from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        coursesList = []
        edges = {i:[] for i in range(numCourses)}
        degrees = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            edges[y].append(x)
            degrees[x] += 1
            
        queue = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)
                
        courses = 0
        while queue:
            prerequisite = queue.popleft()
            courses += 1
            coursesList.append(prerequisite)
            for course in edges[prerequisite]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    queue.append(course)
        
        if courses != numCourses:
            return []
        return coursesList
    