#!/usr/bin/python3

import os, time, sys

year = sys.argv[1]

files_list = []
dirs_list = []

path = "/home/camilo/workspace/superdigital/python_scanfiles/" + year

for (root, dirs, files) in os.walk(path, topdown=False):
   for name in files:
      dirs = os.path.join(root)
      if len(os.listdir(dirs)) > 1:
         dirs_list.append(os.path.join(root))

dirs_list_unique = (set(dirs_list))

for root in sorted(dirs_list_unique):
    for b in os.listdir(root):
       if os.path.isfile(os.path.join(root, b)) and b.endswith(".txt"):
          files_list.append(os.path.join(root, b))
       else:
          continue

    files_list = sorted(files_list, key=os.path.getmtime)

    del files_list[-1]

    for files2del in files_list:
        os.remove(files2del)
    files_list.clear()