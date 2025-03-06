from jinja2 import Environment, FileSystemLoader
from dicter import dicter_parser
import os
import hjson


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
        if f[0] != ".":
            txt = open(os.path.join(folder, f)).read()
            # l = dicter_parser(txt)
            l = hjson.loads(txt)
            var[f] = l

    txtg = open(os.path.join(folder, "global")).read()
    # dg = dicter_parser(txtg)[0]
    dg = hjson.loads(txtg)

    var.update(dg)

    return var


import argparse
parser = argparse.ArgumentParser()

# parser.add_argument("template")
# parser.add_argument("data_folder")
# args = parser.parse_args()

# rendered = render_template(args.template, args.data_folder)

help_mess="""
Usage:
give the base b,
render the template b.temp.html
with the variables from the folder data_b
to the file b.html
"""

parser.add_argument("base", help=help_mess)
parser.add_argument("--suff", help="if present, add _suff to the data folder path")
args = parser.parse_args()

template = args.base + ".temp.html"
if args.suff:
    suff = "_"+args.suff
else:
    suff = ""
folder = "data_" + args.base + suff
rendered = render_template(template, folder)
file_rendered = args.base + suff + ".html"

fw = open(file_rendered, 'w')
fw.write(rendered)

# print(rendered)
