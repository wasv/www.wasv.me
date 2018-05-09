import jinja2 as j2
import yaml
from markdown import markdown


class Page:
    fpath = ""
    content = ""
    data = {}

    def __init__(self, fpath):
        self.fpath = fpath

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
        return page
