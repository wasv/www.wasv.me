import yaml
from markdown import markdown

class Page:
    path = ""
    fname = ""
    data = {}

    def __init__(self, fpath):
        fpath = fpath.split("/")
        self.path = path
        self.fname = fname
        with open(fname, 'r') as f:
            text = f.read()
            parts = text.split('---')
            if len(parts) == 1:
                self.data["content"] = text
            else:
                self.data = yaml.load(parts[0])
                self.data["content"] = "---".join(parts[1:])

    def render(self, env, parent, site):
        template = env.get_template(data["template"])
        text = template.render(self.data)
        content = markdown(text)
        return content
