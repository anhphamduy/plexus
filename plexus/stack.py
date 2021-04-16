from plexus.glass import Glass


class Stack:
    """
    A Stack to represent a stack of glasses.

    The data structure used is a flattened binary tree since it is always perfectly balanced.
    Hence can get the left and right child by the a simple formula: 2 * depth + 1 and 2 * depth + 2.

    Time complexity is O(n) for pouring water and O(1) for looking up glass.

    Parameters
    ----------
    n_levels : int
        The initial number of levels that the stack has.


    Attributes
    ----------
    n_levels : int
        The number of levels that the stack has.
    glasses: Glass[]
        A list contains the glasses of the stack.
    """

    def __init__(self, n_levels):
        self.glasses = []
        for i in range(n_levels):
            self._initialise_level(i + 1)

        self.n_levels = n_levels

    def add_level(self):
        """
        Adds a new glass level to the current stack of glasses
        :return: Glass[]
            An updated list of glasses
        """
        self.n_levels += 1
        self._initialise_level(self.n_levels)

        return self.glasses

    def get_glasses(self):
        """
        Gets a list of glasses following flattened binary tree pattern
        :return: Glass[]
        """
        return self.glasses

    def _initialise_level(self, depth):
        """
        Initialises a new stack level
        :param depth: The depth of the level
        """
        self.glasses += [Glass() for _ in range(depth)]

    def __len__(self):
        return len(self.glasses)
