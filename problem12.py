""" Problem:
주가 분석 (1) 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for i in range(numTestCases):
      ans_list = []
      mark = False
      numList = [int(number) for number in input().split() ]
      for j in range(1,len(numList)-1):
         if numList[j] > numList[j-1]:
            if numList[j] > numList[j+1]:
               ans_list.append(numList[j])
            elif numList[j] == numList[j+1]:
               mark = True
         if mark:
            if numList[j] == numList[j+1]:
               continue
            elif numList[j] > numList[j+1]:
               ans_list.append(numList[j])
               mark = False
            else:
               mark = False
      print(len(ans_list))

    




if __name__ == "__main__":
   solution()