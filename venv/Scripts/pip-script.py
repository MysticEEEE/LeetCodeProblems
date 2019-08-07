<<<<<<< HEAD
#!"F:\Python Repository\LeetCodeProblems\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==19.0.3','console_scripts','pip'
__requires__ = 'pip==19.0.3'
=======
#!C:\Users\gaogao\PycharmProjects\LeetCode\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==10.0.1','console_scripts','pip'
__requires__ = 'pip==10.0.1'
>>>>>>> origin/master
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
<<<<<<< HEAD
        load_entry_point('pip==19.0.3', 'console_scripts', 'pip')()
=======
        load_entry_point('pip==10.0.1', 'console_scripts', 'pip')()
>>>>>>> origin/master
    )
