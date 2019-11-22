#!/usr/bin/python3

import os, time, glob, json, itertools, filecmp

files_list = []
files_remove = []
#dirs_list = []

files_dict = {}

path = "/home/camilo/workspace/superdigital/clear_images/2019"

for (root, dirs, files) in os.walk(path, topdown=False):

   for name in files:
      dirs = os.path.join(root)
      if len(os.listdir(dirs)) > 1:
         #print(abc + " " + str(len(os.listdir(abc))))
         files_list.append(os.path.join(root, name))


for a in sorted(files_list):
   #print(a + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(a))))
   files_dict[a] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(a)))

#print("\n",json.dumps(files_dict))


for f1, f2 in itertools.combinations(files_list, 2):
    if filecmp.cmp(f1, f2):
        print(f1, f2)