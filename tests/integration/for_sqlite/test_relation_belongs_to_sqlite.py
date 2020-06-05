#coding: utf8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

import unittest
from tests.integration.for_sqlite.helper import User, Mobile


class TestRelationBelongsToSQLite(unittest.TestCase):
    
    def setUp(self):
        self.remove_record()

    def tearDown(self):
        self.remove_record()

    def remove_record(self):
        Mobile.delete_all()
        User.delete_all()

    def test_reload(self):
        user_id = User.create(name="Jon", age=31).id
        m = Mobile.create(name="Nokia", user_id=user_id)

        key = m._build_relation_cache_key('user')
        self.assertEqual(False, hasattr(m, key))

        m.user
        self.assertEqual(True, hasattr(m, key))

        m.reload_user()
        self.assertEqual(False, hasattr(m, key))

    def test_query(self):
        user_id = User.create(name="Jon", age=31).id
        Mobile.create(name="Nokia", user_id=user_id)
        Mobile.create(name="IPhone", user_id=user_id)

        m = Mobile.where(name='Nokia').first()
        u = m.user
        self.assertEqual(User, type(u))
        self.assertEqual('Jon', u.name)
        self.assertEqual(31, u.age)

        m = Mobile.where(name='IPhone', user_id=user_id).first()
        self.assertEqual(u.id, m.user.id)

    def test_query_with_include(self):
        user_id = User.create(name="Jon", age=31).id
        Mobile.create(name="Nokia", user_id=user_id)
        Mobile.create(name="IPhone", user_id=user_id)

        m = Mobile.include('user').where(name='Nokia').first()
        u = m.user
        self.assertEqual(User, type(u))
        self.assertEqual('Jon', u.name)
        self.assertEqual(31, u.age)

        m = Mobile.include('user').where(name='IPhone', user_id=user_id).first()
        self.assertEqual(u.id, m.user.id)

    def test_create(self):
        u = User.create(name="Jon", age=31)
        mobile_id = Mobile.create(name="Nokia", user=u).id
        m = Mobile.find(mobile_id)
        self.assertEqual(u.id, m.user_id)

        u = m.user
        self.assertEqual("Jon", u.name)
        self.assertEqual(31, u.age)

    def test_save(self):
        u = User.create(name="Jon", age=31)
        mobile_id = Mobile(name="Nokia", user=u).save().id

        m = Mobile.find(mobile_id)
        self.assertEqual(u.id, m.user_id)

        u = m.user
        self.assertEqual("Jon", u.name)
        self.assertEqual(31, u.age)

    def test_update(self):
        u1 = User.create(name="Jon", age=31)
        u2 = User.create(name="Lily", age=21)
        u3 = User.create(name="Lucy", age=11)

        m = Mobile(name="Nokia", user=u1).save()
        self.assertEqual(u1.id, m.user_id)

        m.update(user=u2)
        self.assertEqual(u2.id, m.user_id)
        
        m = Mobile.where(name='Nokia').first()
        self.assertEqual(u2.id, m.user_id)

        m.user = u3
        m.save()
        self.assertEqual(u3.id, m.user_id)

        m = Mobile.where(name='Nokia').first()
        self.assertEqual(u3.id, m.user_id)


if __name__ == '__main__':
    unittest.main()
