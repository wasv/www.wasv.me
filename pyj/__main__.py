import os
from sys import argv

import jinja2 as j2

import pyj

SITE_DIR = argv[1]
ROOT_DIR = os.path.join(SITE_DIR, 'root')
TEMPLATES_DIR = os.path.join(SITE_DIR, 'templates')

env = j2.Environment(
    loader=j2.FileSystemLoader(TEMPLATES_DIR),
    autoescape=False
    )

print(pyj.Page(os.path.join(ROOT_DIR, "hello.md"))
      .render(env, site={'name': 'example'}))
