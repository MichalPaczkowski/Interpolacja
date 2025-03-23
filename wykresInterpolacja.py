
import random
import matplotlib.pyplot as plt
# Read file and save in memory in list.
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


ilorazy = [[0]*(dlugosc_pliku - i) for i in range(dlugosc_pliku)]

for i in range(dlugosc_pliku):
    ilorazy[0][i] = data[i][1]

for i in range(1,dlugosc_pliku): # Newton's quotients maker
    for j in range(0, dlugosc_pliku - i):
        ilorazy[i][j] = (ilorazy[i-1][j+1]-ilorazy[i-1][j]) / (x[j+i]-x[j])

result = 0 #final result init
new_x = 5.5  # Here you give value of x which value you want to know
iloraz = 1

# for i in range(dlugosc_pliku):
#     for j in range(i+1)

for i in range(1, int(new_x)):
    iloraz = 1
    for j in range(i):
        iloraz = iloraz * (new_x-x[j])
    iloraz = iloraz * ilorazy[i][0]
    result = result + iloraz
result += ilorazy[0][0]
print("List of quotients: ", ilorazy)
print(f"Final result for x = {new_x}\n", result)

def generate_data(rows_number, max_value): #function to generate indicated amount of rows and random value for each row
    with open("data.txt", "w") as data:
        for i in range(rows_number):
            data.write(str(i)+';'+str(random.randint(0,max_value))+'\n')
# generate_data(200, 1000)

print("----------------------------------")
idx= 0 #temp idx for add in the right place our [new_x from interpolation, result]
print("data before insert: ", data)
new_data = data.copy()
for i in data:
    if new_x < float(i[0]):
        new_data.insert(idx, [new_x, result])
        break
    idx = idx + 1
print("data after insert: ", new_data)

# xis and yis for new_data
x = [r[0] for r in new_data]
y = [r[1] for r in new_data]

# xis and yis for old data before new x
xo = [r[0] for r in data]
yo = [r[1] for r in data]
plt.figure(1)
plt.plot(x,y, marker='o', linestyle='-', color='b', label="Wykres")
plt.show(block=False)

plt.figure(2)
plt.plot(xo,yo, marker='o', linestyle='-', color='b', label="Wykres")
plt.show(block=False)
plt.show()