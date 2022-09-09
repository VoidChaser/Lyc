import sys


def word_chars_analysis(word: str) -> tuple:
    to_return = {}
    word_set = tuple(sorted(list(set(word))))
    for _ in sorted(word):
        if _ not in to_return:
            to_return[_] = 1
        else:
            to_return[_] += 1
    return to_return, word_set


def correct(word_analysis):
    w_dict, w_set = word_analysis
    for w in w_dict.keys():
        if w not in main_word or main_word_dict[w] < w_dict[w]:
            return False
    if not(all(list(filter(lambda x: x in main_word_set, w_set)))):
        return False
    return True


text = list(map(lambda x: x.rstrip(), sys.stdin.readlines()))
main_word, other_words = text[0], text[1:]
correct_count = 0
correct_words = []
main_word_dict, main_word_set = word_chars_analysis(main_word)

for __ in other_words:
    if correct((word_chars_analysis(__))):
        correct_count += 1
        correct_words.append(__)

print(correct_count)
print('\n'.join(correct_words))