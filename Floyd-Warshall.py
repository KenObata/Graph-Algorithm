#Floyd-Warshall program
# This program uses Floyd-Warshall program to compute all pair shortest path.
# Runtime is O(n^3).

import math

# make a initial graph
D0 = [
     [0, 3, 8, math.inf, -4 ],
     [math.inf, 0, math.inf, 1, 7 ],
     [math.inf, 4, 0, math.inf, math.inf ],
     [2, math.inf, -5, 0, math.inf ],
     [math.inf, math.inf, math.inf, 6, 0 ]
     ]

memorized_D0=[
             [0, 1, 1, 0, 1 ],
             [0, 0, 0, 2, 2 ],
             [0, 3, 0, 0, 0 ],
             [4, 0, 4, 0, 0 ],
             [0, 0, 0, 5, 0]
             ]
#initialize
n=len(D0)
D_matrix=[D0]
memorized_table=[memorized_D0]

for i in range(n):
    D_matrix.append(D0)
    memorized_table.append(memorized_D0)


for line in D0:
    print(line)
print("memorized table")
for line in memorized_D0:
    print(line)

for k in range(1,n+1):#n
    #debug
    print("------------------")
    print("k=",k)
    
    for i in range(n):
        for j in range(n):
            if(i!=k-1 and j!=k-1 and i!=j):
                
                if(D_matrix[k-1][i][j] < D_matrix[k-1][i][k-1]+D_matrix[k-1][k-1][j]):
                    D_matrix[k][i][j]=D_matrix[k-1][i][j]
                    memorized_table[k][i][j]=memorized_table[k-1][i][j]

                elif(D_matrix[k-1][i][j]==math.inf and D_matrix[k-1][i][k-1]+D_matrix[k-1][k-1][j]==math.inf):
                    
                        #update D value
                        D_matrix[k][i][j]=D_matrix[k-1][i][k-1]+D_matrix[k-1][k-1][j]
                        #but don't update parent table
                        memorized_table[k][i][j]=memorized_table[k-1][i][j]

                else:
                    D_matrix[k][i][j]=D_matrix[k-1][i][k-1]+D_matrix[k-1][k-1][j]
                    memorized_table[k][i][j]=memorized_table[k-1][k-1][j]

    #output
    for line in D_matrix[k]:
        print(line)
    print("memorized table")
    for line in memorized_table[k]:
        print(line)




