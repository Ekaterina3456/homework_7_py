# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При
# переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование
# должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего

import os
from os import chdir
from pathlib import Path
from random import randint, choices


def rename_files(path: str | Path, new_name: str, counter: int, new_file_extension: str,
                old_file_extension: str, from_old_name: int = randint(2, 7)):
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    files = os.listdir()
    for name in files:
        if old_file_extension in name:
            num = ''
            for _ in range(counter):
                num += str(randint(0, 9))
            new = f'{new_name}{num}.{new_file_extension}'
            old = name[:from_old_name]
            os.rename(name, f'{old}{new}')


if __name__ == '__main__':
    new_file_name = input('введите новое имя файла ')
    counter_1 = randint(2,5)
    list_extensions = ['bin', 'txt', 'jpg', 'mp3']
    extension = choices(list_extensions)
    extension_2 = choices(list_extensions)
    rename_files(r'C:\Users\Роман\Desktop\айти\погружение в python\homework_7\pythonProject\dir_1', new_file_name,
                 counter_1, *extension, *extension_2)
