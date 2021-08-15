#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
from unittest import result
import MySQLdb
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

uname = os.environ.get('HBNB_MYSQL_USER')
upass = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
dbase = os.environ.get('HBNB_MYSQL_DB')
u_env = os.environ.get('HBNB_ENV')

run = os.system
sql = 'CREATE DATABASE IF NOT EXISTS hbnb_test_db;'
run("echo '{}' | mysql -uhbnb_test -phbnb_test_pwd ".format(sql))

db = MySQLdb.connect(host,
                     uname,
                     upass,
                     dbase,
                     port=3306)

cursor = db.cursor()


class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        # from models.engine.db_storage import DBStorage
        # storage = DBStorage()
        # storage.reload()
        pass

    def test_create_table(self):
        """Check number of tables"""
        sql = "SHOW TABLES;"
        result = cursor.execute(sql)
        self.assertEqual(result, 7)

    def test_State_create(self):
        """Check all States"""
        sql = "SELECT * FROM states;"
        result = cursor.execute(sql)
        self.assertEqual(result, 0)
        new = State()
        new.name = "California"
        self.state_id = new.id
        new.save()
        sql = "SELECT * FROM states;"
        result = cursor.execute(sql)
        self.assertEqual(result, 0)

