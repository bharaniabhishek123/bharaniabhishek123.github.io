
from collections import defaultdict 

def create_graph(n , arr , graph):
    i = 0 
    while i < 2 * e :
        graph[arr[i]].append(arr[i + 1])
        i += 2 
    
def cycle_util(graph, vertex, visited, rec_stack):
    
    visited[vertex] = True
    rec_stack[vertex] = True 
    
    for neighbor in graph[vertex]:
        if visited[neighbor] == False:
            if cycle_util(graph, neighbor, visited, rec_stack) == True:
                return True
        elif rec_stack[neighbor] == True:
            return True 
    
    print("vertex", vertex) 
    print(rec_stack)
    rec_stack[vertex] = False
    return False

def isCyclic(n, graph):
    # Code here
    
    rec_stack = [False] * n 
    visited = [False] * n 

    for i in range(n):
        print("i :", i)
        if visited[i] == False:
            if cycle_util(graph, i, visited, rec_stack) == True:
                return True 
    return False 
            

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        create_graph(e, arr, graph)
        result = isCyclic(n, graph)
        print("result ", result)




