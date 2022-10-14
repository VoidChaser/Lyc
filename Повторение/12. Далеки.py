import sys

count = 0
text = list(map(str.rstrip, sys.stdin.readlines()))
for _ in text:
    if 'далек' in _.lower():
        count += 1
print(count)
