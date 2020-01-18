import sys

f = open(sys.argv[1], 'r')

tv = []
for line in f:
    tv.append(line.split())
tv.sort()
tv1 = []
for x in range(1, len(tv)):
    tv1.append([tv[x - 1][0], tv[x][0], 0])
tv1.append(tv[-1] + [0])
max = 0
for person in tv:
    for interval in tv1:
        if ((person[0] >= interval[0]) and (person[0] < interval[1])) or (
                (person[1] > interval[0]) and (person[1] <= interval[1])) or (
                (person[0] < interval[0] < interval[1]) and (person[1] > interval[1] > interval[0])):
            interval[2] += 1
        if interval[2] > max:
            max = interval[2]
for x in tv1:
    if x[2] < max:
        tv1.remove(x)
for x in range(1, len(tv1)):
    if tv1[x][0] == tv1[x - 1][1]:
        tv1[x][0] = tv1[x - 1][0]
        tv1[x - 1][2] = 0
for x in tv1:
    if x[2] != 0:
        print(x[0], x[1], end='\n')

