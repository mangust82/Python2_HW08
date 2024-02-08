# 2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.

import os
from pathlib import Path
import json
import csv
import pickle


def file_tree(path_dir: Path) -> dict[str, str]:
    """Функция рекурсивно обходит вложенные директориии и возращает словарь с соотвествующей древовидной структурой"""
    list_file: list[dict[str, int]] = []
    for obj in path_dir.iterdir():
        if obj.is_dir():
            dict_d = file_tree(obj)
            list_file.append(dict_d)
        if obj.is_file():
            size_f = os.path.getsize(obj)
            dict_f = {'file': str(obj).split('\\')[-1], 'size': size_f}
            list_file.append(dict_f)
    dict_d = {'dir': str(path_dir),'size': sum(item.get('size') for item in list_file), 'files': list_file}
    return dict_d


def read_dict(folder_dict: dict[str, str]) -> list[dict[str, str]]:
    """Функция рекурсивно обходит вложенный древовидный словарь повторяющий дерево каталогов
       и возвращает плоский список словарей для записи в csv.
    """
    dict_list = []
    dict_f = {}
    for key, value in folder_dict.items():
        if key == 'files':
            for item in value:
                [dict_list.append(item) for item in read_dict(item)]
        else:
            if key == 'dir' or key == 'file':
                dict_f.update({'type': key, 'name': value})
            elif key == 'size':
                dict_f.update({key: value})
    dict_list.append(dict_f)
    return dict_list

def dict_convert(path_dir: Path, out_file: str = 'folders') -> None:
    """
    Функция производит сериализацию и запись в json, pickle и csv
    :param path_dir:
    :param out_file:
    :return:
    """
    tree_folders = file_tree(path_dir)
    file_list = read_dict(tree_folders)
    with open(out_file + '.json', 'w', encoding='UTF-8') as f_j:
        json.dump(tree_folders, f_j, indent=4, ensure_ascii=False)
    with open(out_file + '.pickle', 'wb') as f_p:
        pickle.dump(tree_folders, f_p)
    with open(out_file + '.csv', 'w', newline='', encoding='UTF-8') as f_c:
        csv_write = csv.DictWriter(f_c, fieldnames=['type','name','size'])
        csv_write.writeheader()
        csv_write.writerows(file_list[::-1])


dict_convert(Path(r"d:\my doc\Обучение\Бизнесс аналитик\20_погружение в Python\Lesson8\HW08"))
# print(file_tree(Path(r"d:\Distrib\Adobe Acrobat X Professional 10.0.0.396 ML RUS" )))
# str(path_dir).split('\\')[-1]
# print(read_dict(file_tree(Path(r"d:\Distrib\Adobe Acrobat X Professional 10.0.0.396 ML RUS" ))))