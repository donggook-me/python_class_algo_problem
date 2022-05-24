""" Problem:
아마다르 곱 (Hadamard Product)
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for i in range(numTestCases):
      list_a = []
      list_b = []
      [row,column] = [int(number) for number in input().split()]
      for j in range(row):
         numLine = [int(number) for number in input().split()]
         list_a.append(numLine)
      for v in range(row):
         numLine = [int(number) for number in input().split()]
         list_b.append(numLine)
      for rw in range(row):
         mul = []
         for col in range(column):
            result = list_a[rw][col] * list_b[rw][col]
            mul.append(str(result))
         print(" ".join(mul))
if __name__ == "__main__":
   solution()