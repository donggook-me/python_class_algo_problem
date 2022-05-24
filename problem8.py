""" Problem:
숫자의 모든 자리수 반복 곱하기 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for j in range(numTestCases):
      number = int(input())
      while(number//10!=0):
         mul = 1
         number = str(number)
         for i in range(len(number)):
            if number[i] == '0':
               continue
            mul *= int(number[i])
         number = mul
      print(number)
if __name__ == "__main__":
   solution()