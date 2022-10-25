from random import randint
import random
import pygame
from Player import *
from Ball import *
import pygame.freetype

#Initalize Mixer and Set Vars
pygame.mixer.init()
hitSound = pygame.mixer.Sound("audio/hit.wav")
goalSound = pygame.mixer.Sound("audio/goal.wav")

elapsedTime = 0
desiredTime = 0

BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
SPEED = 5
ANGLE = -1
GREY = (50,50,50)
width, height = 640, 480

class Game:
  def __init__(self):
    self.screen = pygame.display.set_mode((width, height))
    self.P1 = Player(self.screen, BLUE, 0, height/2, 20,60,0)
    self.CPU = Player(self.screen, RED, width-20, height/2, 20,60,0)
    self.BALL = Ball(self.screen,WHITE,width/2,height/2,5,5)
    self.level = 1
    self.elapsedTime = 0
    self.desiredTime = 0

  def CheckKeys(self):
    x, y = self.screen.get_size()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]: #Move up
        if self.P1.yPos > 60:
            self.P1.yPos = self.P1.yPos - SPEED

    if keys[pygame.K_DOWN]: #Move Down
        if self.P1.yPos + 60 < y:
            self.P1.yPos = self.P1.yPos + SPEED

  def DrawScore(self):
      x, y = self.screen.get_size()
      GAME_FONT = pygame.freetype.Font("fonts/Gummy Bears.ttf", 30)
      pygame.draw.rect(self.screen, BLACK, pygame.Rect(0, 0, x, 60))
      GAME_FONT.render_to(self.screen, (10, 30), str(self.P1.score), WHITE)
      GAME_FONT.render_to(self.screen, (x-50, 30), str(self.CPU.score), WHITE)
      pygame.draw.rect(self.screen, GREY, pygame.Rect(0, 60, x, 3))

  def CPUAI(self):
      #CPU AI controls at MASTER Level
      if self.level == 3:
          if self.CPU.yPos+30 < self.BALL.yPos and abs(self.CPU.yPos - self.BALL.yPos) > 3:
              self.CPU.yPos = self.CPU.yPos + 5
          elif self.CPU.yPos+30 > self.BALL.yPos and abs(self.CPU.yPos - self.BALL.yPos) > 3:
              self.CPU.yPos = self.CPU.yPos - 5
              
      #CPU AI controls at HARD Level   
      if self.level == 2:
          if self.CPU.yPos+30 < self.BALL.yPos and abs(self.CPU.yPos - self.BALL.yPos) > 5:
              self.CPU.yPos = self.CPU.yPos + 3
          elif self.CPU.yPos+30 > self.BALL.yPos and abs(self.CPU.yPos - self.BALL.yPos) > 5:
              self.CPU.yPos = self.CPU.yPos - 3
              
      #CPU AI controls at EASY Level   
      if self.level == 1:
          if self.CPU.yPos+30 < self.BALL.yPos and abs(self.CPU.yPos - self.BALL.yPos) > 10:
              self.CPU.yPos = self.CPU.yPos + 2
          elif self.CPU.yPos+30 > self.BALL.yPos and abs(self.CPU.yPos - self.BALL.yPos) > 10:
              self.CPU.yPos = self.CPU.yPos - 2
  
  def Draw(self):
    self.P1.Draw() 
    self.CPU.Draw() 
    self.BALL.Draw() 
  
  def TrackCollision(self):
     x, y = self.screen.get_size()
     #track collision between ball and players
     collide = pygame.Rect.colliderect(self.P1.rect, self.BALL.rect)
     collide2 = pygame.Rect.colliderect(self.CPU.rect, self.BALL.rect)
     
     if collide: #if ball hits player
         self.BALL.xSpeed = -SPEED
         k = random.randint(-5, 5)
         self.BALL.ySpeed = k
         pygame.mixer.Sound.play(hitSound)
     elif collide2: #if ball hits CPU/Player2
         self.BALL.xSpeed = SPEED
         k = random.randint(-1, 1)
         self.BALL.ySpeed = k
         pygame.mixer.Sound.play(hitSound)
         
     if self.BALL.yPos >= y: #if ball hits Floor
         self.BALL.ySpeed = 1
         pygame.mixer.Sound.play(hitSound)
     elif self.BALL.yPos <= 60: #if ball hits Ceiling
         self.BALL.ySpeed = -1
         pygame.mixer.Sound.play(hitSound)
      
  def TrackScore(self):
    x, y = self.screen.get_size()
    
    if self.BALL.xPos < 0: #Give CPU Score and reset ball
        self.CPU.score = self.CPU.score + 1
        pygame.mixer.Sound.play(goalSound)
        self.ResetGame()
        print('P1: ' + str(self.P1.score) + '| CPU: ' + str(self.CPU.score))
    elif self.BALL.xPos > x: #Give Player Score and reset ball
        self.P1.score = self.P1.score + 1
        pygame.mixer.Sound.play(goalSound)
        self.ResetGame()
        print('P1: ' + str(self.P1.score) + '| CPU: ' + str(self.CPU.score))
      
      
  def ResetGame(self):
    #Get Screen Size
    x, y = self.screen.get_size()
    
    #Set ball to middle of screen
    self.BALL.xPos = x/2
    self.BALL.yPos = y/2
    
    #Set Random Y Velocity
    k = random.randint(-1, 1)
    self.BALL.ySpeed = k