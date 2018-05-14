import os
import pathlib
from shutil import copyfile

import jinja2 as j2
import yaml
from markdown import markdown


class Page:
    data = None
    plain = False

    def __init__(self, fpath):
        if fpath.suffix != '.md':
            self.plain = True
            self.ipath = os.path.abspath(fpath)
            self.opath = fpath
            return

        with open(fpath, 'r') as src_file:
            text = src_file.read()

        parts = text.split('\n\n---\n\n')
        if len(parts) == 1:
            self.content = text
            self.fpath = fpath
        else:
            self.data = yaml.load(parts[0])
            self.content = "\n\n---\n\n".join(parts[1:])
            fpath = pathlib.Path(fpath)
            self.fpath = str(fpath.parent / fpath.stem) + '.html'

    def render(self, env, parent=None, site=None):
        if self.plain is True:
            copyfile(self.ipath, self.opath)
            return
        if self.data is None:
            with open(self.fpath, 'w') as dst_file:
                dst_file.write(self.content+'\n')
            return

        content_template = j2.Template(self.content)
        content = content_template.render(self.data, parent=parent.fpath,
                                          siblings=parent.contents,
                                          site=site.contents)

        page_template = env.get_template(self.data["template"])
        page = page_template.render(self.data, parent=parent.fpath,
                                    siblings=parent.contents,
                                    site=site.contents,
                                    content=markdown(content))

        with open(self.fpath, 'w') as dst_file:
            dst_file.write(page+'\n')

    def __repr__(self):
        return "<Page: %s>" % self.fpath


class Collection:
    fpath = ""
    contents = {}

    def __init__(self, fpath):
        self.fpath = pathlib.Path(fpath)

        contents = {}
        for entry in self.fpath.iterdir():
            if entry.is_dir():
                contents[str(entry.name)] = Collection(entry)
            elif entry.is_file():
                contents[str(entry.name)] = Page(entry)
        self.contents = contents

    def render(self, env, parent=None, site=None):
        try:
            os.mkdir(self.fpath)
        except FileExistsError:
            pass
        for content in self.contents.values():
            content.render(env, parent=self, site=site)

    def __repr__(self):
        return "<Collection: %s>" % self.fpath

if __name__ == "__main__":
    from sys import argv

    START_DIR = os.getcwd()
    SITE_DIR = argv[1]
    OUT_DIR = argv[2]
    TEMPLATES_DIR = os.path.abspath(os.path.join(SITE_DIR, 'templates'))

    env = j2.Environment(
        loader=j2.FileSystemLoader(TEMPLATES_DIR),
        autoescape=False
        )

    os.chdir(os.path.join(SITE_DIR, 'site'))
    site = Collection('.')

    os.mkdir(os.path.join(START_DIR, OUT_DIR))
    os.chdir(os.path.join(START_DIR, OUT_DIR))
    site.render(env, parent=site, site=site)
