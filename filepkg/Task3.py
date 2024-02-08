# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

__all__ = ['json_to_csv']


import csv
import json


def json_to_csv(json_file: str, csv_file: str) -> None:
    with open(json_file, 'r', encoding='Utf-8') as f_j,\
         open(csv_file, 'w', newline='', encoding='UTF-8') as f_c:
        my_dict: dict = json.load(f_j)
        print(len(my_dict))
        dict_list = []
        for level, user in my_dict.items():
            for id, name in user.items():
                dict_list.append({'level': level, 'id': id, 'name':name})
        print(dict_list)
        csv_write = csv.DictWriter(f_c, fieldnames=['level','id','name'])
        print(csv_write)
        csv_write.writeheader()
        csv_write.writerows(dict_list)


if __name__ == '__main__':
    json_to_csv('user_log.json', 'out.csv')
