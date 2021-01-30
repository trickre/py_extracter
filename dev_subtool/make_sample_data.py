import random

lines = []
DATA_LENGTH = 9 #number of data

for idx in range(20):
    l = str(idx) + ","
    for i in range(DATA_LENGTH):
        l += '{:.3f}'.format(random.random()) + ","
    lines.append(l+"\n")

with open("sample_data.txt","w") as f:
    f.writelines(lines)
