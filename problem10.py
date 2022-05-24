""" Problem:
두 사각형 면적 및 둘레 구하기 
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
   numTestCases = int(input())
   for v in range(numTestCases):
      numbers_first = [int(number) for number in input().split()]
      numbers_sec = [int(number) for number in input().split()]

      [x1,y1,x2,y2] = numbers_first
      [x3,y3,x4,y4] = numbers_sec

      first_x = set(range(x1,x2+1))
      first_y = set(range(y1,y2+1))
      # 한쪽 사각형의 내부에 있는 점들의 좌표
      sec_x = set(range(x3,x4+1))
      sec_y = set(range(y3,y4+1))
      # 나머지 사각형의 테두리 + 내부 점들 좌표
      shared_x = first_x & sec_x
      shared_y = first_y & sec_y
      
      first_width = (x2-x1) * (y2-y1)
      second_width = (x4-x3) * (y4-y3)

      first_border = ((x2-x1) + (y2-y1)) * 2
      second_border = ((x4-x3) + (y4-y3)) * 2

      if len(shared_x) > 1 and len(shared_y) >1 :
         if (shared_x == first_x and shared_y== first_y):
            width = second_width
            border = second_border
            print(width, border)
         
         elif (shared_x == sec_x and shared_y == sec_y):
            width = first_width
            border = first_border
            print(width, border)
         
         else:
            # 일부만 겹치는 케이스 -> shared_x 로 겹치는 구간의 너비, 길이 구하기
            shared_shape_x = max(shared_x)- min(shared_x)
            shared_shape_y = max(shared_y)- min(shared_y)
            shared_width = shared_shape_x * shared_shape_y
            shared_border = 2*(shared_shape_x + shared_shape_y)
            width = first_width + second_width - shared_width
            border = first_border + second_border - shared_border
            print(width, border)

            
      else:
         width = first_width + second_width
         border = first_border + second_border
         print(width, border)
            



      




if __name__ == "__main__":
   solution()