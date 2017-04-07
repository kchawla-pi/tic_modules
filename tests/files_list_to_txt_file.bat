REM (Windows) Batch file to generate list of files in specified dirs and writes them to .txt files.
REM Can be used to test functions in create_modules.py
REM Path: "..\tic_modules\tests\testing_data\generate_files_list_independent_of_py.bat"

dir /B C:\Users\kshit\Dropbox\libraries\kc\workspace\kc\tic_modules\tests\testing_data\tic_labels\labels > C:\Users\kshit\Dropbox\libraries\kc\workspace\kc\tic_modules\tests\testing_data\files_lists\tic_labels-labels.txt
dir /B C:\Users\kshit\Dropbox\libraries\kc\workspace\kc\tic_modules\tests\testing_data\tic_tools\tools > C:\Users\kshit\Dropbox\libraries\kc\workspace\kc\tic_modules\tests\testing_data\files_lists\tic_tools-tools.txt