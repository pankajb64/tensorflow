import numpy as np

from Operation import Operation
from Placeholder import Placeholder
from Variable import Variable

class Session:
	"""Represents a particular execution of a computational graph.
    """
	def run(self, operation, feed_dict={}):
		"""Computes the output of an operation

        Args:
          operation: The operation whose output we'd like to compute.
          feed_dict: A dictionary that maps placeholders to values for this session
        """

        # Perform a post-order traversal of the graph to bring the nodes into the right order
		nodes_postorder = postorder_traverse(operation)

		# Iterate all nodes to determine their value
		for node in nodes_postorder:

			if type(node) == Placeholder:
				# Set the node value to the placeholder value from feed_dict
				node.output = feed_dict[node]

			elif type(node) == Variable:
				# Set the node value to the variable's value attribute
				node.output = node.value

			else: # Operation
                # Get the input values for this operation from node_values
				node.inputs = [input_node.output for input_node in node.input_nodes ]

				# Compute the output of this operation
				node.output = node.compute(*node.inputs)

			# Convert lists to numpy arrays
			if type(node.output) == list:
				node.output = np.array(node.output)

		# Return the requested node value
		return operation.output

def postorder_traverse(operation):
	"""Performs a post-order traversal, returning a list of nodes
    in the order in which they have to be computed

    Args:
       operation: The operation to start traversal at
    """
    
	postorder_traversal = []

	if isinstance(operation, Operation):
		for node in operation.input_nodes:
			postorder_traversal.extend(postorder_traverse(node))
	postorder_traversal.append(operation)

	return postorder_traversal

