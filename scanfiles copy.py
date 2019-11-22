#!/usr/bin/python3

import os, time, glob

files_list = []
dirs_list = []

path = "/home/camilo/workspace/superdigital/clear_images"

for (root, dirs, files) in os.walk(path, topdown=False):

   for name in files:
      abc = os.path.join(root)
      #directory = os.path.join(root)
      files_list.append(os.path.join(root, name))
      print(abc + " " + str(len(os.listdir(abc))))

   for name in dirs:
      abc = os.path.join(root, name)
      dirs_list.append(os.path.join(root, name))
      #print(abc + " " + str(len(os.listdir(abc))))
      #print(os.path.join(root, name) + " " + str(len(os.listdir(name))))
#      print(os.path.join(root, name))

#print([name for name in os.listdir(dirs_list) if os.path.isfile(name)])

#for a in dirs_list:



#   files = [name for name in os.listdir(a) if os.path.isfile(name)]
#   print(files)
#   if os.path.isfile(a):
#      print(a + " " + str(len(os.listdir(a))))




#for a in files_list:
#   print(a + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(a))))

#for a in sorted(files_list, key=os.path.getmtime):
#   print(a + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(a))))
