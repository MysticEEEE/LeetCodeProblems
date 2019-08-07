<<<<<<< HEAD
#!"F:\Python Repository\LeetCodeProblems\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==40.8.0','console_scripts','easy_install'
__requires__ = 'setuptools==40.8.0'
=======
#!C:\Users\gaogao\PycharmProjects\LeetCode\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==39.1.0','console_scripts','easy_install'
__requires__ = 'setuptools==39.1.0'
>>>>>>> origin/master
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
<<<<<<< HEAD
        load_entry_point('setuptools==40.8.0', 'console_scripts', 'easy_install')()
=======
        load_entry_point('setuptools==39.1.0', 'console_scripts', 'easy_install')()
>>>>>>> origin/master
    )
