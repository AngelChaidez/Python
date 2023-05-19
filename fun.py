# a script that shows all directoryies in current directory

import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        print(os.path.join(root, name))
    for name in files:
        print(os.path.join(root, name))

