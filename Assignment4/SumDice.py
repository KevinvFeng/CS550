count = 0 #total number of solutions
dic = dict() #key: 2 to 8, value: number of key appearances

#dice 1
for i in range(1,5):

    #dice2
    for j in range(1,5):
        s = i+j
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
        count+=1

for key,value in dic.items():
    print(key,": ",value/count)