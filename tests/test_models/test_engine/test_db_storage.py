#!/usr/bin/python3
"""This module defines unittests for the Database storage."""
from models.engine.db_storage import DBStorage
import unittest
import pycodestyle


class TestDBStorage(unittest.TestCase):
    """Unittests for testing the Database storage class."""
    
    def testPycodeStyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_DBStorage(self):
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
