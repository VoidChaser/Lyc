corners = {'left': (0, 0),
           'right': (0, 0),
           'top': (0, 0),
           'bottom': (0, 0)}


amount = int(input())
points_between = []
all_points = []
NOPOINT = (0, 0)

for _ in range(amount):
    x, y = list(map(int, input().split(' ')))
    if (y < abs(x)) and (y > -(abs(x))):
        points_between.append((x, y))
    all_points.append((x, y))

all_points_max_x = max(list(map(lambda xx: xx[0], all_points)))
all_points_max_y = max(list(map(lambda yy: yy[1], all_points)))
all_points_min_x = min(list(map(lambda xx: xx[0], all_points)))
all_points_min_y = min(list(map(lambda yy: yy[1], all_points)))

true_mx, true_my, true_mix, true_miy = 0, 0, 0, 0

for point in all_points:
    _, __ = point
    if _ == all_points_max_x and true_mx == 0:
        true_mx = _, __

    if _ == all_points_min_x and true_mix == 0:
        true_mix = _, __

    if __ == all_points_max_y and true_my == 0:
        true_my = _, __

    if __ == all_points_min_y and true_miy == 0:
        true_miy = _, __

corners['left'], corners['right'], corners['top'], corners['bottom'] = true_mix, true_mx, true_my, true_miy

for point in points_between:
    print(point)

for key, value in corners.items():
    print(f'{key}: {value}')
