#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestModels(unittest.TestCase):

    def tearDown(self):
        # Run this after each test
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_base(self):
        # Test the Base class and its methods
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

        base_instance = Base(100)
        self.assertEqual(base_instance.id, 100)

        # Save and load from file
        Base.save_to_file([base_instance])
        loaded_base_instances = Base.load_from_file()
        self.assertEqual(len(loaded_base_instances), 1)
        self.assertIsInstance(loaded_base_instances[0], Base)

    def test_rectangle(self):
        '''Test the Rectangle class and its methods'''
        rectangle_instance = Rectangle(5, 10, 2, 3, 1)

        # Check properties
        self.assertEqual(rectangle_instance.width, 5)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)
        self.assertEqual(rectangle_instance.area(), 50)

        # Save and load from file
        Rectangle.save_to_file([rectangle_instance])
        loaded_rectangle_instances = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangle_instances), 1)
        self.assertIsInstance(loaded_rectangle_instances[0], Rectangle)

    def test_square(self):
        # Test the Square class and its methods
        square_instance = Square(4, 1, 2, 1)

        # Check properties
        self.assertEqual(square_instance.size, 4)
        self.assertEqual(square_instance.width, 4)
        self.assertEqual(square_instance.height, 4)
        self.assertEqual(square_instance.x, 1)
        self.assertEqual(square_instance.y, 2)
        self.assertEqual(square_instance.area(), 16)

        # Save and load from file
        Square.save_to_file([square_instance])
        loaded_square_instances = Square.load_from_file()
        self.assertEqual(len(loaded_square_instances), 1)
        self.assertIsInstance(loaded_square_instances[0], Square)


if __name__ == '__main__':
    unittest.main()
