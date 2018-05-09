import os
import pathlib

import jinja2 as j2
import yaml
from markdown import markdown


class Page:
    fpath = ""
    content = ""
    data = {}

    def __init__(self, fpath):
        self.fpath = pathlib.Path(fpath)

        with open(self.fpath, 'r') as src_file:
            text = src_file.read()

        parts = text.split('---')
        if len(parts) == 1:
            self.content = markdown(text)
        else:
            self.data = yaml.load(parts[0])
            self.content = markdown("---".join(parts[1:]))

    def render(self, env, parent=None, site=None):
        content_template = j2.Template(self.content)
        content = content_template.render(self.data,
                                          parent=parent, site=site)
        page_template = env.get_template(self.data["template"])
        page = page_template.render(self.data, parent=parent,
                                    site=site, content=content)
        outname = str(self.fpath.parent / self.fpath.stem) + '.html'
        with open(outname, 'w') as dst_file:
            dst_file.write(page)

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
        os.mkdir(self.fpath)
        for content in self.contents.values():
            content.render(env, parent=self.contents, site=site)

    def __repr__(self):
        return "<Collection: %s>" % self.fpath
