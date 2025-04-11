import json
import logging
import sys

from gadlogger import Logger
from gadlogger import config

config.setup(Logger("root", logging.INFO, json, sys.stdout))

logger = logging.getLogger()
