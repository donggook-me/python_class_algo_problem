""" Problem:
해밍 거리 (Hamming Distance)
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for v in range(numTestCases):
      [numA, numB] = list(map(int, input().split()))
      numA, numB = str(format(numA, 'b')), str(format(numB, 'b'))
      lenA = numA.count('1')
      lenB = numB.count('1')
      cnt = 0
      lenC = max(len(numA), len(numB))
      numA = numA.zfill(lenC)
      numB = numB.zfill(lenC)

      for i in range(lenC):
         if numA[i] != numB[i]:
            cnt += 1
      print(lenA, lenB, cnt)





if __name__ == "__main__":
   solution()