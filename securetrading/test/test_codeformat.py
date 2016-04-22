#!/usr/bin/env python
from __future__ import unicode_literals
import sys
import unittest
from securetrading.test import abstract_test
import glob
import os
import pkgutil

try:
    import pep8
except ImportError:
    pep8 = None


class Test_CodeFormat(abstract_test.TestCase):

    def get_files(self, directory):
        return glob.glob(os.path.join(directory, "*.py"))

    def test_pep8_conformance(self):
        ignore_error_codes = []

        base_path = pkgutil.get_loader('securetrading').filename

        test_cases = ["",
                      "test",
                      ]

        for directory in test_cases:
            path = os.path.join(base_path, directory)
            if os.path.exists(path):
                files = self.get_files(path)
                """Test that we conform to PEP8."""

                results = []
                # Need to check if pep8 is installed before running
                for f in sorted(files):
                    pep8_style = pep8.StyleGuide(quiet=True,
                                                 ignore=ignore_error_codes)
                    result = pep8_style.check_files([f])
                    if result.total_errors != 0:
                        results.append("Found code style errors (and warnings)\
 Run 'pep8 --show-source {0}'.".format(f))

                self.assertEqual(0, len(results),
                                 "results {0}".format(results))

if __name__ == '__main__':
    if pep8 is not None:
        unittest.main()
    else:
        print("PEP8 module is not installed skipping test.")