import os
from sys import stderr


def dup_dirs(src, dst):
    print("mkdir %s" %
          os.path.join(dst), file=stderr)
    try:
        os.mkdir(dst)
    except FileExistsError:
        print("W: %s exists." %
              os.path.join(dst), file=stderr)
    for name in os.listdir(src):
        if os.path.isdir(os.path.join(src, name)):
            dup_dirs(os.path.join(src, name),
                     os.path.join(dst, name))
