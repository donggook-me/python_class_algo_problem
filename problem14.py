""" Problem:
변수 이름 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for v in range(numTestCases):
      case = input()
      ans = 0
      for i in range(len(case)):
         if i == 0 and case[i].isdigit():
            break
         if case[i].isalpha() or case[i].isdigit() or case[i] == "_":
            ans += 1
      if ans == len(case):
         print(1)
      else: print(0)



if __name__ == "__main__":
   solution()