"""
There are core functions for file manager
"""

import os
import shutil
import datetime

def create_file(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Folder already exists")


def get_list(is_folder = False):
    result = os.listdir()
    if is_folder:
        result = [item for item in result if os.path.isdir(item)]
    print(result)


def copy_file(name, new_name):
    try:
        shutil.copy(name, new_name)
    except FileNotFoundError:
        print(f"File or folder {name} not found")



def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print("File or folder isn't exists")


def save_log(message):
    with open("main.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {message}")


def change_folder(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print("Folder isn't exists")

if __name__ == "__main__":
    print(get_list())
    create_file("test.txt")
    create_folder("test_folder")
    print(get_list())
    copy_file("test.txt", "test_new.txt")
    delete_file("test.txt")
    delete_file("test.txt")
    delete_file("test_folder")
    delete_file("test_folder")
    copy_file("test.txt", "test_new.txt")
    save_log("test message")
    get_list()
    change_folder("..")
    get_list()
