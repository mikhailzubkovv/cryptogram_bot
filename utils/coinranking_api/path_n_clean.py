import os
import pathlib


def path_to_temp(add_path: str = '/utils/tmp/') -> str:
    """
    Func to create an absolute path to TMP folder

    :param add_path: relative path to TMP folder
    :return: absolute path for user to TMP folder
    """
    current_path: list = str(pathlib.Path.cwd()).split('/')
    index_main_catalog_path = current_path.index('python_basic_diploma')
    main_catalog_path = '/'.join(current_path[0:index_main_catalog_path + 1])
    return main_catalog_path + add_path


def clean_tmp(path: str = path_to_temp()) -> None:
    """
    Func to clean all PNG files from TMP folder

    :param path: path to TMP folder
    :return: None
    """
    for path, dirs, files in os.walk(path):
        for file in files:
            if '.png' in file:
                os.remove(path + file)


if __name__ == '__main__':
    print(path_to_temp())
    clean_tmp()
