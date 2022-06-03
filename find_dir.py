""" Problem:
anaconda3 파일 및 .py의 개수 구하기
국민대학교 소프트웨어융합대학 소프트웨어학부 2학년 20192282 이동국 """
import os
import queue
def get_subdir(path):
    try:
        dirfiles = os.listdir(path)
    except PermissionError:
        return
    
    subdir_list = []
    for each in dirfiles:
        full_name = path + '/' + each
        if each[-3:] == ".py":
            py_list.append(full_name)
        if os.path.isdir(full_name):
            subdir_list.append(full_name)

    return subdir_list


# print(get_subdir("/Users/dongguk/opt/anaconda3"))


dir_queue = queue.Queue() 
dir_queue.put("/Users/dongguk/opt/anaconda3")
all_dirs = []
py_list = []
f = open("./output.txt", 'w')
while not dir_queue.empty():
    dir_name = dir_queue.get()
    all_dirs.append(dir_name)

    subdir_names = get_subdir(dir_name)
    for each in subdir_names:
        dir_queue.put(each)
f.write(', '.join(py_list))
f.close()
print(len(py_list))
