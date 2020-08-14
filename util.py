




from termcolor import colored, cprint

import colorama
colorama.init()

print = lambda x: cprint(x, "red", attrs=["bold"])



from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pprint import pformat

def pprint(obj):
    print(highlight(pformat(obj), PythonLexer(), Terminal256Formatter()))
