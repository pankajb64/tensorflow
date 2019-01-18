_default_graph = None

class Graph:
	"""Represents a computational graph
    """
    
	def __init__(self):
		"""Construct Graph"""
		self.operations = []
		self.placeholders = []
		self.variables = []

	def as_default(self):
		global _default_graph
		print("Setting default")
		_default_graph = self