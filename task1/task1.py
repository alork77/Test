import sys


f = open(sys.argv[1], "r")  # открыли файл

values = [0, 0, -32768, 32768, 0]
data = []
for x in f:
    x = float(x.rstrip())
    data.append(x)
data.sort()
i = len(data)

for x in data:
    values[4] += x  # сумирование для подсчета среднего
values[4] = values[4] / i  # подсчет среднего
values[2] = data[-1]  # максимальное значение
values[3] = data[0]  # минимальное значение
values[0] = data[int(round(len(data)*0.9))-1]  # 90 перцентиль
if i % 2 == 0:  # медиана
    values[1] = 0.5*(data[i//2]+data[i//2-1])
else:
    values[1] = data[i//2]


for x in values:  # вывод значений
    print('%.2f' % x,end='\n')

f.close()  # закрыли файл

