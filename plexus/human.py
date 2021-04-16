from plexus.glass import Glass


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
        self._pour(stack.get_glasses(), water_amount)

        return stack.get_glasses()

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
