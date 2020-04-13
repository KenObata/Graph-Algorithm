
import math

def max_flow(Capa, s, t):
    n = len(Capa) # C is the capacity matrix
    Flow = [[0] * n for i in range(n)]
    Residual = Capa #build residual first time

    path = bfs(Capa, Residual, s, t) #find path from residual graph
    while(s in path):

        #find the bottlleneck
        min=math.inf
        for i in range(len(path)-1,0,-1):
            #debug
            #print("Residual[{}][{}]".format(path[i],path[i-1]),Residual[path[i]][path[i-1]])
            if(min>Residual[path[i]][path[i-1]]):
                min=Residual[path[i]][path[i-1]]
        #debug
        #print("min is:",min)

        #augment current Flow
        for i in range(len(path)-1,0,-1):
            Flow[path[i]][path[i-1]] +=min
            Residual[path[i]][path[i-1]] -=min
        
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
        
        #debug
        #print("{} is poped.".format(u))
        
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

    #debug
    #print("que",queue)
    #print("path",path)
    #print("parent_array",parent_array)
    return path



# make a capacity graph
# node s v1 v2  v3 v4  t
Capa = [[ 0, 16, 13, 0, 0, 0 ],  # s
     [ 0, 0, 0, 12, 0, 0 ],  # v1
     [ 0, 4, 0, 0, 14, 0 ],  # v2
     [ 0, 0, 9, 0, 0, 20 ],  # v3
     [ 0, 0, 0, 7, 0, 4 ],  # v4
     [ 0, 0, 0, 0, 0, 0 ]]  # t

source = 0
sink = 5
max_flow_value = max_flow(Capa, source, sink)

print("-----max_flow_value-----")
Flow=max_flow_value
for item in Flow:
    print(item)
