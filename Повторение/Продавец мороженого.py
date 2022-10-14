prices = {}


def get_name_price(arg: str):
    b_n = ''
    b_p = ''
    arg = arg.split('\t')
    for _ in arg:
        if not _.isdigit():
            b_n += _
        else:
            b_p = _
    return b_n, int(b_p)


n = int(input())
for _ in range(n):
    line = input()
    name, price = get_name_price(line)

    prices[name] = price

razd = input()

summ = 0
orders = []
new_orders = input()
while new_orders != '.':
    if new_orders != '':
        orders.append(new_orders + '  ')
    else:
        if orders[-1] != '\n':
            orders.append('\n')
        else:
            pass
    new_orders = input()

orders = ' '.join(orders)
order_count = 1

for _ in orders.split('\n'):
    if _ != '\n':
        order_price = 0
        for __ in _.split('  '):
            __ = __.lstrip()
            if __ != '':

                name, price = __.split('\t')
                order_price += (prices[name.strip()] * int(price))
            else:
                if order_price:
                    print(f"{order_count}) {order_price}")
                    order_count += 1
                    summ += order_price

print(f"Итого: {summ}")
