import json
import logging
import sys

from gadlogger import Logger, config

config.setup(Logger("root", logging.INFO, json, sys.stdout))

logger = logging.getLogger()
