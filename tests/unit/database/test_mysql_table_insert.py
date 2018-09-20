#coding: utf8
from sweet.tests.unit import TestCase
from sweet.database.table import MySQLTable


class MySQLTableInsertTest(TestCase):

    def get_table(self):
        class FakeDB(object): pass
            # def execute_lastrowid(self, sql, *params): pass
            # def execute_rowcount(self, sql, *params): pass
        return MySQLTable(db=FakeDB(), tbname="users")

    def test_insert_an_record(self):
        def _(sql, *params):
            self.assertEqual('INSERT INTO `users` (`id`, `name`, `age`) VALUES (%s, %s, %s)', sql)
            self.assertEqual([3, "Poy", 33], list(params))
            return 1
        tb = self.get_table()
        tb.db.execute_rowcount = _
        self.assertEqual(1, tb.insert(id=3, name="Poy", age=33))

    def test_insert_an_record_with_a_dict(self):
        def _(sql, *params):
            self.assertEqual('INSERT INTO `users` (`id`, `name`, `age`) VALUES (%s, %s, %s)', sql)
            self.assertEqual([3, "Poy", 33], list(params))
            return 1
        tb = self.get_table()
        tb.db.execute_rowcount = _
        self.assertEqual(1, tb.insert(dict(id=3, name="Poy", age=33)))

    def test_insert_multple_records(self):
        def _(sql, *params):
            self.assertEqual('INSERT INTO `users` (`id`, `name`, `age`) VALUES (%s, %s, %s), (%s, %s, %s)', sql)
            self.assertEqual([3, "Poy", 33, 4, "Ryan", 44], list(params))
            return 2
        tb = self.get_table()
        tb.db.execute_rowcount = _
        self.assertEqual(
            2, 
            tb.insert([
                dict(id=3, name="Poy", age=33),
                dict(id=4, name="Ryan", age=44),
            ])
        )


if __name__ == '__main__':
    import unittest
    unitest.testmain()

    