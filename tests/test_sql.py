#!/usr/bin/pyhthon3
"""This module defines the tests for MySQL."""
import MySQLdb
import unittest
import io
import os
from os import getenv
from unittest.mock import patch
from console import HBNBCommand
from models.engine.db_storage import DBStorage



@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Not DBStorage")
class TestMySQL(unittest.TestCase):
    """Test SQL database."""
    conn = None
    cur = None

    def connection(self):
        """Connect to MySQL databse."""
        storage = DBStorage()
        storage.reload()
        self.conn = MySQLdb.connect(getenv('HBNB_MYSQL_HOST'),
                                    getenv('HBNB_MYSQL_USER'),
                                    getenv('HBNB_MYSQL_PWD'),
                                    getenv('HBNB_MYSQL_DB'))
        self.cur = self.conn.cursor()

    def disconnection(self):
        """Disconnect from MySQL database."""
        self.cur.close()
        self.conn.close()
        self.conn = None
        self.cur = None

    def test_create_state(self):
        """Test to create a State."""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        self.cur.execute("SELECT COUNT(*) FROM states")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_city(self):
        """Test to create a City."""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id}"
                                 name="San_Francisco"''')
        self.cur.execute("SELECT COUNT(*) FROM cities")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()


if __name__ == '__main__':
    unittest.main()
