""" Problem:
1 차원 라이프(Life) 게임 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
import sys
def solution():
   numTestCases = int(input())
   for v in range(numTestCases):
      [table_len, time] = list(map(int, sys.stdin.readline().split()))
      Bac_list = list(map(int,sys.stdin.readline().split()))
      while(time):
         time -= 1
         new_Bac_list = []
         
         for i in range(table_len):
            chg = 0
            if i == 0:
               neighbor = [Bac_list[1]]
            elif i == (table_len-1):
               neighbor = [Bac_list[i-1]]
            else:
               neighbor = [Bac_list[i-1], Bac_list[i+1]]
            case = sum(neighbor)

            if case < 3:
               correct_val = Bac_list[i]-1
            elif case > 7:
               correct_val = Bac_list[i]-1
            elif case >=  4 and case <= 7:
               correct_val = Bac_list[i]+1
            elif case == 3:
               correct_val = Bac_list[i]

            if correct_val < 0:
               correct_val = 0
            elif correct_val > 9:
               correct_val = 9

            new_Bac_list.append(correct_val)
         Bac_list = new_Bac_list
      Bac_list = list(map(str, Bac_list))
      print(" ".join(Bac_list))

            



if __name__ == "__main__":
   solution()