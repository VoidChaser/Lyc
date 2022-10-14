import sys

dalekis = ['далек', 'далеки', 'далека', 'далеков', 'далеку', 'далекам', 'далека', 'далеков', 'далеком', 'далеками',
           'далеке', 'далеках']
dale_dic = {}
for _ in dalekis:
    dale_dic[_] = len(_)


def dalek(sent):
    for k, v in dale_dic.items():
        if len(sent) == v:
            if sent == k:
                return True
    return False


count = 0
text = list(map(str.rstrip, sys.stdin.readlines()))
for _ in text:
    for __ in list(map(lambda x: x.lstrip(), _.lower().split(' '))):
        if dalek(__):
            count += 1
            break

print(count)
