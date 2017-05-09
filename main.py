from pygameapp import App
import sys
import gameObjects.terrain.blocks as blocks
import numpy as np

terrain_objects = None
playerPos = [0,0]
playerSpeed = [0,0]
class main(App):

	def generateTerrain(self,sizeW,sizeH):
		objectList = np.empty((sizeW,sizeH),dtype=object)
		switch = True
		for i in range(0,sizeW):
			switch = not switch
			for j in range(0,sizeH):
				switch = not switch
				if switch:
					objectList[i][j] = blocks.dirt(i,j)
				else:
					objectList[i][j] = blocks.stone(i,j)
		return objectList
	def drawTerrain(self,objects):
		global playerPos
		size = list(objects.shape)
		for i in range(0,size[0]):
			for j in range(0,size[1]):
				#print(dir(objects[i][j]))
				scale = 4
				image = self.pygame.image.load(objects[i][j].textureDir)
				image = self.pygame.transform.scale(image,(32*scale,32*scale))
				self.display.blit(image,((i*(32*scale))+playerPos[0]*scale,(j*(32*scale))+playerPos[1]*scale))
				self.pygame.draw.rect(self.display,(255,255,255),((self.getWindowWidth()-50)/2,(self.getWindowHeight()-50)/2,100,100))
	def movePlayer(self):
		global playerPos
		playerPos[0] += playerSpeed[0]
		playerPos[1] += playerSpeed[1]

	def onKeyDown(self,key):
		global playerSpeed
		if key == self.pygame.K_w:
			playerSpeed[1] = 1
		if key == self.pygame.K_s:
			playerSpeed[1] = -1
		if key == self.pygame.K_a:
			playerSpeed[0] = 1
		if key == self.pygame.K_d:
			playerSpeed[0] = -1
	def onKeyUp(self,key):
		global playerSpeed
		if key == self.pygame.K_w:
			playerSpeed[1] = 0
		if key == self.pygame.K_s:
			playerSpeed[1] = 0
		if key == self.pygame.K_d:
			playerSpeed[0] = 0
		if key == self.pygame.K_a:
			playerSpeed[0] = 0
	def onStart(self):
		global terrain_objects
		terrain_objects = self.generateTerrain(10,10)
		
	def onExecute(self):
		global terrain_objects
		self.drawTerrain(terrain_objects)
		self.movePlayer()
main(500,500,30).start()