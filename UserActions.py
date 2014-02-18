     
class Enum(object):
	"""docstring for Enum"""
	def __init__(self):
		super(Enum, self).__init__()
		self.lastId = 0
	def addId(self):
		self.lastId +=1
		return self.lastId
		
Enum = Enum()

class UserAction:
        """docstring for UserAction"""
        MOVE_N = Enum.addId()
        MOVE_S = Enum.addId()
        MOVE_E = Enum.addId()
        MOVE_W = Enum.addId()

        MOVE_NW = Enum.addId()
        MOVE_NE = Enum.addId()
        MOVE_SW = Enum.addId()
        MOVE_SE = Enum.addId()
        
        MOVE_NULL = Enum.addId()

        ZAP = Enum.addId()
        TELEPORT = Enum.addId()
