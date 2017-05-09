import terrain_block
import settings


class dirt(terrain_block.block):
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY
	
		self.textureDir = settings.DEFINITIONS_ROOT+"/textures/terrain/dirt_terrain_block.png"
class stone(terrain_block.block):
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY
	
		self.textureDir = settings.DEFINITIONS_ROOT+"/textures/terrain/stone_terrain_block.png"