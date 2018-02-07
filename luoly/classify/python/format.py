# formatting data


file = open('log1')
datas = file.readlines()
file_new = open('newlog', 'w')
count = 1
for i in range(len(datas)):
    data = datas[i].strip('\n').split(', ')
    if i % 3 == 0:
        if i != 0:
            file_new.write('\n')
        file_new.write('-1 ')
        count = 1
    for j in range(len(data)):
        file_new.write(str(count))
        file_new.write(':')
        file_new.write(str(data[j]))
        count += 1
        file_new.write(' ')
file.close()
file_new.close()