"""
Contains functions to create a module.
Usage:
Navigate to the root directory of the directory containing the .py files for the new module.
$<python interpreter name> create_modules.py <dir containing .py files for the modules>
Example:
	$py.exe create_modules label

creates the module 'label' containing all the .py files in the dir label.
"""

import os
import sys
from pprint import pprint
import time


def path(file_arg):
	"""
	Generates the path of the directory with the .py files for the new module.
	:return:
	"""
	
	cwd = os.getcwd()
	try:
		path = os.path.join(cwd, file_arg[1])
	except:
		path = os.getcwd()
	finally:
		contents(path)


def contents(path):
	"""
	Retrieves the list of files and directories in dir specified by 'path'.
	Does not parse subdirectories.
	:param (str) path
	:return:
	"""
	
	for root, dirs, files in os.walk(path, topdown=True):
		print('_' * 29)
		pprint('root')
		print(root)
		print('dirs')
		pprint(dirs)
		print('files')
		pprint(files)
		break
		
		
if __name__ == '__main__':
	
	file_arg = sys.argv
	path(file_arg)