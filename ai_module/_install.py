# ======================================================================
# This file is used to download and import all dependancies and packages
# required for this project
# ======================================================================
# pip install nltk
# pip install numpy==1.16.4
# pip install tensorflow==1.14.0
# pip install tflearn
# pip install windows-curses
# ======================================================================

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_all():
    install('nltk')
    install('numpy==1.16.4')
    install('tensorflow==1.14.0')
    install('tflearn')
    install('windows-curses')

    import nltk
    nltk.download('punkt')