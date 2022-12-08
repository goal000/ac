def Astar(a,vis,src,dest):
    stk=[]
    cost=[]
    vc=[0]*n
    stk.append(src)
    cost.append(cost)
    path=[]
    c=0
    while( len(stk)>0 and stk[len(stk)-1]!=dest):
        ele=stk.pop()
        cost.pop()
        path.append(ele)
        for i in range(0,len(a)):
            if(a[ele][i]>0 and vis[i]==0):
                stk.insert(0,i)
                vc[i]=a[ele][i]+vc[ele];
                cost.insert(0,h[i]+vc[i])
                vis[i]=1
        sort(stk,cost)
    if(len(stk)==0):
        print("Goal state not found")
    else:
        path.append(dest)
        c=0
        for i in range(0,len(path)-1):
            c+=a[path[i]][path[i+1]]
        print("shortest path Goal found in this path  ",path,"with min cost ",c)

def sort(stk,cost):
    for i in range(0,len(stk)):
        for j in range(0,len(stk)-1):
            if(cost[j]<cost[j+1]):
                t=cost[j]
                cost[j]=cost[j+1]
                cost[j+1]=t
                t=stk[j]
                stk[j]=stk[j+1]
                stk[j+1]=t
print("Enter no of vertices : ")
n=int(input())
a=[]
for i in range(0,n):
    b=[0]*n
    a.append(b)
print("Enter edgs : ")
edgs=int(input())
print("Enter edgs as src to dest : ")
for i in range(0,edgs):
    src,dest,cost=map(int,input().split(" "))
    a[src][dest]=cost
    a[dest][src]=cost
h=[0]*n
print("Enter heuristic val for every vertex (node,val): ")
for i in range(n):
    src,val=map(int,input().split(" "))
    h[src]=val
print("Enter src ")
vis=[0]*n
src=int(input())
vis[src]=1
print("Enter dest ")
dest=int(input())
Astar(a,vis,src,dest)