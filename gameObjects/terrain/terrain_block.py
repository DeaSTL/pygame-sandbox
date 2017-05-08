class block(object):
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY

		self.textureDir = "textures/terrain/default_terain_block.png"
	def initialization(self):
		pass
	def getX(self): #XDDDDDDDDDDDDDDDDDDDD
		return self.positionX
	def getY(self):
		return self.positionY
	def getTexture(self):
		return self.textureDir