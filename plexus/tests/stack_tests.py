import unittest

from plexus import Stack
from plexus.stack import StackSearcher, Human


class StackTests(unittest.TestCase):

    def setUp(self):
        self.human = Human()

    def test_pour_for_one_level_stack(self):
        stack = Stack(n_levels=1)
        self.assertEqual(len(stack), 1)

        # pour no water
        water_amount = 0
        glasses = self.human.pour(stack, water_amount)
        self.assertEqual(glasses[0].current_capacity, water_amount)

        # pour an additional of 250ml water
        glasses = self.human.pour(stack, 250)
        self.assertEqual(glasses[0].current_capacity, 250)

        # pour more water and the state should not change
        glasses = self.human.pour(stack, 300)
        self.assertEqual(glasses[0].current_capacity, 250)

    def test_pour_for_two_level_stack(self):
        stack = Stack(n_levels=2)
        self.assertEqual(len(stack), 3)

        # pour no water
        glasses = self.human.pour(30)
        self.assertEqual(glasses[0].current_capacity, 30)
        self.assertEqual(glasses[1].current_capacity, 0)
        self.assertEqual(glasses[2].current_capacity, 0)

        # pour an additional of 250ml water
        glasses = self.human.pour(250)
        self.assertEqual(glasses[0].current_capacity, 250)
        self.assertEqual(glasses[1].current_capacity, 15)
        self.assertEqual(glasses[2].current_capacity, 15)

        # pour lot more water and glasses should all be filled up
        glasses = self.human.pour(1000)
        self.assertEqual(glasses[1].current_capacity, 250)
        self.assertEqual(glasses[2].current_capacity, 250)

    def test_pour_for_three_and_four_level_stack(self):
        stack = Stack(n_levels=3)
        self.assertEqual(len(stack), 6)

        # pour no water
        glasses = self.human.pour(30)
        self.assertEqual(glasses[0].current_capacity, 30)
        self.assertEqual(glasses[1].current_capacity, 0)
        self.assertEqual(glasses[2].current_capacity, 0)
        self.assertEqual(glasses[3].current_capacity, 0)
        self.assertEqual(glasses[4].current_capacity, 0)
        self.assertEqual(glasses[5].current_capacity, 0)

        # pour an additional of 250ml water
        glasses = self.human.pour(250)
        self.assertEqual(glasses[0].current_capacity, 250)
        self.assertEqual(glasses[1].current_capacity, 15)
        self.assertEqual(glasses[2].current_capacity, 15)
        self.assertEqual(glasses[3].current_capacity, 0)
        self.assertEqual(glasses[4].current_capacity, 0)
        self.assertEqual(glasses[5].current_capacity, 0)

        # pour an additional of 500ml water
        glasses = self.human.pour(stack, 500)
        self.assertEqual(glasses[0].current_capacity, 250)
        self.assertEqual(glasses[1].current_capacity, 250)
        self.assertEqual(glasses[2].current_capacity, 250)
        self.assertEqual(glasses[3].current_capacity, 7.5)
        self.assertEqual(glasses[4].current_capacity, 15)
        self.assertEqual(glasses[5].current_capacity, 7.5)

        # fill up everything
        glasses = self.human.pour(stack, 1000)
        self.assertEqual(glasses[0].current_capacity, 250)
        self.assertEqual(glasses[1].current_capacity, 250)
        self.assertEqual(glasses[2].current_capacity, 250)
        self.assertEqual(glasses[3].current_capacity, 250)
        self.assertEqual(glasses[4].current_capacity, 250)
        self.assertEqual(glasses[5].current_capacity, 250)

        # add a new level
        stack.add_level()
        self.assertEqual(len(stack), 1 + 2 + 3 + 4)

        self.human.pour(stack, 400)
        self.assertEqual(glasses[6].current_capacity, 50)
        self.assertEqual(glasses[7].current_capacity, 150)
        self.assertEqual(glasses[8].current_capacity, 150)
        self.assertEqual(glasses[9].current_capacity, 50)


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
