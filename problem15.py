""" Problem:
행렬(Matrix) 곱셈
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
import sys
def solution():
   numTestCases = int(input())
   for i in range(numTestCases):
      [r,s,t] = list(map(int, sys.stdin.readline().split()))
      mat1 = []
      for v in range(r):
         mat1.append(list(map(int, sys.stdin.readline().split())))
      mat2 = []
      for j in range(s):
         mat2.append(list(map(int, sys.stdin.readline().split())))
      
      for rr in range(r):
         pt = []
         for tt in range(t):
            ans = 0
            for j in range(s):
               ans += mat1[rr][j] * mat2[j][tt]
            pt.append(str(ans))
         print(" ".join(pt)) 








if __name__ == "__main__":
   solution()