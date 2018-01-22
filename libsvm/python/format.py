# formatting data
import sys

log_name = sys.argv[1]
new_log_name = sys.argv[2]

file = open(log_name)
datas = file.readlines()
file_new = open(new_log_name, 'w')
count = 1
for i in range(len(datas)):
    t_data = datas[i]
    t_data = t_data.strip()
    t_data = t_data.replace('[', '')
    t_data = t_data.replace(']', '')
    t_ds = t_data.split(", ")
    count = 1
    file_new.write('1 ')
    for j in range(len(t_ds)):
        file_new.write(str(count))
        file_new.write(':')
        file_new.write(str(t_ds[j]))
        count += 1
        file_new.write(' ')
    file_new.write('\n')
file.close()
file_new.close()