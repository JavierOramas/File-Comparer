import os

f = open("source.muh")

flag = True
for i in enumerate(f):
    if flag:
        source = i
        flag = False
    else:
        destination = i
source = source[1][0:-1]
destination = destination[1][:]
line = "diff -rq "+source+" "+destination+" > result.muh"
os.system(line)

r = open("result.muh")

for i in enumerate(r):
    index = i[1].find(destination)
    if index == -1:
        index = i[1].find(source)
    temp = i[1][index:]
    j = 0
    while temp[j] != ':':
        j-= 1
    
    file = temp[j+1:]
    temp = temp[:j]
    if temp.find(source) != -1:
        line = "cp "+temp+"/"+file[1:-1]+" "+destination+temp[len(source):]
        os.system(line)
    if temp.find(destination) != -1:
        line = "cp "+temp+"/"+file[1:-1]+" "+source+temp[len(destination):]
        os.system(line)

