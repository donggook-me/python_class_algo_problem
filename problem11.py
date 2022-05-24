""" Problem:
두 구간(interval)이 차지하는 길이 구하기 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
import sys
def solution():
   numTestCases = int(input())
   for i in range(numTestCases):
      numList = [int(number) for number in sys.stdin.readline().split()]
      [a,b,c,d] = numList

      first_range = set(range(a,b+1))
      second_range = set(range(c,d+1))

      wrapped_range = first_range & second_range
      sum_range = first_range | second_range
      # 6789 // 2345 일 경우 -> 중복된거 없어서 len(wrapped_range) == 0 나옴
      if len(wrapped_range) > 0:
         wrapped_len = len(wrapped_range)-1
         sum_len = len(sum_range)-1

      else: 
         len(wrapped_range) == 0
         wrapped_len = 0
         sum_len = len(sum_range)-2

      # 합해서 2345 6789 len = 8 - 1 = 7이 나오는데, 원래 기준으로는 하나의 구간마다 -1을 빼줘야 함(한번 더 )

      print(wrapped_len, sum_len)




if __name__ == "__main__":
   solution()