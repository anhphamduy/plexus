class Glass:
    """ Represents a glass entity """

    MAX_CAPACITY = 250

    def __init__(self, current_capacity=0):
        self.current_capacity = current_capacity

    def __repr__(self):
        return f'Glass(current_capacity={self.current_capacity})'
