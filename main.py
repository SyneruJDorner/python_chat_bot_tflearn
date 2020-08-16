import sys

import ai_module.ai_logging
from ai_module import training_module
from ai_module import chat_module
from ai_module import _install as install

def main():
    if (len(sys.argv) >= 2):
        arg = str(sys.argv[1]).lower()

        if (arg == "install"):
            install.install_all()
            return

        if (arg == "train"):
            training_module.train()
            return
            
    chat_module.chat()

if __name__ == "__main__":
    main()