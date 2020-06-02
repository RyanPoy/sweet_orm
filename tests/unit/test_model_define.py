#coding: utf8
from unittest import mock
import unittest
from sweet_orm.orm.model import Model


def get_db():
    db = mock.MagicMock('db')
    db.qutotation_marks = '`'
    db.paramstyle_marks = '%s'
    db.get_columns = mock.MagicMock(return_value={})
    return db

db = get_db()

class ModelAutoStub(Model):
    db = db

class ModelCustomerStub(Model):
    db = db
    __tablename__ = 'customer_models'
    __pk__ = 'customer_pk'
    __timestamp__ = False


class TestModelDefine(unittest.TestCase):

    def test_auto_tablename(self):
        self.assertEqual('model_auto_stubs', ModelAutoStub.__tablename__)

    def test_auto_primary_key(self):
        self.assertEqual('id', ModelAutoStub.__pk__)

    def test_auto_created_at(self):
        self.assertTrue(hasattr(ModelAutoStub, 'created_at'))

    def test_auto_updated_at(self):
        self.assertTrue(hasattr(ModelAutoStub, 'updated_at'))

    def test_customer_tablename(self):
        self.assertEqual('customer_models', ModelCustomerStub.__tablename__)

    def test_customer_primary_key(self):
        self.assertEqual('customer_pk', ModelCustomerStub.__pk__)

    def test_auto_created_at(self):
        self.assertFalse(hasattr(ModelCustomerStub, 'created_at'))

    def test_auto_updated_at(self):
        self.assertFalse(hasattr(ModelCustomerStub, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
