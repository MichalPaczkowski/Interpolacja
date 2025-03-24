import numpy as np
import random
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
# Read file and save in memory in list.
getcontext().prec = 50
with open("data.txt", 'r') as file:
    lines = file.readlines()
    data = []
    for line in lines:
        line = line.strip().split(';')
        line = [float(i) for i in line]
        data.append(line)

x = []
dlugosc_pliku = len(data)

for i in data:
    x.append(i[0])

ilorazy = [[Decimal(0)]*(dlugosc_pliku - i) for i in range(dlugosc_pliku)] # init triangular tab

for i in range(dlugosc_pliku):
    ilorazy[0][i] = data[i][1] #fill up first column with y values

for i in range(1,dlugosc_pliku): # Newton's quotients maker
    for j in range(0, dlugosc_pliku - i):
        ilorazy[i][j] = (Decimal(ilorazy[i-1][j+1]-ilorazy[i-1][j]) / Decimal(x[j+i]-x[j]))



new_xis = np.arange(x[0], x[-1], 0.05)

# for i in range(dlugosc_pliku):
#     for j in range(i+1)
new_data = []
def calcXis(tabX, ilorazy, new_data,x):
    for el in tabX:
        result = Decimal(ilorazy[0][0])
        for i in range(1, int(el)+2):
            iloraz = Decimal(1)
            for j in range(i):
                iloraz = iloraz * Decimal((el-x[j]))
            iloraz *= ilorazy[i][0]
            result += iloraz
        new_data.append([el, result])

calcXis(new_xis[1:], ilorazy, new_data,x)

print(f"Old data: {data}")
print(f"New data: after interpolation {new_data}")
def generate_data(rows_number, max_value): #function to generate indicated amount of rows and random value for each row
    with open("data.txt", "w") as data:
        for i in range(rows_number):
            data.write(str(i)+';'+str(random.randint(0,max_value))+'\n')
# generate_data(30, 40)

print("Ilorazy: ", ilorazy)
new_data.sort(key=lambda x: x[0])
# xis and yis for new_data
x = [r[0] for r in data]
y = [r[1] for r in data]

# xis and yis for old data before new x
new_data = new_data[:]
xo = [r[0] for r in new_data]
yo = [r[1] for r in new_data]
plt.figure(1)
plt.plot(x,y, marker='o', linestyle='-', color='b', label="Wykres przed")
plt.show(block=False)

plt.figure(2)
plt.plot(xo,yo, marker='o', linestyle='-', color='r', label="Wykres po")
plt.show(block=False)
plt.show()