import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, level="DEBUG", backtrace=True, diagnose=True)
