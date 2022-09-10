import sys


def dalek(sent):
    if len(__) >= 5:
        if __[:5] == 'далек':
            return True
        return False
    return False


count = 0
text = list(map(str.rstrip, sys.stdin.readlines()))
for _ in text:
    for __ in list(map(lambda x: x.lstrip(), _.lower().split(' '))):
        if dalek(__):
            count += 1
            break

print(count)
