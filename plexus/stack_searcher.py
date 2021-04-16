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

        return stack.get_glasses()[level_offset + j]
