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

    testsdata_tree_dirs = os.getcwd().split(os.sep)  # creates path to data used in unit tests.
    testsdata_tree_dirs.append('data')
    testsdata_path = os.sep.join(testsdata_tree_dirs)

    testcase_dirs = list()  # list of directories in the subtree for each test case
    for element in os.scandir(testsdata_path):
        if element.name[:4] == 'tic_' and element.is_dir():  # selects all dirs starting with 'tic_'
            temp = [element.name, element.name[4:]]
            testcase_dirs.append(temp)  # [tic_<dir>, <dir>]

    return testsdata_path, testcase_dirs  # path to ../tests/data; list of dirs for different test cases


def files_list(tests_data_path, testcase_dir_ = tests_paths(), filename='~files_list', ext='txt'):
    """
    Reads & returns lists of files from filename.ext present in each individual test case dir.
    Typically, each test case directory is testsdata_path/testcase_dirs[0]/testcase_dirs[1]
    filename.ext default: '~files_list.txt' 
    :param tests_data_path: (str) Path to data used in testing
    :param testcase_dir_: (list(str)) lists of dirs used for individual test cases 
    :param filename: (str) name of file containing the list of files. default: '~files_list'
    :param ext: (str) extension of file to read the lists of files from. default: 'txt'
    :return: fileslist: (list) list of files in the supplied test case directory 
    """
    fileslist_file = os.extsep.join([filename, ext])
    fileslist_filepath = os.sep.join([tests_data_path, os.sep.join(testcase_dir_), fileslist_file])
    with open(fileslist_filepath, 'r') as file_obj:
        f_list = file_obj.readlines()
    fileslist = set(list_entry.rstrip() for list_entry in f_list)
    return fileslist


def files_list_filter(fileslist, ext='py',discard_ext=True):
    """
    filters the list of files generated by files_list() based on the extension in arg:ext.
    :param fileslist: (list(str)) names of files, generated by files_list().
    :param ext: (str) extension of files to keep. 
    :param discard_ext: (boolean) True(default) to not save the extension of filtered in files.
    :return: files_list: (list)
    """
    file_ext = ''
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