import os
import platform
import time
import sys
from pprint import pprint

_COUNT = 0
_STRICT = True


def dp(*arg):
    """
    Custom print function for debugging. Iterates through (arg), prints each element in easy to distinguish
    manner.
    :param arg:
    :return: None
    """
    global _COUNT
    _COUNT += 1
    print('.'*5, 'Start', '_COUNT')
    for i in arg:
        print(i)
    print('.'*5, 'END', '_COUNT')


def inputs(file_arg):
    """
    Parses the command parameters given and passes them to relevant functions.
    :param :list(str): file_arg:
    :return:
    """
    global _STRICT
    if len(file_arg) == 0:
        print()
        print("ERROR. Command parameters not registered!")
        print("Source Code debugging might be necessary.")
        print("Contact the program author. Include a screenshot and details of the error if possible.")
        print("Terminating program...")
        quit()
    elif len(file_arg) == 1:  # when no path or switches used, and executed command is the only arg.
        final_path_arg = os.getcwd()
    elif len(file_arg) > 1:
        if file_arg[1][0] == '-':  # when path not specified but switches used.
            final_path_arg = os.getcwd()
        else:
            final_path_arg = file_arg[1]
    return final_path_arg
         

def paths(final_path_arg):
    """
    Gets the inputs given as terminal parameters and processes them.
    :return:
    """
    global _STRICT
    path_ = os.path.realpath(os.path.expanduser(final_path_arg))
    if os.path.exists(path_) is False:
        print("ERROR. Specified path does not exist.")
        print('Interpreted path:', path_)
        if _STRICT is False:
            print("Continuing testing without terminating program.")
        else:
            print("Terminating program...")
            quit()
    else:
        return path_
    
    
def run_from_file(data_file):
    # in nt (windows) systems, replaces \t in paths with \\t, preventing its interpretation as tab character.
    if os.name == 'nt':
        data_file = data_file.replace('\t', '\\t')
    print(os.path.realpath(data_file))
    with open(data_file, 'r') as f_obj:
        file_args = f_obj.read()
        file_args = file_args.splitlines()
    for file_arg_ in file_args:
        print()
        print('Input -- test().file_arg_:  ', file_arg_)
        str2argv = file_arg_.split(sep=' ')
        use(str2argv)
        
        
def run_from_terminal():
    file_arg_ = sys.argv
    use(file_arg_)
        

def use(file_args):
    print('use().file_arg_:', file_args)
    resolved_inputs = inputs(file_args)
    path_ = paths(resolved_inputs)
    print('Output -- test().path_:   ', path_)

    
def main(data_file):
    global _STRICT
    if os.name == 'nt':
        _STRICT = False
        run_from_file(data_file)
    else:
        _STRICT = True
        run_from_terminal()
    

if __name__ == '__main__':
    print()
    test_data_file = "D:\libraries\kc\Dropbox\workspace\tic\kc\tic_modules\tests\data\test_paths_from_sh.txt"
    main(test_data_file)
    





