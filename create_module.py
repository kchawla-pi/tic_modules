
import os
import sys
from pprint import pprint
import time


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
	cwd = os.getcwd()
	print(cwd)
	argins = sys.argv
	try:
		path = os.path.join(cwd, argins[1])
		print(path)
	except:
		path = os.getcwd()
	finally:
		time.sleep(5)
		contents(path)
