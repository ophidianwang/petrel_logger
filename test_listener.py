# -*- coding: utf-8 -*-

import logging
import logging.config

logging.config.fileConfig("logconfig.ini")
logger = logging.getLogger('mark')

cursor = 0
while cursor<10:
    logger.error("test_listener")
    cursor += 1