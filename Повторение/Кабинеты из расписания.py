import sys

days_info = ' '.join(list(map(str.rstrip, sys.stdin.readlines())))
days_info = days_info.split('  ')

cabinets = {}

for _ in days_info:
    time_table = _.split(' ')[1:]
    buff_str = ''
    for __ in time_table:
        if not __.isdigit():
            buff_str += __ + ' '
        else:
            key, val = int(__), ' '.join(buff_str.rstrip().split(' '))
            if key not in cabinets.keys():
                cabinets[key] = [' '.join(buff_str.rstrip().split(' '))]
            else:
                cabinets[key].append(' '.join(buff_str.rstrip().split(' ')))

                cabinets[key] = list(dict.fromkeys(cabinets[key]).keys())
            buff_str = ''

for key, value in cabinets.items():
    cabinets[key] = ', '.join(value)

for key in sorted(list(cabinets.keys())):
    print(f"{key}: {cabinets[key]}")
    