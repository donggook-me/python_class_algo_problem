""" Problem:
   자리수 거듭제곱수
   국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 
"""
import sys

def solution():
   numTestCases = int(input())
   for i in range(numTestCases):
      total_num = 0
      number = input()
      for i in range(len(number)):
         total_num += int(number[-(i+1)]) ** len(number)
      if total_num == int(number):
         print(1)
      else: print(0)

      




if __name__ == "__main__":
   solution()