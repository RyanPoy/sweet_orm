#coding: utf8
import unittest
from unittest import mock
from sweet_orm.db.recordset import SQLiteRecordset, SQLError


class TestSQLiteRecordsetDelete(unittest.TestCase):

    def get_db(self):
        return mock.MagicMock('db')

    def test_delete(self):
        db = self.get_db()
        db.execute_rowcount = mock.MagicMock(return_value=3)
        tb = SQLiteRecordset(db=db, tbname='users')
        tb.where(id=[1, 2, 3], name='Ryan', age__gte=30).delete()
        db.execute_rowcount.assert_called_once_with('DELETE FROM `users` WHERE `id` IN (?, ?, ?) AND `name` = ? AND `age` >= ?', *[1, 2, 3, "Ryan", 30])

    def test_delete_with_join(self):
        db = self.get_db()
        tb = SQLiteRecordset(db=db, tbname='users')
        tb = tb.where(id=[1,2,3]).or_where(name="Ryan").join('cars', on='users.id=cars.user_id')
        with self.assertRaises(SQLError) as err:
            tb.delete()
            self.assertEqual("SQLite can't support delete with join", str(err.exception))

    def test_truncate(self):
        db = self.get_db()
        db.execute_rowcount = mock.MagicMock(return_value=10)
        db.execute = mock.MagicMock()
        tb = SQLiteRecordset(db=db, tbname='users')
        tb.where(id=[1, 2, 3]).truncate()
        db.execute_rowcount.assert_called_once_with('DELETE FROM `users`')
        db.execute.assert_called_once_with('UPDATE sqlite_sequence SET seq = 0 where name = `users`')

    def test_delete_after_find_all(self):
        db = self.get_db()
        db.fetchall = mock.MagicMock()
        db.execute_rowcount = mock.MagicMock()

        tb = SQLiteRecordset(db=db, tbname='users')
        tb = tb.where(id=1, name='Ryan')
        tb.all()
        tb.delete()

        db.fetchall.assert_called_once_with('SELECT * FROM `users` WHERE `id` = ? AND `name` = ?', *[1, 'Ryan'])
        db.execute_rowcount.assert_called_once_with('DELETE FROM `users` WHERE `id` = ? AND `name` = ?', *[1, 'Ryan'])

if __name__ == '__main__':
    unittest.main()

