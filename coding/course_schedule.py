""" 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""

def check_cycle(vertex, adj_list, visited, recursion_stack):
    visited[vertex] = True 
    recursion_stack[vertex] = True 

    for neighbor in adj_list[vertex]:
        if visited[neighbor] == False :
            check_cycle(neighbor, adj_list, visited, recursion_stack)
        elif recursion_stack[neighbor] == True:
            return False 
    
    recursion_stack[vertex] = False 
    return True  # there is no cycle 


def canFinish(numCourses, prerequisites):

    # pre-requisites is edge list , convert it to adj list

    adj_list = [[] for _ in range(numCourses)]

    for edge in prerequisites:
        src, dest = edge 
        adj_list[src].append(dest)

    print(adj_list)

    # 0->1   [[], [0]]
    # 0->1, 0->1 [[1], [0]]
    # 0->1, 2->0, 1->2 [[2],[0],[1]]

    visited = [False] * numCourses
    recursion_stack = [False] * numCourses 

    for i in range(numCourses):
        if visited[i] == False :
            check_cycle(i, adj_list, visited, recursion_stack)
    return True 







"""
visted[0,1,2], rec_stack[0,1] = True

for neighbor in graph[2]: 
    # neighbor = 1 not visited , again do a recursive call
    # neighbor = 2 not visited , again do a recursice call
    # neighbor = 0 visited, if it's in rec stack return True 
    #                                            else False rec_stack[vertex] = False
    
"""


def test_canFinish():
    numCourses1 = 2 
    prerequisites1 = [[1,0], [0,1]]

    numCourses2 = 2 
    prerequisites2 = [[1,0]]

    numCourses3 = 3
    prerequisites3 = [[1,0], [2,1], [0,2]]

    print(canFinish(numCourses1, prerequisites1))

test_canFinish()

