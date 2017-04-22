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


def paths(file_arg):
    """
    Gets the inputs given as terminal parameters and processes them.
    :return:
    """
    print()
    path_is_abs = 'empty'
    # for i in range(0, len(file_arg)):
    if file_arg[1]:
        print(1)
        path_is_abs = file_arg[1] == os.sep or \
                      file_arg[1][0] == os.sep or \
                      file_arg[1][2] == os.sep  # for when coding on windows
        
    if path_is_abs is False:
        cwd = os.getcwd()
        if file_arg[1]:
            path_ = os.sep.join([cwd, file_arg[1]])
        else:
            path_ = cwd
    elif path_is_abs is True:
        path_ = file_arg[1]
    
    print('cwd:', os.getcwd())
    print('file_arg:', file_arg)
    print('path_is_abs:', path_is_abs)
    print('path_:', path_)
    print('path_ exists:', os.path.exists(path_))
    
    
def main():
    file_arg = sys.argv
    paths(file_arg)

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




