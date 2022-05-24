""" Problem:
숫자정사각형출력하기-1
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
def solution():
    numTestCases = int(input())
    for j in range(numTestCases):
      number = int(input())
      mid = number //2
      if number % 4 == 1:
         mid_num = ("01" * mid) + "0"
         for i in range(number):
            if i == mid:
               print(mid_num)
            else:
               dif = abs(mid-i)
               line = mid_num[0:mid-(dif-1)] + str(dif%2)*(2*dif-1) + mid_num[mid+dif:number]
               print(line)
      elif number % 4 == 3:
         mid_num = ("10" * mid) + "1"
         for i in range(number):
            if i == mid:
               print(mid_num)
            else:
               dif = abs(mid-i)
               line = mid_num[0:mid-(dif-1)] + str(dif%2)*(2*dif-1) + mid_num[mid+dif:number]
               print(line)


if __name__ == "__main__":
   solution()

