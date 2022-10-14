import sys

a = '''А: ка	
И: ки	
Р: ши	
Ш: ли
Б: зу	
Й: фу	
С: ари	
Щ: ни
В: ру	
К: ме	
Т: чи	
Ъ: д
Г: джи	
Л: та	
У: мей	
Ы: хе
Д: те	
М: рин	
Ф: лу	
Ь: ксе
Е: ку
Ё: ку
Н: то	
Х: ри	
Э: га
Ж: зу	
О: мо	
Ц: ми	
Ю: до
З: з	
П: но	
Ч: зи	
Я: ма'''.split('\n')


def japan_name(name):
    j_name = ''
    for __ in name:
        j_name += jap_ru_dic[__]
    return j_name


def normalize(name):
    r_name = name[0].capitalize() + ''.join(list(map(lambda x: x.lower(), list(name[1:]))))
    return r_name


jap_ru_dic = {}

a = list(map(lambda z: z.split(': '), list(map(lambda y: y.rstrip(), list(filter(lambda x: x is not None, a))))))
for _ in a:
    key, value = _
    jap_ru_dic[key], jap_ru_dic[key.lower()] = value.capitalize(), value


name = sys.stdin.readline().rstrip()
print(normalize(japan_name(name)))
