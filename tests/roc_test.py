"""
Tests for the pywind.roc module.
"""
import os
import unittest

from pywind.roc.eroc import *


class ROCTest(unittest.TestCase):
    """
    ROC Tests
    """
    def test_local(self):
        """
        Local file test.
        """
        erp = EROCPrices()
        here = os.path.dirname(__file__)
        self.assertTrue(erp.process_file(os.path.join(here, 'files', 'eroc.html')))
        self.assertTrue('200704' in erp.periods)
        self.assertEqual(erp['200704'], 47.51)
