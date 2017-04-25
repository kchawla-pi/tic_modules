import unittest
import os

# import setup_testing as st
from core.create_module import get_path
from core.create_module import contents


# from create_module import if __name__ == '__main__':


class CreateModuleTest(unittest.TestCase):


    def test_path(self):
        tests_relative_path = st.tests_path()
        for case in range(0, len(tests_relative_path)):
            path_fn_returns = get_path(tests_relative_path[case])
            expected_value = os.sep.join(tests_subtree_dirs[case])
            self.assertEqual(path_fn_returns, expected_value)

    def test_contents(self, ext='txt'):
        for case in range(0, len(self.tests_relative_path)):
            path = self.tests_relative_path[case]
            contents_fn_returns = contents(path)
            filenames = self.filenames(path, ext)
            expected_values = self.py_files(filenames)
            self.assertEqual(contents_fn_returns, expected_values)


            # expected_value =


unittest.main()
