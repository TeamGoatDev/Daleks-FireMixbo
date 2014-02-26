from Position import Position


class GameObject(object):
        """docstring for GameObject"""
        def __init__(self):
                super(GameObject, self).__init__()
                self.position = Position(0,0)
                

class Dalek(GameObject):
        """docstring for Dalek"""
        def __init__(self):
                super(Dalek, self).__init__()

        def move(self, docPos):
                if docPos.x > self.position.x:
                        self.position.x += 1
                if docPos.x < self.position.x:
                        self.position.x += -1

                if docPos.y > self.position.y:
                        self.position.y += 1
                if docPos.y < self.position.y:
                        self.position.y += -1

                      
                

class ScrapHeap(GameObject):
        """docstring for ScrapHeap"""
        def __init__(self):
                super(ScrapHeap, self).__init__()

class Doctor(GameObject):
        """docstring for Doctor"""
        def __init__(self):
                super(Doctor, self).__init__()
                self.nbPoints  = 0
                self.nbZappeurs = 0
