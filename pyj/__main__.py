import os
from sys import argv

import jinja2 as j2

import pyj

START_DIR = os.getcwd()
SITE_DIR = argv[1]
OUT_DIR = argv[2]
TEMPLATES_DIR = os.path.abspath(os.path.join(SITE_DIR, 'templates'))

ENV = j2.Environment(
    loader=j2.FileSystemLoader(TEMPLATES_DIR),
    autoescape=False
    )

os.chdir(SITE_DIR)
site = pyj.Collection('site')

os.mkdir(os.path.join(START_DIR, OUT_DIR))
os.chdir(os.path.join(START_DIR, OUT_DIR))
site.render(ENV, parent=site, site=site)
