# Python:   2.7.13
#
# Author:   Nash N. Wood
#
#Purpose:   The Tech Acadmey - Python Course, Item 64
#           Daily File Transfer scripting project
#           An exercise to transfer text files added or edited in the
#           last day to the main office
#=====================================================================           

import os
import shutil
from datetime import *

src = 'C:\Users\Student\Desktop\Source Folder'
dest = 'C:\Users\Student\Desktop\Receiving Folder'

currentTime = datetime.now()
twentyFourHoursAgo = currentTime + timedelta(hours=-24)

files = os.listdir(src)

for f in files:
    src_file = src + '\\' + f
    lastModUnix = os.path.getmtime(src_file)
    lastMod = datetime.fromtimestamp(int(lastModUnix))
    if lastMod >= twentyFourHoursAgo:
        dest_file = dest + '\\' + f
        shutil.copy(src_file, dest_file)
