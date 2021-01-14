#!C:\Users\Administrator\PycharmProjects\tbgo\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'module-name==0.5.1','console_scripts','py-module-name'
__requires__ = 'module-name==0.5.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('module-name==0.5.1', 'console_scripts', 'py-module-name')()
    )
