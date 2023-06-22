#Напишите программу для поиска всех файлов с заданным расширением в заданной
# директории и всех ее поддиректориях. Если директория не найдена, программа должна
# вызывать исключение.

import os

newDir = "my_folder"
newExt = ".txt"

def find_files(locDir, locExt):
    if not os.path.isdir(locDir):
        raise ValueError("Директории не найдено")

    files_dirs = os.listdir(locDir)

    for file_dir in files_dirs:
        full_path = os.path.join(locDir, file_dir)

        if os.path.isdir(full_path):
            find_files(full_path, locExt)
        else:
            if full_path.endswith(locExt):
                print(full_path)

find_files(newDir, newExt)