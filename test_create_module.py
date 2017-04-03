import unittest
import os

from create_module import path
# from create_module import if __name__ == '__main__':

class CreateModuleTest(unittest.TestCase):


    def test_path(self):
        default_path_parts = ['D:\\', 'libraries', 'kc', 'workspace', 'tic', 'kc', 'tic_modules']  # dir names of path in windows
        default_path = ''
        test_dirs = ['label', 'tools']
        for path_dir_ in default_path_parts:
            default_path = os.path.join(default_path, path_dir_)
        module_dir_paths = [os.path.join(default_path, test_dir_) for test_dir_ in test_dirs]
        print(module_dir_paths)
        cwd = os.getcwd()
        print('cwd:', cwd)
        print('def:', default_path)
        for idx, test_dir_ in enumerate(test_dirs):
            print(module_dir_paths, path(test_dir_))