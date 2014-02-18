from random import randrange

class Position(object):
	"""docstring for Position"""
	def __init__(self, x,y):
		super(Position, self).__init__()
		self.x = x
		self.y = y

	def add(self, position):
		self.x += position.x
		self.y += position.y
		
	def randomize(self, rangeX, rangeY):
		""" rangeX and rangeY are Tuples(min,max)"""
		self.x = randrange(rangeX[0], rangeX[1]+1)
		self.y = randrange(rangeY[0], rangeY[1]+1)
