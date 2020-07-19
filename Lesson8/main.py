from core import create_file, create_folder, delete_file
from core import copy_file, get_list, change_folder, save_log
import game
import sys
import os

save_log("Start")

try:
    command = sys.argv[1]
except IndexError:
    print("Command required")
    command = "help"

if command == "list":
    get_list()
elif command == "create_file":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command requires file name parameter")
    else:
        create_file(name)
elif command == "create_folder":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command requires folder name parameter")
    else:
        create_folder(name)
elif command == "delete":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command requires file/folder name parameter")
    else:
        delete_file(name)
elif command == "copy":
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print("command requires file/folder name and newname parameters")
    else:
        copy_file(name, new_name)
elif command == "change_folder":
    try:
        name = sys.argv[2]
    except IndexError:
        print("command require folder name parameter")
    else:
        change_folder(name)
    print(os.path)
elif command == "game":
    game.guess_reverse()
elif command == "help":
    print("list - list content of folder")
    print("create_file - create file")
    print("create_folder - create folder")
    print("delete - delete file or folder")
    print("copy - copy file or folder")
    print("change - change current folder")
    print("help - display help")

save_log("End")
