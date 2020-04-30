#coding: utf8
from sweet.tests import TestCase
from sweet.orm.model import Model
from sweet.orm.relation import *


class TestRelationBasic(TestCase):

    def test_belongs_to_without_argument(self):

        class Member(Model):
            __table_name__ = 'users'

        class Phone(Model):
            __table_name__ = 'mobiles'
            belongs_to(Member)

        r = Phone.__relations__.get('member')
        self.assertEqual(BelongsTo, type(r))
        self.assertEqual(Phone, r.owner)
        self.assertEqual(Member, r.target)
        self.assertEqual('member_id', r.fk)
        self.assertEqual('id', r.pk)
        
    def test_belongs_to_with_argument(self):

        class Member(Model):
            __pk__ = 'member_id'
            __table_name__ = 'users'

        class Phone(Model):
            __table_name__ = 'mobiles'
            belongs_to(Member, fk='owner_id')

        r = Phone.__relations__.get('member')
        self.assertEqual(BelongsTo, type(r))
        self.assertEqual(Phone, r.owner)
        self.assertEqual(Member, r.target)
        self.assertEqual('owner_id', r.fk)
        self.assertEqual('member_id', r.pk)    


if __name__ == '__main__':
    import unittest
    unittest.main()
