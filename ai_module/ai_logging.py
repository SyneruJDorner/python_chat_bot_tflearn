import warnings
import logging, os, sys

warnings.simplefilter(action='ignore', category=FutureWarning)
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"