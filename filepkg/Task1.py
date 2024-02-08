# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

__all__ = ['json_convert']

import json


def json_convert(src_file: str, out_file: str):
    with open(src_file, 'r', encoding='UTF-8') as f,\
         open(out_file, 'w', encoding='UTF-8' ) as f2:
        my_dict = {}
        for line in f:
            dict_txt = {line.split()[0].capitalize(): line.split()[1]}
            my_dict.update(dict_txt)
        json.dumps(my_dict)
        f2.write(json.dumps(my_dict, indent=3, ensure_ascii=False))


if __name__ == '__main__':
    print(json_convert('results.txt', 'out.txt'))



# dict_compr = {a[i]:ord(a[i]) for i in range(len(a))}

#     x = {chr(int(my_list[0])): my_list[0], chr(int(my_list[1])): my_list[1]}
#     dict_uni.update(x)
# result = {chr(num): num for num in range(min(nums), max(nums) + 1)}




















# import json
# a = 'Hello world!'
# b = {key: value for key, value in enumerate(a)}
# c = json.dumps(b, indent=3, separators=('; ', '= '))
# print(c)