import unittest

from plexus import Stack


class StackTests(unittest.TestCase):

    def test_initialise_stack_correctly(self):
        stack = Stack(n_levels=1)
        self.assertEqual(len(stack), 1)

        stack = Stack(n_levels=2)
        self.assertEqual(len(stack), 3)

        stack = Stack(n_levels=3)
        self.assertEqual(len(stack), 6)

    def test_add_level_to_the_stack_correctly(self):
        stack = Stack(n_levels=0)
        self.assertEqual(len(stack), 0)

        stack.add_level()
        self.assertEqual(len(stack), 1)

        stack.add_level()
        self.assertEqual(len(stack), 3)

        stack.add_level()
        self.assertEqual(len(stack), 6)
