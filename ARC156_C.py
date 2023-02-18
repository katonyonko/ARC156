import io
import sys

_INPUT = """\
6
3
1 2
2 3
4
2 1
2 3
2 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  N=int(input())
  G=[[] for _ in range(N)]
  for _ in range(N-1):
    u,v=map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)
  D=bfs(G,0)
  tmp=sorted([(D[i],i) for i in range(N)])
  if N%2==0: ans=tmp[N//2:]+tmp[:N//2]
  else: ans=tmp[N//2+1:]+[tmp[N//2]]+tmp[:N//2]
  print(*[ans[i][1]+1 for i in range(N)])