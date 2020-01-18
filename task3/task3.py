import sys
import os

cash1 = open(os.path.join(sys.argv[1], 'Cash1.txt'), 'r')
cash2 = open(os.path.join(sys.argv[1], 'Cash2.txt'), 'r')
cash3 = open(os.path.join(sys.argv[1], 'Cash3.txt'), 'r')
cash4 = open(os.path.join(sys.argv[1], 'Cash4.txt'), 'r')
cash5 = open(os.path.join(sys.argv[1], 'Cash5.txt'), 'r')
cash = [cash1, cash2, cash3, cash4, cash5]

m = -1
i = -1
for _ in range(1, 17):
    s = 0
    for f in cash:
        s += float(f.readline())
    if s > m:
        m = s
        i = _
print(i, end='\n')

for f in cash:
    f.close()


