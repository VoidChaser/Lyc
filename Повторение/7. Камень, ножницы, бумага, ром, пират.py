addictions = {
    'ножницы': ('бумага', 'ром'),
    'бумага': ('пират', 'камень'),
    'камень': ('ром', 'ножницы'),
    'ром': ('пират', 'бумага'),
    'пират': ('ножницы', 'камень')
}


def get_choice(f, s):
    if f == s:
        return 'ничья'
    elif s in addictions[f]:
        return 'первый'
    elif f in addictions[s]:
        return 'второй'


first, second = input(), input()
print(get_choice(first, second))