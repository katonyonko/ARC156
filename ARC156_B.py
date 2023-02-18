import io
import sys

_INPUT = """\
6
3 1
0 1 3
2 1
0 0
5 10
3 1 4 1 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  F=[1]
  for i in range(4*10**5):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(4*10**5):
    I.append(I[-1]*(4*10**5-i)%mod)
  I=I[::-1]
  used=[0]*(2*10**5+2)
  for i in range(N): used[A[i]]=1
  path=[]
  now=0
  for i in range(K+1):
    while now<2*10**5+2 and used[now]==1: now+=1
    path.append(now)
    now+=1
  ans=0
  for i in range(K+1):
    if i==0 and path[0]==0: pass
    else: ans+=F[K-i+path[i]-1]*I[K-i]*I[path[i]-1]
    ans%=mod
  print(ans)