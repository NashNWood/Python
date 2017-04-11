# Python:   2.7.13
#
# Author:   Nash N. Wood
#
#Purpose:   The Tech Acadmey - Python Course, Item 63
#           File Transfer
#           An exercise to transfer text files from one folder to another.
#           

import shutil
import os

src = 'C:\Users\Student\Desktop\Folder A'
dest = 'C:\Users\Student\Desktop\Folder B'

files = os.listdir(src)

for f in files:
    src_file = src + '\\' + f
    dest_file = dest + '\\' + f
    shutil.move(src_file,dest_file)
