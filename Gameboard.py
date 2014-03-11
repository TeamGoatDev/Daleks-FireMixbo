 #!/usr/bin/python
 # -*- coding: utf-8 -*-
class Gameboard(object):
	"""Manages the map"""
	x = 0
	y = 0
	def __init__(self, x,y):
		self.x = x
		self.y = y