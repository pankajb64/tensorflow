from Graph import Graph
from Variable import Variable
from Placeholder import Placeholder
from MatMul import matmul
from Addition import add
from Session import Session

# Create a new graph
g = Graph()
g.as_default()

# Create variables
A = Variable([[1, 0], [0,-1]])
b = Variable([1, 1])

# Create placeholders
x = Placeholder()

# Create hidden node y
y = matmul(A, x)

# Create output node z
z = add(y, b)

#Create session
session = Session()

#Run the session to get output for z
output = session.run(z, {
	x : [1, 2]
	})

print(output)