#!/usr/bin/python3
"""unittest for review module"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_default_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == "__main__":
    unittest.main()
