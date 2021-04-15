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


    Examples
    --------
    >>> from plexus import Stack
    >>> stack = Stack(n_levels=2)
    >>> stack.pour(2000)
    [Glass(current_capacity=250), Glass(current_capacity=250), Glass(current_capacity=250)]
    >>> print(stack.get_glass(0, 0))
    250
    >>> print(stack.get_glass(1, 0))
    250
    """

    def __init__(self, n_levels):
        self.glasses = []
        self.n_levels = n_levels
        raise NotImplementedError()

    def pour(self, water_amount):
        """
        Pours water into the stack of glasses
        :param water_amount: number
            The amount of water to be poured into
        :return: Glass[]
            An updated list of glasses
        """
        raise NotImplementedError()

    def add_level(self):
        """
        Adds a new glass level to the current stack of glasses
        :return: Glass[]
            An updated list of glasses
        """
        raise NotImplementedError()

    def get_glass(self, depth, j):
        """
        Gets a glass from the stack of the glasses based on the position
        :param depth: number
            The x position of the glass
        :param j: number
            The y position of the glass
        :return: Glass
            The glass that is on (x, y)
        """
        raise NotImplementedError()
