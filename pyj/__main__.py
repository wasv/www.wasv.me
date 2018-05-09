import os
import jinja2 as j2
from sys import argv

import pyj

SITE_DIR = argv[1]
ROOT_DIR = os.path.join(SITE_DIR,'root')
TEMPLATES_DIR = os.path.join(SITE_DIR,'templates')

env = j2.Environment(
    loader = j2.FileSystemLoader(TEMPLATES_DIR),
    autoescape = False
    )

print(pyj.Page(os.path.join(ROOT_DIR,"hello.md")).render(env,{},{'name':'test'}))
