import sys

ffi = open(sys.argv[1], 'r')  # открыли файлы
fpo = open(sys.argv[2], 'r')

fig = []
for line in ffi:  # считывание точек фигуры
    x = line.split()
    x = [float(x[0]), float(x[1])]
    fig.append(x)
side = [[fig[0], fig[1]], [fig[1], fig[2]], [fig[2], fig[3]], [fig[0], fig[3]]]


def pos(point):  # определение позиции
    if ontop(point):
        return 0  # на вершине
    if onside(point):
        return 1  # на ребре
    if infig(point):
        return 2  # точка внутри
    return 3  # точка снаружи


def ontop(point):  # проверка расположения на вершинах
    global fig
    for x in fig:
        if x == point:
            return True
    return False


def eq(x, y, point):  # уравнение прямой
    if ((point[0] - x[0]) * (y[1] - x[1])) == ((point[1] - x[1]) * (y[0] - x[0])):
        return 'on'
    if ((point[0] - x[0]) * (y[1] - x[1])) > ((point[1] - x[1]) * (y[0] - x[0])):
        return 'dawn'
    if ((point[0] - x[0]) * (y[1] - x[1])) < ((point[1] - x[1]) * (y[0] - x[0])):
        return 'up'
    return False


def onside(point):  # проверка расположения на стороне
    global side
    for line in side:
        if eq(line[0], line[1], point) == 'on':
            if ((line[0][0] <= point[0] <= line[1][0]) or (line[0][0] >= point[0] >= line[1][0])) and (
                    (line[0][1] <= point[1] <= line[1][1]) or (line[0][1] >= point[1] >= line[1][1])):
                return True
    return False


def infig(point):  # проверка расположения внутри четырехугольника
    global side
    if (eq(side[0][0], side[0][1], point) == 'dawn') and (eq(side[1][0], side[1][1], point) == 'dawn') and (
            eq(side[2][1], side[2][0], point) == 'up') and (eq(side[3][0], side[3][1], point) == 'up'):
        return True
    return False


for line in fpo:  # считали точки
    point = line.split()
    point = [float(point[0]), float(point[1])]
    print(pos(point),end='\n')

ffi.close()  # закрыли файлы
fpo.close()

