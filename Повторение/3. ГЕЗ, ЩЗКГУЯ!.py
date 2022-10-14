current_alphabet = input()
len_o_alphabet = len(current_alphabet)
step = int(input())
crypted_alphabet = ''
uncrypted_alphabet = ''


if step > 0:
    for _ in range(len(current_alphabet)):
        crypted_alphabet += current_alphabet[(_ + step) % len_o_alphabet]
        uncrypted_alphabet += current_alphabet[(len_o_alphabet - step + _) % len_o_alphabet]

elif step < 0:
    for _ in range(len(current_alphabet)):
        crypted_alphabet += current_alphabet[(len_o_alphabet + _ + step) % len_o_alphabet]
        uncrypted_alphabet += current_alphabet[(len_o_alphabet - step + _) % len_o_alphabet][::-1]

else:
    crypted_alphabet = current_alphabet


print(crypted_alphabet)
print(current_alphabet)
print(uncrypted_alphabet)





