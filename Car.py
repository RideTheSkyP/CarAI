import pygame
import math


class Car:
	def __init__(self):
		self.angle = 0
		self.speed = 5
		self.radars = []
		self.collisionPoints = []
		self.center = ()

		self.carSprite = pygame.image.load("sprites/Orange.png")
		self.carSprite = pygame.transform.scale(self.carSprite, (math.floor(self.carSprite.get_size()[0] / 2),
		                                                         math.floor(self.carSprite.get_size()[1] / 2)))
		self.car = self.carSprite
		self.carPosition = [650, 930]
		self.isAlive = True
		self.reachedGoal = False
		self.distance = 0
		self.time = 0

	def drawCar(self):
		pass

	def setCarCenterPosition(self):
		self.center = (self.carPosition[0] + (self.car.get_size() / 2),
		               self.carPosition[1] + (self.car.get_size()[1] / 2))

	def draw(self, screen):
		screen.blit(self.car, self.carPosition)
		self.drawRadars(screen)

	def drawCenter(self, screen):
		pygame.draw.circle(screen, (0, 0, 255), (math.floor(self.center[0]), math.floor(self.center[1])), 5)

	def drawRadars(self, screen):
		for radar in self.radars:
			p, _ = radar
			pygame.draw.line(screen, (0, 255, 0), self.center, p, 1)
			pygame.draw.circle(screen, (0, 255, 0), p, 5)
