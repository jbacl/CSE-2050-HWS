# Import what you need
# Include unittests here. Focus on readability, including comments and docstrings.
import unittest
from RecordsMap import LocalRecord, RecordsMap


class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """Tests pos, min, and max"""
        position = (3.43543, 6.43213)
        x = LocalRecord(position)
        self.assertEqual(x.pos, (3, 6))
        self.assertEqual(x.max, None)
        self.assertEqual(x.min, None)

    def test_hash(self):
        """Tests has position"""
        position = (3.43543, 6.43213)
        x = LocalRecord(position)
        hashed = x.__hash__()
        self.assertEqual(hashed, hash((3,6)))

    def test_eq(self):
        """Tests if two records are the same position"""
        x1 = LocalRecord((3.43543, 6.43213))
        x2 = LocalRecord((3.43543, 6.43213))
        x3 = LocalRecord((4.43543, 8.43213))
        self.assertEqual(x1,x2)
        self.assertNotEqual(x1, x3)

    def test_add_report(self):
        """Tests if the max and min are updated"""
        x = LocalRecord((3.43543, 6.43213), 5, 4)
        new_max = x.add_report(8)
        self.assertEqual(x.max, 8)

        new_min = x.add_report(1)
        self.assertEqual(x.min, 1)

class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """Testing len, get, contains, and add_report"""
        x = RecordsMap()

        x.add_report((3,6, 5))

        #Get Item Tests
        item = x.__getitem__((3,6))
        self.assertEqual(item, (5,5))

        #Contains tests
        item1 = x.__contains__((3,6))
        self.assertTrue(item1)
        item2 = x.__contains__((4,8))
        self.assertFalse(item2)

        #Len tests of RecordsMap
        self.assertEqual(x.len, 1)

    def test_add_many_reports(self):
        """Testing len, get, contains, and add_report"""
        x = RecordsMap()
        #Tests add report
        x.add_report((2,5), 5)
        x.add_report((2,5), 5)
        x.add_report((3,1), 3)
        x.add_report((3,2), 6)

        item = x.__getitem__((2,5))
        self.assertEqual(item, (5,5))

        #Tests contains
        item1 = x.__contains__((2,5))
        self.assertTrue(item1)
        item2 = x.__contains__((3,2))
        self.assertTrue(item2)
        item3 = x.__contains__((3,4))
        self.assertFalse(item3)

        #Tests len
        self.assertEqual(x.len, 3)
        
# You need to add a line here to run the unittests
unittest.main()