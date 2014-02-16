from Position import Position


class GameObject(object):
	"""docstring for GameObject"""
	def __init__(self):
		super(GameObject, self).__init__()
		self.position = Position(None,None)
		

class Dalek(GameObject):
	"""docstring for Dalek"""
	def __init__(self):
		super(Dalek, self).__init__()

	def move(docPos):
		self.position.x += 1 if docPos.x > self.position.x else -1
		self.position.y += 1 if docPos.y > self.position.y else -1


class ScrapHeap(GameObject):
        """docstring for ScrapHeap"""
        def __init__(self):
                super(ScrapHeap, self).__init__()

class Doctor(object):
	"""docstring for Doctor"""
	def __init__(self):
		super(Doctor, self).__init__()
		self.nbCredits  = 0
		self.nbZappeurs = 0
