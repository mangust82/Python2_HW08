# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import json
import csv

def trans_csv(csv_file: str, json_file: str) -> None:
    with open(csv_file, 'r', encoding='UTF-8', newline='') as f_c:


        # data = f_c.readlines()
        # keys = data[0].split(',')
        # all_date = []
        # for string in data[1:]:
        #     u_dict = {}
        #     list_str = string.split(',')
        #     # list_str[1] = list_str[1] + '0'*(10 - len(list_str[1]))
        #     list_str[1] = f'{int(list_str[1]):010}'
        #     list_str[2] = list_str[2][:-2].title()
        #     u_hash = hash(list_str[0] + list_str[2])
        #     u_dict = {keys[0]:list_str[0],keys[1]:list_str[1],keys[2][:-2]:list_str[2], 'u_hash':u_hash}
        #     all_date.append(u_dict)
        # print(all_date)

        csv_data = csv.reader(f_c)
        all_date = []
        for i, line in enumerate(csv_data):
            u_dict ={}
            if i == 0:
                n_level, n_id, n_name = line
            else:
                level, id, name = line
                u_dict = {
                    n_level: level,
                    n_id: f'{int(id):010}',
                    n_name: name.title(),
                    'u_hash': hash(name+id)
                }
                all_date.append(u_dict)



    with open(json_file, 'w', encoding='UTF-8') as f_j:
        json.dump(all_date, f_j, indent=2, ensure_ascii=False)

trans_csv('out.csv','out.json')

# import json
# from pathlib import Path
#
#
# def input_user(path: Path) -> None:
#     unique_id = set()
#     if not path.is_file():
#         data = {str(level): {} for level in range(1, 8)}
#     else:
#     with open(path, 'r', encoding='UTF-8') as f_read:
#     data = json.load(f_read)
#     # unique_id = {id for id_name in data.values() for id in id_name.keys()}
#     for id_name in data.values():
#     unique_id.update(id_name.keys())
#
#     while name := input("Введите имя пользователя: "):
#     level = input("Введите уровень доступа от 1 до 7: ")
#     user_id = input("Введите id пользователя: ")
#     if user_id not in unique_id:
#     unique_id.add(user_id)
#     data[level].update({user_id: name})
#     with open(path, 'w', encoding="UTF-8") as f_write:
#     json.dump(data, f_write, indent=4, ensure_ascii=False)
#     else:
#     print("Такой id пользователя уже существует")
#
#
# if __name__ == '__main__':
# input_user(Path("users.json"))