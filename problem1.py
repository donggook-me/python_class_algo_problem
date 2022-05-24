""" Problem:
   정사각형 출력
   국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 
"""
import sys
def solution():
   numTestCases = int(input())
   for i in range(numTestCases):
      number = int(input())
      for i in range(number):
         if i == 0 or i == (number-1):
            line = ["-"]*number
            line[0] = "+"
            line[-1] = "+"
            line[number//2] = "+"
         elif i == (number//2):
            line = ["-"]*number
            line[0] = "+"
            line[-1] = "+"
            line[number//2] = "*"
         elif i < (number//2):
            line = ["."]*number
            line[0] = "|"
            line[-1] = "|"
            line[number//2] = "|"
            line[i] = "\\"
            line[-(i+1)] = "/"
         elif i > (number//2):
            line = ["."]*number
            line[0] = "|"
            line[-1] = "|"
            line[number//2] = "|"
            line[(number-1)-i] = "/"
            line[-((number-1)-i+1)] = "\\"
         print("".join(line))






if __name__ == "__main__":
   solution()