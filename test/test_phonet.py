import unittest
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../src'))

from aphone_py import Filter, Phonet


class PhonetTest(unittest.TestCase):

    def test_filter(self):
        f = Filter()
        self.assertEqual(u"POPO", f.filter(u"popo"))

    def test_rule(self):
        j = """ {
          "again": false,
          "text": "EN",
          "ending": false,
          "priority": 5,
          "starting": false,
          "minus": 1,
          "alternates": "AEUIO",
          "replace": "EM"
        }"""
        p = Phonet({"rules": [ json.loads(j)]})

