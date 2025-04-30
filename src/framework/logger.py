import json
import logging
import sys

from gadlogging import Logger
from gadlogging import config

config.setup(
    Logger("root", logging.INFO, json, sys.stdout),
    Logger("asyncio.detector", logging.WARNING, json, sys.stdout),
    Logger("sqlalchemy.profiler", logging.INFO, json, sys.stdout),
    Logger("fastapi.route", logging.INFO, json, sys.stdout),
)

logger = logging.getLogger()
