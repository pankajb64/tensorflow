class Operation:
	"""Represents a graph node that performs a computation.

    An `Operation` is a node in a `Graph` that takes zero or
    more objects as input, and produces zero or more objects
    as output.
    """

	def __init__(self, input_nodes):
		"""Construct Operation
        """
		self.input_nodes = input_nodes

		# Initialize list of consumers (i.e. nodes that receive this operation's output as input)
		self.consumers = []

		# Append this operation to the list of consumers of all input nodes
		for node in self.input_nodes:
			node.consumers.append(self)

		# Append this operation to the list of operations in the currently active default graph
		from Graph import _default_graph
		_default_graph.operations.append(self)

	def compute(self):
		"""Computes the output of this operation.
        "" Must be implemented by the particular operation.
        """
		pass