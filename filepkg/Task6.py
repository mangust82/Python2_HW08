# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import csv
import pickle

def pkl_to_csv(pkl_file: str, csv_file: str) -> None:
    with open(pkl_file, 'rb') as f_p:
        data =  pickle.load(f_p)
    # return data
    fieldname = []
    for key in data[0].keys():
        fieldname.append(key)
    print(fieldname)
    with open(csv_file, 'w', encoding='UTF-8', newline='') as f_c:
        csv_write = csv.DictWriter(f_c, fieldnames=fieldname)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    print(pkl_to_csv('out.pickle', 'pkl_to_csv.csv'))