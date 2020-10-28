




from termcolor import colored, cprint

import colorama
colorama.init()




def p(*args):
    if len(args) == 2:
        return cprint(args[0],"blue",),cprint(args[1], "red",)
    else:
        return cprint(args[0], "magenta",)




from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pprint import pformat

def pprint(obj):
    print(highlight(pformat(obj), PythonLexer(), Terminal256Formatter()))





def getArrayName(list1):
    return str(list1).replace('[','').replace(']','')






import time
import functools

from django.db import connection, reset_queries


def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func