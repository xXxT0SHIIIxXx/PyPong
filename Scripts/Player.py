import pygame
from pygame.locals import *

class Player:
  def __init__(self, screen, color, xPos, yPos, width, height, score):
    self.screen = screen
    self.color = color
    self.xPos = xPos
    self.yPos = yPos
    self.width = width
    self.height = height
    self.score = score
    self.rect = Rect(self.xPos, self.yPos, self.width, self.height)
    
  def Draw(self):
      self.rect = Rect(self.xPos, self.yPos, self.width, self.height)
      pygame.draw.rect(self.screen,self.color,self.rect)