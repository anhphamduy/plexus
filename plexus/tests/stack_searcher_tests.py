import unittest

from plexus.stack import StackSearcher, Stack


class StackSearcherTests(unittest.TestCase):

    def setUp(self):
        self.searcher = StackSearcher()

    def test_search_glass_on_one_level_stack(self):
        stack = Stack(n_levels=1)

        self.assertIs(self.searcher.search_glass(stack, 0, 0), stack.glasses[0])
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 0, 1))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 1, 0))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, -1, 0))

    def test_search_glass_on_two_level_stack(self):
        stack = Stack(n_levels=2)

        self.assertIs(self.searcher.search_glass(stack, 0, 0), stack.glasses[0])
        self.assertIs(self.searcher.search_glass(stack, 1, 0), stack.glasses[1])
        self.assertIs(self.searcher.search_glass(stack, 1, 1), stack.glasses[2])

        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 0, 1))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 2, 0))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 1, 2))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 1, -1))

    def test_search_glass_on_three_level_stack(self):
        stack = Stack(n_levels=3)

        self.assertIs(self.searcher.search_glass(stack, 0, 0), stack.glasses[0])
        self.assertIs(self.searcher.search_glass(stack, 1, 0), stack.glasses[1])
        self.assertIs(self.searcher.search_glass(stack, 1, 1), stack.glasses[2])
        self.assertIs(self.searcher.search_glass(stack, 2, 0), stack.glasses[3])
        self.assertIs(self.searcher.search_glass(stack, 2, 1), stack.glasses[4])
        self.assertIs(self.searcher.search_glass(stack, 2, 2), stack.glasses[5])

        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 2, 3))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 2, 4))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 3, 2))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, -1, 0))
        self.assertRaises(ValueError, lambda: self.searcher.search_glass(stack, 3, -1))
