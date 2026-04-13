# python file dtetection

import os

file_path = "/Users/keshav/Desktop/python/Lecture46"

if os.path.exists(file_path):
    print(f"The Location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory")

else:
    print("That Location doesn't exists")
