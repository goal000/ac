def df(a,vis,src):
    for i in range(0,len(a)):
        if(a[src][i]==1 and vis[i]==0):
            vis[i]=1
            print(i,end=" ")
            df(a,vis,i)
print("enter number of vertices: ")
n=int(input())
a=[]
for i in range(0,n):
    b=[0]*n
    a.append(b)
print("Enter no of egds  ")
edgs=int(input())
print("Enter edgs with src to dest : ")
for i in range(0,edgs):
    src,des=map(int,input().split(" "))
    a[src][des]=1
    a[des][src]=1
vis=[0]*n
print("enter source :")
src=int(input())
print(src,end=" ")
vis[src]=1
df(a,vis,src)
