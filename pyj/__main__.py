import os
from sys import argv

import jinja2 as j2

import pyj

START_DIR = os.getcwd()
SITE_DIR = argv[1]
OUT_DIR = argv[2]
TEMPLATES_DIR = os.path.abspath(os.path.join(SITE_DIR, 'templates'))

env = j2.Environment(
    loader=j2.FileSystemLoader(TEMPLATES_DIR),
    autoescape=False
    )

os.chdir(os.path.join(SITE_DIR, 'site'))
site = pyj.Collection('.')

os.mkdir(os.path.join(START_DIR, OUT_DIR))
os.chdir(os.path.join(START_DIR, OUT_DIR))
site.render(env, parent=site, site=site)
