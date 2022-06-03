""" Problem:
오셀로(Othello) 게임 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for v in range(numTestCases):

      TestCount = int(input())
      black_list = [[4,5], [5,4]]
      white_list = [[4,4], [5,5]]
      target = [[1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,0],[-1,1],[-1,-1]]

      chk = True
      while(TestCount >0):
         TestCount -= 1

         debug = True
         if [3,4] in white_list:
            debug = True
         elif [3,4] in black_list:
            debug = False

         [x,y] = list(map(int, input().split()))
         if chk: ## 검은돌 놓을때
            black_list.append([x,y])
            for tar2 in target:
               add_list = []
               cnt = 1
               while True:
                  tar_point = [(x+(tar2[0]*cnt)), (y+(tar2[1]*cnt))]
                  if tar_point in white_list:
                     add_list.append(tar_point)
                     cnt += 1
                     continue
                  elif ((tar_point in black_list) and (len(add_list)>0)):
                     for add in add_list:
                        if add in white_list:
                           white_list.remove(add)
                        black_list.append(add)
                     break
                  else:
                     break
            # print(f"white list {white_list} and black list {black_list}")

         else: ## 흰돌 놓을때
            white_list.append([x,y])
            for tar2 in target:
               add_list = []
               cnt = 1

               while True:
                  tar_point = [x+(tar2[0]*cnt), y+(tar2[1]*cnt)]
                  if tar_point in black_list:
                     add_list.append(tar_point)
                     cnt += 1
                     continue
                  elif (tar_point in white_list) and (len(add_list)>0):
                     for add in add_list:
                        if add in black_list:
                           black_list.remove(add)
                        white_list.append(add)
                        
                     break
                  else:
                     break
         chk = not(chk)

      print(len(black_list),len(white_list))
      for first in range(1,9):
         for sec in range(1,9):
            if [first,sec] in white_list:
               print("O", end="")
            elif [first,sec] in black_list:
               print("X", end="")
            else:
               print("+", end="")
         print()


if __name__ == "__main__":
   solution()