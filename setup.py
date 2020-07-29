import cx_Freeze
import sys
import os
import os.path


#dependencies
import  re

base=None

if sys.platform=='win32':
    base='Win32GUI'

PYTHON_INSTALL_DIR=os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')


executables=[cx_Freeze.Executable('main.py',base=base,icon="icon.ico")]

cx_Freeze.setup(
    name = "Vpad Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
)