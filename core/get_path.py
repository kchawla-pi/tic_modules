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
    print('\n','-'*50, 'Start', '-'*50, '\n', sep='\n')
    for i in arg:
        print(i)
    print('\n', '-' * 50, 'END', '-' * 50, '\n', sep='\n')


def inputs():
    """
    Gets the inputs given as terminal parameters and processes them.
    :return:
    """
    file_arg = sys.argv
    for i in range(0, len(file_arg)):
        if file_arg[i]:
            path_is_abs = file_arg[i] == os.sep or \
                          file_arg[i][0] == os.sep or \
                          file_arg[i][1] == os.sep
    dp(file_arg)
    dp(path_is_abs)
    
inputs()

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




