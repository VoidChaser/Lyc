def correct_sum_nums(f, s):
    return sum(list(map(int, list(str(f))))) != sum(list(map(int, list(str(s)))))


h_hours = sorted(list(map(int, input().split(' '))))
h_minutes = sorted(list(map(int, input().split(' '))))

for h in h_hours:
    for m in h_minutes:
        if correct_sum_nums(h, m):
            print(f"{str(h).rjust(2, '0')}:{str(m).rjust(2, '0')}")
