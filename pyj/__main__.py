import pyj
import jinja2 as j2

env = j2.Environment(
    loader = FileSystemLoader('templates'),
    autoescape = False
    )
