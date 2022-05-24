""" Problem:
세 정수의 정렬(2) 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for v in range(numTestCases):
      numList = [int(number) for number in input().split()]
      [a,b,c] = numList
      if a <= b:
         if b <= c:
            print(a,b,c)
         else:
            if a <= c:
               print(a,c,b)
            else:
               print(c,a,b)
      else:
         if c <= b:
            print(c,b,a)
         else:
            if a <= c:
               print(b,a,c)
            else:
               print(b,c,a)




if __name__ == "__main__":
   solution()