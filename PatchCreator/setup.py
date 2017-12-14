# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:00:31 2017

@author: almge
"""

import sys

from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os","tkinter"]}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes      = []
include_files = [r"c:\\Users\\almge\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tcl86t.dll", \
                 r"c:\\Users\\almge\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tk86t.dll"]

setup(
    name = "Test",
    version = "1.0",
    options = {"build_exe": {"includes": includes, "include_files": include_files}},
    executables = [Executable("c:\\Chrome\\patch_script.py", base=base)]
)