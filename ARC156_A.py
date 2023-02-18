import io
import sys

_INPUT = """\
6
6
3
101
6
101101
5
11111
6
000000
30
111011100110101100101000000111
4
1100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for _ in range(T):
    N=int(input())
    S=input()
    m=S.count('1')
    if (N==3 and S[1]=='1') or m%2==1: print(-1)
    else:
      if m!=2: print(m//2)
      else:
        a=[]
        for i in range(N):
          if S[i]=='1': a.append(i)
        if a[1]-a[0]==1:
          if a[0]>1 or a[1]<N-2: print(2)
          else: print(3)
        else: print(1)