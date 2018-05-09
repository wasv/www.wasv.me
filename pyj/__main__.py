import os
from sys import argv

import jinja2 as j2

import pyj

SITE_DIR = argv[1]
OUT_DIR = argv[2]
ROOT_DIR = os.path.join(SITE_DIR, 'root')
TEMPLATES_DIR = os.path.abspath(os.path.join(SITE_DIR, 'templates'))

ENV = j2.Environment(
    loader=j2.FileSystemLoader(TEMPLATES_DIR),
    autoescape=False
    )

c = pyj.Collection(os.path.join(ROOT_DIR))
print(c)
os.mkdir(OUT_DIR)
os.chdir(OUT_DIR)
os.mkdir(SITE_DIR)
c.render(ENV, parent=c, site=c)
