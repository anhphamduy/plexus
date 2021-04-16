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

    def _initialise_level(self, depth):
        """
        Initialises a new stack level
        :param depth: The depth of the level
        """
        self.glasses += [Glass() for _ in range(depth)]


class Human:
    """ Represents a human doing action entity """

    def pour(self, stack, water_amount):
        """
        Pours water into the stack of glasses
        :param stack: Stack
            The stack to be poured into
        :param water_amount: float
            The amount of water to be poured into the stack
        :return: Glass[]
            An updated list of glasses
        """
        self._pour(stack.glasses, water_amount)

        return stack.glasses

    def _pour(self, glasses, water_amount, depth=0):
        """
        Recursively pours the water into the stack
        :param glasses: Glass[]
            A list of glasses to be poured to
        :param water_amount: float
            The amount of inflow water
        :param depth: int
            The current depth in the stack
        """
        # inflow water to the glass
        glass = glasses[0]
        glass.current_capacity += water_amount

        # if the water is outflowing, flow it to the children glasses then update the glass capacity
        if glass.current_capacity > Glass.MAX_CAPACITY:
            overflow_amount = glass.current_capacity - Glass.MAX_CAPACITY

            try:
                # outflow the water to the bottom left and right glasses until no glasses are left (IndexError occurred)
                self._pour(glasses[depth + 1:], overflow_amount / 2, depth + 1)
                self._pour(glasses[depth + 2:], overflow_amount / 2, depth + 1)
            except IndexError:
                pass

            # update the glass capacity to its maximum
            glass.current_capacity = Glass.MAX_CAPACITY


class StackSearcher:
    """ A searcher to search glasses on stack based on some given criteria """

    def search_glass(self, stack, i, j):
        """
        Gets a glass from the stack of the glasses based on the position
        :param stack: Stack
            The stack that needs to be searched from
        :param i: number
            The x position of the glass
        :param j: number
            The y position of the glass
        :return: Glass
            The glass that is on (x, y)
        """
        if j > i or i < 0 or (i + 1) > stack.n_levels or j < 0:
            raise ValueError("Invalid inputs")

        # get the level offset in the binary tree array
        level_offset = ((i + 1) * i) // 2

        return self.glasses[level_offset + j]
