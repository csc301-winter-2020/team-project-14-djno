class Vector:
    def __init__(self, data):
        self._data = data

    """
    turn the data input format to comparable vectors
    """

    def unroll(self):
        raise NotImplementedError("Should be implemented in the later classes")

    def __sub__(self):
        raise NotImplementedError("Should be implemented for relative distance")

    def __repr__(self):
        raise NotImplementedError(
            "Should be implemented to show the actual data vector")
