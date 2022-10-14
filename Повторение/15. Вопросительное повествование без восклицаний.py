import sys

analysis = {'dot': [], 'exp': [], 'ques': []}


def que(sent):
    if '.' in sent or '!' in sent or '?' in sent:
        return False
    return True


def turn_to(massive, path):
    for sent in massive:
        sent_spl = sent.split(' ')
        for _ in sent_spl:
            cymbs = list(_)
            _ = ''.join(list(filter(lambda x: x.isalpha(), cymbs)))
            if _ not in analysis[path]:
                analysis[path].append(_)


def get_aplitted(text):
    to_ret = []
    current_str = ''
    for __ in text:
        if __ != '.' and __ != '?' and __ != '!':
            current_str += __
        else:
            current_str += __
            to_ret.append(current_str.lstrip())
            current_str = ''
    return to_ret


def main():
    text = list(map(lambda x: x.rstrip(), sys.stdin.readlines()))
    text = ' '.join(text)
    sentences = get_aplitted(text)

    dot = list(map(str.lower, list(filter(lambda x: '.' in x, sentences))))
    exp = list(map(str.lower, list(filter(lambda x: '!' in x, sentences))))
    ques = list(map(str.lower, list(filter(lambda x: '?' in x, sentences))))

    turn_to(dot, 'dot')
    turn_to(exp, 'exp')
    turn_to(ques, 'ques')
    d = set(analysis['dot'])
    e = set(analysis['exp'])
    q = set(analysis['ques'])
    bb = d & q
    cc = bb - e
    return cc


goted = sorted(list(main()))
print(' '.join(goted))
