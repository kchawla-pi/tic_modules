import os

from pprint import pprint


def tests_paths():
    """
    Creates data necessary to test create_module.py.
    Makes available variable:
     tests_subtrees: list of subtrees of each test case (dirs with .py files)
    :param None: 
    :return: (list(str)): testcase_dirs
    """

    testdata_path_dirs = os.getcwd().split(os.sep)
    testdata_path_dirs.append('data')
    testdata_path = os.sep.join(testdata_path_dirs)  # creates path to data used in unit tests.

    testcase_dirs = list()  # list of directories in the subtree for each test case
    for element in os.scandir(testdata_path):
        if element.name[:4] == 'tic_' and element.is_dir():
            temp = [element.name, element.name[4:]]
            testcase_dirs.append(temp)

    return testdata_path, testcase_dirs


def files_list(tests_data_path, testcase_dir_, ext):
    fileslist_file = os.extsep.join(['~files_list', ext])
    file_path = os.sep.join([tests_data_path, os.sep.join(testcase_dir_), fileslist_file])
    with open(file_path, 'r') as file_obj:
        f_list = file_obj.readlines()
    fileslist = set(list_entry.rstrip() for list_entry in f_list)
    return fileslist


def files_list_filter(fileslist, ext='py',discard_ext=True):
    files_list = set()
    for file_ in fileslist:
        file_ = file_.rstrip()
        if '.' in file_:
            file_name, file_ext = file_.split(os.extsep)
        if file_ext == ext:
            if discard_ext:
                files_list.add(file_name)
            else:
                files_list.add(file_)
    return files_list


def main():
    tests_data_path, testcase_dirs = tests_paths()
    for testcase_dir_ in testcase_dirs:
        fileslist = files_list(tests_data_path, testcase_dir_, 'txt')
        pyfiles = files_list_filter(fileslist, 'py', discard_ext=False)


if __name__ == '__main__':
    main()