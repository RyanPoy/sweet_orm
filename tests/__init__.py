#coding: utf8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest

import logging
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s [%(levelname)s]: %(message)s",
)

class TestCase(unittest.TestCase):
    pass
