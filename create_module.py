"""
Contains functions to create a module.
Usage:
Navigate to the root directory of the directory containing the .py files for the new module.
$<python interpreter name> create_modules.py <dir containing .py files for the modules>
Example:
    $py.exe create_modules label

creates the module 'label' containing all the .py files in the dir label.
"""

import os
import sys
from pprint import pprint
import time

root_dir = ('tic_modules',)
core_files_dir = os.getcwd()

def get_path(file_arg):
    """
    Generates the path of the directory with the .py files for the new module.
    :param [str,] file_arg: list containing various command line options.
    :return: (str) path
    """
    
    cwd = os.getcwd()
    try:
        if isinstance(file_arg, list):
            path = os.path.join(cwd, file_arg[1])
        elif isinstance(file_arg, str):
            path = os.path.join(cwd, file_arg)
    except:
        path = os.getcwd()
    finally:
        return path


def contents(path):
    """
    Retrieves the list of files and directories in dir specified by 'path'.
    Does not parse subdirectories.
    :param (str) path
    :return: [str,] list of names of .py files
    """
    
    for root, dirs, files in os.walk(path, topdown=True):
        break  # limits tree walk to the current directory
    py_files = set()
    for file_ in files:
        filename, file_ext = file_.split('.')
        if file_ext == 'py':  # and '__init__' not in filename:
            py_files.add(filename)
    return py_files


def main():
    file_arg = sys.argv
    path = get_path(file_arg)
    py_files = contents(path)
    pprint(py_files)
    
if __name__ == '__main__':
    main()