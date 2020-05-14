#coding: utf8
from sweet.tests import TestCase
from sweet.tests import StudentForHasOneThrough as Student
from sweet.tests import CourseForHasOneThrough as Course
from sweet.tests import ScoreForHasOneThrough as Score


class TestRelationHasOneThroughMysql(TestCase):

    def setUp(self):
        self.remove_record()

    def tearDown(self):
        self.remove_record()

    def remove_record(self):
        Score.delete_all()
        Student.delete_all()
        Course.delete_all()

    def test_query(self):
        s1 = Student.create(name='lily')
        s2 = Student.create(name='jon')

        c1 = Course.create(name='math')
        c2 = Course.create(name='sport')

        Score.create(student=s1, course=c1, value=100)
        Score.create(student=s2, course=c2, value=90)

        self.assertEqual(2, len(Score.all()))

        self.assertEqual('math', s1.course.name)
        self.assertEqual('sport', s2.course.name)

        self.assertEqual('lily', c1.student.name)
        self.assertEqual('jon', c2.student.name)

    def test_dissociate(self):
        s1 = Student.create(name='lily')
        c1 = Course.create(name='math')
        Score.create(student=s1, course=c1, value=100)


        self.assertEqual(1, len(Score.all()))

        s1.dissociate_with_course(c1)
        self.assertEqual(0, len(Score.all()))
        self.assertEqual(None, s1.course)
        self.assertEqual(None, c1.student)


if __name__ == '__main__':
    import unittest
    unittest.main()
