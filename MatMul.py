from Operation import Operation

class matmul(Operation):
	"""Multiplies matrix x by matrix y, producing x * y.
    """

	def __init__(self, x, y):
		"""Construct matmul

        Args:
          x: First matrix
          y: Second matrix
        """
		super().__init__([x,y])

	def compute(self, x_value, y_value):
		"""Compute the output of the matmul operation

        Args:
          x_value: First matrix value
          y_value: Second matrix value
        """
		return x_value.dot(y_value)