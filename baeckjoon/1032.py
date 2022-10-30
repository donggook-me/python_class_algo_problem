def solution():
    numTestCases = int(input())
    testList = []
    for v in range(numTestCases):
       target = input()
       testList.append(target)
       
    tmp_len = len(testList[0])
    tmp = "?" * tmp_len
    for i in range(tmp_len):
        char = testList[0][i]
        cnt = 0
        for case in testList:
            if case[i] == char:
                cnt +=1
        if cnt == numTestCases:
            token_list = list(tmp)
            token_list[i] = char
            tmp = ''.join(token_list)
    return tmp
                
                
        

if __name__ == "__main__":
   print(solution())
   