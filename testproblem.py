"""
Problem:
    주가 분석 (1)
"""
def solution():
    numData = int(input())
    for i in range(numData):
        numbers = list(map(int, input().split(" ")))
        lst = []
        min = numbers[0]

        for j in range(1, len(numbers)):
            if j <= len(numbers) - 2:
                if min <= numbers[j] and numbers[j] > numbers[j+1]:
                    min = numbers[j]
                    lst.append(min)
                else:
                    min = numbers[j]

        print(lst)
        print(len(lst))

if __name__ == "__main__":
    solution()