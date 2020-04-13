# This program calculates maximum number of matching from a given graph.
# By using Edmonds carp algorithm, this can find maximum number of matching
# and its detail combination by O(VE) runtime.

import math


def max_flow(Capa, s, t):
    n = len(Capa) # Capa is the capacity matrix
    Flow = [[0] * n for i in range(n)]
    Residual = Capa #build residual first time

    path = bfs(Capa, Residual, s, t) #find path from residual graph
    while(s in path):

        #find the bottlleneck
        min=math.inf
        for i in range(len(path)-1,0,-1):
            
            if(min>Residual[path[i]][path[i-1]]):
                min=Residual[path[i]][path[i-1]]

        #augment current Flow
        for i in range(len(path)-1,0,-1):
            Flow[path[i]][path[i-1]] +=min
            Residual[path[i]][path[i-1]] -=min
        
        #debug
        for item in Flow:
            print(item)
        
        #repeat BFS
        path = bfs(Capa, Residual, s, t)

    return Flow

def bfs(Capa, Residual, s, t):
    n = len(Capa)
    queue = [s]
    path=[t]#output
    
    parent_array=[0]*n #s,v1,v2,v3,v4,t
    marked_array=[s] #s,v1,v2,v3,v4,t
    
    while(queue):#while Que is not empty
        u=queue.pop(0)
        
        
        if(u == t):
            parent = parent_array[n-1] #first parent is parent of t
            path.append(parent)
            while parent != s:
                parent=parent_array[parent]
                path.append(parent)
        
        else: # do BFS
            for v in range(n):
                if(Residual[u][v]>0 and v not in marked_array):
                # it means there exists a path
                    marked_array.append(v)
                    parent_array[v]=u
                    queue.append(v)

    return path


# capacity of bipartitie graph
        #node s L1 L2  L3 L4 L5|R6 R7 R8 R9 t
Capa     = [[ 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], # s
           [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # L1
           [ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # L2
           [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],  # L3
           [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # L4
           [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # L5
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # R6
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # R7
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # R8
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # R9
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]   # t
            ]

source = 0
sink = 10
max_flow_value = max_flow(Capa, source, sink)

print("-----Final output of max_flow_value-----")
Flow=max_flow_value
for item in Flow:
    print(item)

left_nodes=[i for i in range(len(max_flow_value[0])) if max_flow_value[0][i] == 1 ]
right_nodes=[]
print("source maps to:", left_nodes)

while(len(left_nodes)>0):
    node = left_nodes.pop(0)
    for i in range(len(max_flow_value[node])):
        if max_flow_value[node][i] == 1:
            print("node:",node," maps to node:", i)

