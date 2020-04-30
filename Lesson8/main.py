from core import create_file, create_folder, delete_file, copy_file, get_list, save_log, change_folder
import sys
import os

try:
    command = sys.argv[1]
except IndexError:
    print("Command required")
    command = "help"

if command == "list":
    get_list()
elif  command == "create_file":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command require file name parameter")
    else:
        create_file(name)
elif command == "create_folder":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command require folder name parameter")
    else:
        create_folder(name)
elif command == "delete":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command require file/folder name parameter")
    else:
        delete_file(name)
elif command == "copy":
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_file(name, new_name)
    except IndexError:
        print("command require file/folder name parameter")
elif command == "change_folder":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command require folder name parameter")
    else:
        change_folder(name)
    print(os.path)
elif command == "help":
    print("list - list content of folder")
    print("create_file - create file")
    print("create_folder - create folder")
    print("delete - delete file or folder")
    print("copy - copy file or folder")
    print("change - change current folder")
    print("help - display help")
