def get_remind(name):
    name_index = order.index(name)
    if name_index == 0:
        return order[:name_index + 2]
    elif name_index == len(order) - 1:
        return order[-2:]
    else:
        return order[name_index - 1: name_index + 2]


order = input().split(' -> ')
count = int(input())
for _ in range(count):
    print(' -> '.join(get_remind(input())))
