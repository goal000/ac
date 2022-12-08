def bestfs(a,vis,src):
    stk=[]
    cost=[]
    stk.append(src)
    cost.append(cost)
    while(len(stk)>0):
        ele=stk.pop()
        cost.pop()
        print(ele,end=" ")
        for i in range(0,len(a)):
            if(a[ele][i]>0 and vis[i]==0):
                stk.insert(0,i)
                cost.insert(0,h[i])
                vis[i]=1
        sort(stk,cost)
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
bestfs(a,vis,src)
