# -*- mode: python -*-
"""
Unit tests to ensure that pippel.py is up to date with all versions of pip.
"""

import unittest
import pippel

PipBackend = pippel.PipBackend()


class TestPippel(unittest.TestCase):
    def test_get_installed_packages(self):
        """
        Tests if pippel.get_installed_packages works.
        """
        self.assertIsInstance(
            PipBackend.get_installed_packages(),
            list,
            "`get_installed_packages` does not return a list.")
        self.assertIsNot(
            len(PipBackend.get_installed_packages()),
            0,
            "`get_installed_packages` is an empty list.")


    def test_install_package(self):
        """
        Tests if pip.install_package works.
        """
        self.assertEqual(
            PipBackend.install_package('pippel_fake_package'),
            1,
            "`install_package` failed.")

    def test_remove_package(self):
        """
        Tests if pip.remove_package works.
        """
        self.assertEqual(PipBackend.remove_package('pippel_fake_package'),
                         0,
                         "`remove_package` failed.")


if __name__ == "__main__":
    unittest.main()
