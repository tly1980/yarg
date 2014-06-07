import unittest
import tempfile
import os

import yarg

def funa(a, b='b', c='c'):
    return a, b, c

class BasicParseTest(unittest.TestCase):

    def setUp(self):
        self.ymain = yarg.Main({'funa': funa})

    def test_parse1(self):
        ret = self.ymain.main(['funa', 'A', 'B', 'C'])
        self.assertEqual(ret, ('A', 'B', 'C'))

    def test_parse2(self):
        ret = self.ymain.main(['funa', '-va', '[A, B, C]'])
        self.assertEqual(ret, ('A', 'B', 'C'))

    def test_parse3(self):
        ret = self.ymain.main(['funa', '-ka', '{ a: A, b: B, c: C }'])
        self.assertEqual(ret, ('A', 'B', 'C'))

    def test_parse4(self):
        ret = self.ymain.main(['funa', '-ka', '{ a: A, b: B, c: C }', '-x', 'a: AA', 'b: 2', 'c: yes'])
        self.assertEqual(ret, ('AA', 2, True))

    def test_parse5(self):
        with self.assertRaises(SystemExit):
            self.ymain.main(['funa', 'A', 'yes', '3', '-x', 'a: AA'])

    def test_parse6(self):
        f = tempfile.NamedTemporaryFile()
        f.write("[1, 'yes', yes]")
        f.flush()
        ret = self.ymain.main(['funa', '-va', f.name])
        self.assertEqual(ret, (1, 'yes', True))

    def test_parse7(self):
        f = tempfile.NamedTemporaryFile()
        f.write("{ a: 1, b: 'yes', c: yes }")
        f.flush()
        ret = self.ymain.main(['funa', '-ka', f.name])
        self.assertEqual(ret, (1, 'yes', True))

