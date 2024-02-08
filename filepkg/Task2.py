# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

__all__ = ['who_a_u']

import json
import os


def who_a_u(f_name: str) -> None:
    while True:
        u_name = input('Введите имя: ')
        u_id = input('Введите идентификатор: ')
        u_level = input('Ваш уровень доступа: ')
        u_dict= {u_id: u_name}
        with open(f_name, 'r+', encoding='UTF-8') as f1:
            if os.path.getsize(f_name) !=0:
                chek_dict: dict = json.load(f1)
                for user in chek_dict.values():
                    flag = False
                    if user.get(u_id) is not None:
                        flag = True
                        break
                if flag:
                    print('Такой id уже существует')
                else:
                    if chek_dict.get(u_level) is not None:
                        chek_dict[u_level].update(u_dict)
                        f1.seek(0)
                        json.dump(chek_dict, f1, indent=2)
                    else:
                        chek_dict.setdefault(u_level, {u_id: u_name})
                        f1.seek(0)
                        json.dump(chek_dict, f1, indent=2)
            else:
                json.dump({u_level:u_dict}, f1, indent=2)

if __name__ == '__main__':
    who_a_u('user_log.json')

#
# import json
# from pathlib import Path
#
#
# def input_user(path: Path) -> None:
#     unique_id = set()
#     if not path.is_file():
#         data = {str(level): {} for level in range(1, 8)}
#     else:
#         with open(path, 'r', encoding='UTF-8') as f_read:
#             data = json.load(f_read)
#         # unique_id = {id for id_name in data.values() for id in id_name.keys()}
#         for id_name in data.values():
#             unique_id.update(id_name.keys())
#
#     while name := input("Введите имя пользователя: "):
#         level = input("Введите уровень доступа от 1 до 7: ")
#         user_id = input("Введите id пользователя: ")
#         if user_id not in unique_id:
#             unique_id.add(user_id)
#             data[level].update({user_id: name})
#             with open(path, 'w', encoding="UTF-8") as f_write:
#                 json.dump(data, f_write, indent=4, ensure_ascii=False)
#         else:
#             print("Такой id пользователя уже существует")
#
#
# if __name__ == '__main__':
#     input_user(Path("users.json"))