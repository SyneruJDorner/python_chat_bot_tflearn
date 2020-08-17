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

import sys, subprocess, os, shutil

def install(package, *args):
    install_string = [sys.executable, "-m", "pip", "install", package]
    install_string = install_string + list(args)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_all():
    install('nltk', "--user")
    install('numpy==1.16.4', "--user")
    install('tensorflow==1.14.0', "--user")
    install('tflearn', "--user")
    install('windows-curses', "--user")

    import nltk
    nltk.download('punkt')

def clean():
    folder = os.path.join(os.getcwd(), "trained_data")

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print('Completed cleaning up training data.')