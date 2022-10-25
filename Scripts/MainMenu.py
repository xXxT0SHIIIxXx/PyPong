import pygame_menu
import pygame
from Game import*
import sys

# Variables
width, height = 640, 480
Game = Game()
fps = 60
fpsClock = pygame.time.Clock()

THEME = pygame_menu.themes.THEME_DARK
#Other Themes v
#Default = pygame_menu.themes.THEME_DEFAULT
#Blue = pygame_menu.themes.THEME_BLUE
#Green = pygame_menu.themes.THEME_GREEN
#Orange = pygame_menu.themes.THEME_ORANGE
#Solarized = pygame_menu.themes.THEME_SOLARIZED

def set_difficulty(value, difficulty):
    Game.level = difficulty
    pass

def start_the_game():
    # Game loop.
    while True:
      Game.screen.fill((0, 0, 0))
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      # Update.
      Game.CheckKeys()
      Game.CPUAI()
      Game.TrackCollision()
      Game.TrackScore()  
      # Draw.
      Game.Draw()
      Game.DrawScore()
      #END
      pygame.display.flip()
      fpsClock.tick(fps)
    pass

class MainMenu:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((width, height))
    menu = pygame_menu.Menu('Welcome', width, height,theme=THEME)
    menu.add.text_input('Name :', default='John Doe')
    menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2), ('Master', 3)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(self.screen)