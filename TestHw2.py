# Start here. Once you have good test, move on to hw2.py

import random
import unittest
from hw2 import Card, Deck, is_group
class TestCard(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize cards w/ number/color/shading/shaper"""
        c1 = Card(2, "green", "striped", "diamond")

        self.assertEqual(c1.number, 2)
        self.assertEqual(c1.color, "green")
        self.assertEqual(c1.shading, "striped")
        self.assertEqual(c1.shape, "diamond")

    def test_str(self):
        c1 = Card(2, "green", "striped", "diamond")
        self.assertEqual(str(c1), "Card(2, green, striped, diamond)")
        """test that we can get a good string representation of GroupCard instances"""

    def test_eq(self):
        c1 = Card(2, "green", "striped", "diamond")
        c2 = Card(2, "green", "striped", "diamond")
        self.assertEqual(c1,c2)
        """Tests that two cards are equal iff all attributes (number, color, shading, shape) are equal"""
        

# Write your own docstrings for the tests below
class TestDeck(unittest.TestCase):
    def test_init(self):
        x = Deck()
        self.assertEqual(len(x), 81)

    def test_draw_top(self):
        #Checks to see if card was removed from top
        x = Deck()
        test = Card(3, "purple", "solid", "oval")
        rCard = x.draw_top()
        self.assertEqual(rCard, test)
        self.assertRaises(AttributeError)

    def test_shuffle(self):
        #Checks for reshuffle
        x = Deck()
        rSeed = random.seed(652)
        shuffled = x.shuffle()
        self.assertEqual(rSeed, shuffled)

# After Card and Deck are working, write and test the alg below.
# Include a docstring.
class TestSimulator(unittest.TestCase):
    def test_is_group(self):
        #Tests to see if false or true
        c1 = Card(1,'green','empty','diamond')
        c2 = Card(2,'blue','striped','squiggle')
        c3 = Card(3,'purple','solid','oval')
        c4 = Card(2,'green','empty','diamond')
        self.assertTrue(is_group(c1,c2,c3))
        self.assertFalse(is_group(c2,c2,c4))


unittest.main() # runs all unittests above