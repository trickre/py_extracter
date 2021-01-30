lines = []
dat1 = []
dat2 = []
dat3 = []
dat4 = []
dat5 = []
dat6 = []
dat7 = []
dat8 = []
dat9 = []

with open("sample_data.csv") as f:
  lines = f.readlines()

cnt = 0
cnt0 = -1
for l in lines[1:]:
  data = l.split(",")
  cnt = int(data[0])
  if((cnt-cnt0) == 1):
    dat1.append(float(data[1]))
    dat2.append(float(data[2]))
    dat3.append(float(data[3]))
    dat4.append(float(data[4]))
    dat5.append(float(data[5]))
    dat6.append(float(data[6]))
    dat7.append(float(data[7]))
    dat8.append(float(data[8]))
    dat9.append(float(data[9]))
    cnt0 += 1
  else:
    for i in range((cnt-cnt0)):
      dat1.append(float(0))
      dat2.append(float(0))
      dat3.append(float(0))
      dat4.append(float(0))
      dat5.append(float(0))
      dat6.append(float(0))
      dat7.append(float(0))
      dat8.append(float(0))
      dat9.append(float(0))
      cnt0 += 1

with open("dat1.txt",'w') as f:
  for l in dat1:
    f.write(str(l)+"\n")
with open("dat2.txt",'w') as f:
  for l in dat2:
    f.write(str(l)+"\n")
with open("dat3.txt",'w') as f:
  for l in dat3:
    f.write(str(l)+"\n")
with open("dat4.txt",'w') as f:
  for l in dat4:
    f.write(str(l)+"\n")
with open("dat5.txt",'w') as f:
  for l in dat5:
    f.write(str(l)+"\n")
with open("dat6.txt",'w') as f:
  for l in dat6:
    f.write(str(l)+"\n")
with open("dat7.txt",'w') as f:
  for l in dat7:
    f.write(str(l)+"\n")
with open("dat8.txt",'w') as f:
  for l in dat8:
    f.write(str(l)+"\n")
with open("dat9.txt",'w') as f:
  for l in dat9:
    f.write(str(l)+"\n")
