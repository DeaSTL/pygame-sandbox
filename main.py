from pygameapp import App
import sys
import gameObjects.terrain.blocks as blocks
import numpy as np

terrain_objects = None
class main(App):
	def generateTerrain(self,sizeW,sizeH):
		objectList = np.empty((sizeW+1,sizeH+1),dtype=object)
		for i in range(0,sizeW):
			for j in range(0,sizeH):
				objectList[i][j] = blocks.dirt(i,j)
				#pass
		return objectList
	def drawTerrain(self,objects):
		size = list(objects.shape)
		for i in range(0,size[0]):
			for j in range(0,size[1]):
				image = self.pygame.image.load(objects[i][j].getTexture())
				self.display.blit(image,(i*32,j*32))				
	def onStart(self):
		global terrain_objects
		terrain_objects = self.generateTerrain(100,100)
		
	def onExecute(self):
		global terrain_objects
		self.drawTerrain(terrain_objects)
main(500,500,30).start()