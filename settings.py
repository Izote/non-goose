from math import ceil
from os.path import abspath, dirname, join


# General settings
ROOT_PATH = dirname(abspath(__file__))
FILE_PATH = join(ROOT_PATH, "file")
IPA_FILEPATH = join(FILE_PATH, "ipa.csv")

EXCLUDE_MANNER = ["click"]
EXCLUDE_PLACE = None
