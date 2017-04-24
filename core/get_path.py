import os
import platform
import time
import sys
from pprint import pprint

_OS_TYPE = 'nix'
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
    path_ = os.path.abspath(final_path_arg)
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

    
def set_os_type(os_info='nix'):
    if 'win' in os_info.lower():
        global _OS_TYPE
        _OS_TYPE = 'win'
        os_info = 'win'
    return os_info
    
    
def test():
    global _OS_TYPE
    global _STRICT
    _STRICT = False
    test_data_file = "D:\\libraries\\kc\\Dropbox\\workspace\\tic\\kc\\tic_modules\\tests\\data\\test_paths_from_sh.txt"
    print(os.path.abspath(test_data_file))
    with open(test_data_file, 'r') as f_obj:
        file_args = f_obj.readlines()
    for file_arg_ in file_args:
        file_arg_ = file_arg_.rstrip()
        print()
        print('Input -- test().file_arg_:  ', file_arg_)
        str2argv = file_arg_.split(sep=' ')
        resolved_inputs = inputs(str2argv)
        path_ = paths(resolved_inputs)
        print('Output -- test().path_:   ', path_)
        

def use():
    global _OS_TYPE
    global _STRICT
    _STRICT = True
    print('use', _OS_TYPE)
    file_arg_ = sys.argv
    print('use().file_arg_:', file_arg_)
    inputs(file_arg_)

    
def main():
    global _OS_TYPE
    os_info = platform.platform()
    os_info = set_os_type(os_info)
    _OS_TYPE = os_info
    if _OS_TYPE == 'win':
        test()
    else:
        use()
    

if __name__ == '__main__':
    print()
    main()
    





