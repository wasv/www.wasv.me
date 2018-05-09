import os
import jinja2 as j2
from sys import argv

import pyj

SITE_DIR = argv[1]
env = j2.Environment(
    loader = j2.FileSystemLoader(os.path.join(SITE_DIR,'templates')),
    autoescape = False
    )

print(pyj.Page(os.path.join(SITE_DIR,"root","hello.md")).render(env,{},{'name':'test'}))
