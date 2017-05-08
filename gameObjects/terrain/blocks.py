import terrain_block


class dirt(terrain_block.block):
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY

		self.textureDir = "./textures/terrain/dirt_terain_block.png"
	