from jinja2 import Environment, FileSystemLoader
from dicter import dicter_parser
import os


def render_template(template_file, data_folder):
    """ render the template_file with the variables
    from load_folder folder
    """
    var = load_folder(data_folder)
    environment = Environment(loader=FileSystemLoader("."))
    template = environment.get_template(template_file)

    content = template.render( var)
    return content

def load_folder(folder):
    """
    structure of data folder:
    a "global" file, containing only one dict, whose content is directly passed as variables
    other files, containing list of dicts,
    each list being passed as variables named after the file

    folder:
        global
        list1
        ...
        listn
    gives the environment
        global[k] = v (for k,v ...)
        list1 = [...]
        listn = [...]
    """
    files = os.listdir(folder)
    files.remove("global")

    var = {}

    for f in files:
        txt = open(os.path.join(folder, f)).read()
        l = dicter_parser(txt)
        var[f] = l

    txtg = open(os.path.join(folder, "global")).read()
    dg = dicter_parser(txtg)[0]

    var.update(dg)

    return var


import argparse
parser = argparse.ArgumentParser()

# parser.add_argument("template")
# parser.add_argument("data_folder")
# args = parser.parse_args()

# rendered = render_template(args.template, args.data_folder)

"""
Usage:
give the base b,
render the template b.temp.html
with the variables from the folder data_b
to the file b.html
"""

parser.add_argument("base")
args = parser.parse_args()

template = args.base + ".temp.html"
folder = "data_" + args.base
rendered = render_template(template, folder)

fw = open(args.base + ".html", 'w')
fw.write(rendered)

# print(rendered)
