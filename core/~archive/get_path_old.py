import os
import platform
import time
import sys
from pprint import pprint

_OS_TYPE = 'nix'
_COUNT = 0


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
         
    
def resolve_dots_in_path(path_arg):
    cwd_parts = os.getcwd().split(os.sep)
    path_arg_parts = path_arg.split(os.sep)
    temp = list()
    for part_ in path_arg_parts:
        if '.py' not in part_:
            if part_ != os.curdir:
                temp.append(part_)
    path_arg_parts = temp.copy()
    temp = list()
    for part_ in path_arg_parts:
        if part_ == os.pardir:
            cwd_parts.pop()
        else:
            temp.append(part_)
    # path_arg = os.sep.join(temp)
    cwd_parts.extend(temp)
    path_ = os.sep.join(cwd_parts)
    print("resolve_dots_in_path().path_:", path_)
    return path_
    

def paths(path_arg):
    """
    Gets the inputs given as terminal parameters and processes them.
    :return:
    """
   
    path_is_abs = is_path_abs(path_arg)

    path_ = resolve_dots_in_path(path_arg)
    
    if path_is_abs is False:
        path_ = os.sep.join([os.getcwd(), path_arg])
    elif path_is_abs is True:
        path_ = path_arg
    
    
    #/ for debugging
    # print('-'*50)
    # print('cwd:', os.getcwd())
    # print('path_arg:', path_arg)
    # print('path_is_abs:', path_is_abs)
    # print('path_:', path_)
    # print('path_ exists:', os.path.exists(path_))
    # print('-' * 50)
    #\

    if os.path.exists(path_) is False:
        print("ERROR. Specified path does not exist.")
        print('Interpreted path:', path_)
        print("Terminating program...")
        quit()


def is_path_abs(path_arg):
    sep_char = {'/', '\\'}
    a = path_arg == os.sep  # if os.sep, then at root of *nix system
    b = path_arg[0] == os.sep  # if first character is os.sep, then abs path of *nix os.
    c = path_arg[1] == ':'  # for when coding on windows- root is C:\, for example.
    path_is_abs = a or b or c
    return path_is_abs


def path_win2nix(path_win):
    """
    Accepts a windows path as arg and returns its unix-style path.
    :param (str) path_win:
    :return: (str)
    """
    temp = path_win.split(os.sep)
    temp.reverse()
    nix_add = ['', 'mnt', temp[-1][0].lower()]
    nix_add.reverse()
    temp.pop()
    temp.extend(nix_add)
    temp.reverse()
    file_nix = os.path.sep.join(temp)
    # print('>'*100, 'file_nix:', file_nix)
    return file_nix


def path_nix2win(path_nix):
    """
    Converts a unix style path into a windows-style path.
    :param (str) path_nix:
    :return: (str)
    """
    path_is_abs = is_path_abs(path_nix)
    temp = path_nix.split(os.sep)
    if path_is_abs is False:
        if './' in path_nix:
            print("WARNING: PATH uses . and .. Verify converted PATH. Accomodations might be necessary.")
    elif path_is_abs is True:
        if path_nix[1] == 'mnt':
            drive_ = ''.join([path_nix[2], ':'])
            temp[0] = drive_
    else:
        print("ERROR in unix to windows path conversion in path_nix2win()")
    path_win = '\\'.join(temp)
    return path_win
        # drive_letters = tuple(chr(num) for num in list(range(67, 91)))
        # temp = path_nix.split(os.sep)
        # for path_part_ in temp[0:5]:
        #     for drive_letter_ in drive_letters:
        #         if path_part_ == drive_letter_

    # print('>'*100, 'file_nix:', file_nix)
    return file_nix
    
    
def set_os_type(os_info='nix'):
    if 'win' in os_info.lower():
        global _OS_TYPE
        _OS_TYPE = 'win'
        os_info = 'win'
    return os_info
    
    
def test():
    global _OS_TYPE
    test_data_file = "D:\\libraries\\kc\\Dropbox\\workspace\\tic\\kc\\tic_modules\\test_paths_from_sh.txt"
    if _OS_TYPE == 'nix':
        test_data_file = path_win2nix(test_data_file)
    # print('>'*100, 'test_data_file:', test_data_file)
    # file_nix = "/home/kc/workspace-dropbox/tic/kc/tic_modules/test_paths_from_sh.txt"
    with open(test_data_file, 'r') as f_obj:
        contents = f_obj.readlines()
    for content_ in contents:
        content_ = content_.rstrip()
        print('test().content_:', content_)
        str2argv = content_.split(sep=' ')
        inputs(str2argv)


def main():
    file_arg = sys.argv
    print('main().file_arg:', file_arg)
    inputs(file_arg)
    # paths(file_arg)

if __name__ == '__main__':
    print()  ##
    # global _OS_TYPE
    os_info = platform.platform()
    os_info = set_os_type(os_info)
    
    _OS_TYPE = os_info
    # print('> >', _OS_TYPE)
    # print('< <', os_info)
    path_nix = "/mnt/d/xyz/abc.txt"
    print(path_nix2win(path_nix))
    # test()
    # main()

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




