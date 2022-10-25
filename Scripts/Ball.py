import pygame
from pygame.locals import *
from Game import *

class Ball:
  def __init__(self,screen,color,xPos,yPos,r,w):
    self.screen = screen 
    self.color = color
    self.xPos = xPos
    self.yPos = yPos
    self.r = r
    self.w = w
    self.xSpeed = 5
    self.ySpeed = -1
    self.rect = Rect(self.xPos, self.yPos, self.r, self.w)

  def Draw(self):
      self.rect = Rect(self.xPos, self.yPos, self.r, self.w) 
      pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos, self.r, self.w))
      self.xPos = self.xPos - self.xSpeed #Move Ball on X Axis
      self.yPos = self.yPos - self.ySpeed #Move Ball on Y Axis