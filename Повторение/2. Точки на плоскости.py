quarters = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}


def get_quarter(point: tuple):
    global quarters
    x, y = point

    if x >= 0 and y >= 0:
        return "I"

    elif x <= 0 <= y:
        return 'II'

    elif x <= 0 and y <= 0:
        return 'III'

    elif x >= 0 and y <= 0:
        return 'IV'


amount = int(input())
points_on_axis = []


for _ in range(amount):
    x, y = list(map(int, input().split(' ')))

    if x == 0 and y == 0:
        points_on_axis.append((x, y))
        continue

    elif x == 0 or y == 0:
        points_on_axis.append((x, y))
        continue

    quarters[get_quarter((x, y))] += 1

for point in points_on_axis:
    print(point)

buffered_points = []
for key, value in quarters.items():
    buffered_points.append(f'{key}: {value}')

formated = ', '.join(buffered_points) + '.'
print(formated)