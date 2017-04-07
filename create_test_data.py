import os
from pprint import pprint as pp  # for ease of priningt lists during debugging.

from create_module import path  # serves no purpose in this file, yet.


# TODO: os.walk(topdown=false) from os.getcwd() and locate test_dirs == ['labels', 'tools']. Use that to contruct common_tree.

# creating test data.

# creates the common path to the testing data.
create_module_path = os.getcwd()  # "C:/Users/kshit/Dropbox/libraries/kc/workspace/kc/tic_modules"
tests_path_dirs = create_module_path.split(os.sep)
tests_path_dirs.append('tests')
tests_path_dirs.append('data')
tests_data_path = os.sep.join(tests_path_dirs)
tests_subtree_dirs = list()

for ls_entry in os.scandir(tests_data_path):
    if ls_entry.name[:4] == 'tic_' and ls_entry.is_dir():
        temp = tests_path_dirs + [ls_entry.name, ls_entry.name[4:]]
        tests_subtree_dirs.append(temp)

test_dir_start_idx = len(create_module_path.split(os.sep))

tests_subtrees = [os.sep.join(dirs[test_dir_start_idx:]) for dirs in tests_subtree_dirs]

for case in range(0, len(tests_subtrees)):
    path_check = path(tests_subtrees[case]) == os.sep.join(tests_subtree_dirs[case])
    print(path_check)
# path()
print()






















# for test_case_ in os.scandir()test_cases
# # combines common_tree, test_dirs to create full paths for each test case.
# cases_path = []
# for test_dir_ in test_dirs:
#     cases_path.append(
#         os.path.join(common_tree,
#                      os.sep.join(test_dir_)
#                      )
#     )
#
# probe_dirs = ['labels', 'tools']  # list of dirs with the known file names for testing.
# files_list_name_suffix = "files_list"
# files_list_ext = "txt"
# for probe_dir_ in probe_dirs:
#
#     files_list_in = os.extsep.join([files_list_name_suffix, files_list_ext])  # name of file with the list of files in probe_dirs.
#     for test_path_ in cases_path:
#         file_path = os.path.join(test_path_, files_list_in)
#         if os.path.exists(file_path):
#             with open(file_path, 'r') as file_object:
#                 contents = file_object.read()
#             files = contents.split('\n')
#
#
#
# test_path = test_path_dirs
# for dir in os.scandir(os.pardir):
#     print(dir.name)
#





# default_path_parts = ['D:\\', 'libraries', 'kc', 'workspace', 'tic', 'kc',
#                       'tic_modules']  # dir names of path in windows
# default_path = ''
# test_dirs = ['label', 'tools']
# for path_dir_ in default_path_parts:
#     default_path = os.path.join(default_path, path_dir_)
# module_dir_paths = [os.path.join(default_path, test_dir_) for test_dir_ in test_dirs]
# print(module_dir_paths)
# cwd = os.getcwd()
# print('cwd:', cwd)
# print('def:', default_path)
# for idx, test_dir_ in enumerate(test_dirs):
#     print(module_dir_paths, path(test_dir_))

