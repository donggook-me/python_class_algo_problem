""" Problem:
시침과 분침 사이각 구하기
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """

def solution():
    numTestCases = int(input())
    for i in range(numTestCases):
      numbers = [float(num) for num in input().split()]
      mnt_dgr = numbers[1] * 6
      hour_dgr = ((30*numbers[0]+numbers[1] * float(0.5)))
      dgr = abs(hour_dgr - mnt_dgr)
      if dgr >= (360-dgr):
         print(int(360-dgr))
      else: print(int(dgr))



if __name__ == "__main__":
   solution()