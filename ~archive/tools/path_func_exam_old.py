import os

create_module_path = os.getcwd()  # "C:/Users/kshit/Dropbox/libraries/kc/workspace/kc/tic_modules"

# TODO: os.walk(topdown=false) from os.getcwd() and locate test_dirs == ['labels', 'tools']. Use that to contruct common_tree.

# creating test data.

# creates the common tree path shared by the directories used as test cases.
path_dirs = create_module_path.split(os.sep)
shared_tree_dirs = path_dirs[0:-2]
common_tree = os.sep.join(shared_tree_dirs)

# lists directories in the tree branches
branch_dirs = list(' ' * 3)
branch_dirs[0] = ['kc', 'tic_modules']
branch_dirs[1] = ['tic', 'tic', 'tic_labels']
branch_dirs[2] = ['tic', 'tic', 'tic_tools']

# combines common_tree, branch_dirs to create full paths for each test case.
cases_path = []
for branch_dir_ in branch_dirs:
    cases_path.append(
        os.path.join(common_tree,
                     os.sep.join(branch_dir_)
                     )
    )

probe_dirs = ['labels', 'tools']  # list of dirs with the known file names for testing.
files_list_name_suffix = "files_list"
files_list_ext = "txt"
for probe_dir_ in probe_dirs:

    files_list_in = os.extsep.join([files_list_name_suffix, files_list_ext])  # name of file with the list of files in probe_dirs.
    for test_path_ in cases_path:
        file_path = os.path.join(test_path_, files_list_in)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file_object:
                contents = file_object.read()
            files = contents.split('\n')



test_path = path_dirs
for dir in os.scandir(os.pardir):
    print(dir.name)






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

