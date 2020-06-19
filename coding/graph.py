


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

