import unittest
from class_Set import Set
from class_num import Num


class ClassSet(unittest.TestCase):
    def test_sum_el(self):
        test_obj = Set(4, 2, 3, 5, 6)
        self.assertEqual(test_obj.sum_el(), 20, 'Should eqaul 20!')
        test_obj_1 = Set()
        self.assertEqual(test_obj_1.sum_el(), 0, 'should equal 0!')

    def test_average(self):
        test_obj = Set(10, 20, 30)
        self.assertEqual(test_obj.average(), 20, 'should equal 20!')
        test_obj_2 = Set(10, -42, 5)
        self.assertEqual(test_obj_2.average(), -9, 'should equal -9!')
        test_obj_3 = Set()
        with self.assertRaises(ZeroDivisionError):
            test_obj_3.average()

    def test_maximum(self):
        test_obj = Set(2, 32, 323, 14, 435, 77, 643, 32, 344, -3, 22, -33)
        self.assertEqual(test_obj.maximum(), 643, 'maximum value is 643')

    def test_minimum(self):
        test_obj = Set(2, -2, 0, 4)
        self.assertEqual(test_obj.minimum(), -2, 'should equal -2!')


class TestNum(unittest.TestCase):
    def test_input(self):
        test_obj = Num(4)
        self.assertTrue(test_obj.input_value(6), True)

    def test_output(self):
        test_obj = Num(2)
        self.assertTrue(test_obj.print_value(), True)

    def test_from_one_to_eight(self):
        test_obj = Num(77)
        self.assertEqual(test_obj.from_one_value_to_eight(), '0o115', 'Should equal 0o115')

    def test_from_one_to_sixteen(self):
        test_obj = Num(345)
        self.assertEqual(test_obj.from_one_value_to_sixteen(), '0x159', 'should equal 0x159')

    def test_one_to_two(self):
        test_obj = Num(78)
        self.assertEqual(test_obj.from_one_value_to_two(), '0b1001110', 'should equal 0b1001110')
