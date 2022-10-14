n_boxes = {}
taken_boxes = []
need_boxes = []


def get_name_num(arg: str):
    name = ''
    num = ''
    for _ in arg:
        if not _.isdigit():
            name += _
        else:
            num += _
    if name and num:
        return name, int(num)
    return name, 0


def entering_boxes_from_takens(takens):
    boxes = {}
    for _ in takens:
        nick = _.split('@')[0]
        nick, nick_num = get_name_num(nick)
        # print(nick, nick_num)
        if nick_num not in boxes.keys():
            boxes[nick] = nick_num
        else:
            if boxes[nick] < nick_num:
                boxes[nick] = nick_num
    return boxes


n = int(input())
for _ in range(n):
    taken_boxes.append(input())

m = int(input())
for __ in range(m):
    need_boxes.append(input())

n_boxes = entering_boxes_from_takens(taken_boxes)


for __ in need_boxes:
    new_nick = __
    if new_nick not in n_boxes.keys():
        n_boxes[new_nick] = 0
        print(f"{new_nick}@untitled.py")
    else:
        n_boxes[new_nick] += 1
        print(f"{new_nick}{n_boxes[new_nick]}@untitled.py")
