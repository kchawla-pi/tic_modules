import os
import platform
import time
import sys
from pprint import pprint


def dp(*arg):
    """
    Custom print function for debugging. Iterates through (arg), prints each element in easy to distinguish
    manner.
    :param arg:
    :return: None
    """
    print('-'*50, 'Start', '-'*50, sep='\n')
    for i in arg:
        print(i)
    print('-' * 50, 'END', '-' * 50, sep='\n')


def inputs(file_arg):
    """
    Parses the command parameters given and passes them to relevant functions.
    :param :list(str): file_arg:
    :return:
    """
    
    if len(file_arg) == 0:
        print()
        print("ERROR. Command parameters not registered!")
        print("Source Code debugging might be necessary.")
        print("Contact the program author. Include a screenshot and details of the error if possible.")
        print("Terminating program...")
        quit()
    elif len(file_arg) == 1:  # when no path or switches used, and executed command is the only arg.
        paths(os.getcwd())
    elif len(file_arg) > 1:
        if file_arg[1][0] == '-':  # when path not specified but switches used.
            paths(os.getcwd())
        else:
            paths(file_arg[1])
        
def resolve_pardir_paths(path_arg):
    path_arg_parts = path_arg.split(os.sep)
    if path_arg_parts[0] == os.pardir:
        pardir_idx = list()
        pardir_count = 0
        for idx, part_ in enumerate(path_arg_parts):
            # print(idx, part_)
            if part_ == os.pardir:
                pardir_idx.append(idx)
                pardir_count += 1
            else:
                break
        post_path_parts = path_arg_parts[idx:]
        cwd = os.getcwd()
        cwd_parts = cwd.split(os.sep)
        pre_path_parts = cwd_parts[:-pardir_count]
        pre_path_parts.extend(post_path_parts)
        path_arg = os.sep.join(pre_path_parts)
        return path_arg

def paths(path_arg):
    """
    Gets the inputs given as terminal parameters and processes them.
    :return:
    """
    """
    path_arg == os.sep  :  if os.sep, then at root of *nix system
    path_arg[0] == os.sep  :  if first character is os.sep, then abs path of *nix os.
    path_arg[2] == os.sep  # for when coding on windows- root is C:\, for example.
    """
    path_is_abs = path_arg == os.sep or \
                  path_arg[0] == os.sep or \
                  path_arg[2] == os.sep  # for when coding on windows- root is C:\, for example.
    
    if path_arg_parts[0] == os.curdir:
        curdir_idx = list()
        curdir_count = 0
        for idx, part_ in enumerate(path_arg_parts):
            # print(idx, part_)
            if part_ == os.curdir:
                curdir_idx.append(idx)
                curdir_count += 1
            else:
                break
        post_path_parts = path_arg_parts[idx:]
        cwd = os.getcwd()
        cwd_parts = cwd.split(os.sep)
        pre_path_parts = cwd_parts[:-curdir_count]
        pre_path_parts.extend(post_path_parts)
        path_arg = os.sep.join(pre_path_parts)
    ## pre_path_parts = os.sep.join(cwd_parts[:-pardir_count])
    ## print('pre_path_parts', pre_path_parts)
    ## print('post_path_parts', post_path_parts)
    ## print('pre_path_parts', pre_path_parts)
    
    
    if path_is_abs is False:
        path_ = os.sep.join([os.getcwd(), path_arg])
    elif path_is_abs is True:
        path_ = path_arg
    
    
    #/ for debugging
    print('cwd:', os.getcwd())
    print('path_arg:', path_arg)
    print('path_is_abs:', path_is_abs)
    print('path_:', path_)
    print('path_ exists:', os.path.exists(path_))
    #\

    if os.path.exists(path_) is False:
        print("Specified path does not exist.")
        print('Interpreted path:', path_)
        print("Terminating program...")
        quit()
    
def main():
    print()  ##
    file_arg = sys.argv
    print('file_arg:', file_arg)
    inputs(file_arg)
    # paths(file_arg)

if __name__ == '__main__':
    main()

#
#
# dp(path_is_abs)
# dp(os.getcwd())
#
# if path_is_abs is True:
#     path = file_arg[1]
# else:
#     path = os.sep.join([os.getcwd(), file_arg[1]])
# print(path)
#
# for root, subdir, files in os.walk(path, topdown=True):
#     print('-' * 50)
#     print('root:', end='\t')
#     pprint(root)
#     print('subdir:', end='\t')
#     pprint(subdir)
#     print('files:', end='\t')
#     pprint(files)
#     print('\n' * 2 )
#     time.sleep(5)




