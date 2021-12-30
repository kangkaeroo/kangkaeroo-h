import os
import sys
import sfml
import math
from Game import Game
from MainMenu import MainMenu



screenSizeX = 350/640
screenSizeY = 400/480


ArtFileNames = ["Gems.png", "Humans.png", "Peridot.png", "ShotsNegative.png ", "Shots.png"]
PeridotIdleRectangle = sfml.Rectangle((200, 4), (61, 116))
PeridotSpellRectangle = sfml.Rectangle((269, 4), (68, 116))
StevenRectangle = sfml.Rectangle((94, 42), (50,86))

      
def HandleEventsGame(Win) :
  global CState
  global OnScreenObjs
  for event in Win.events :
    if type(event) is sfml.CloseEvent :
      Win.close()
      exit(0)
    if type(event) is sfml.KeyEvent :
      if sfml.Keyboard.is_key_pressed(sfml.Keyboard.Z) :
        pass
      if sfml.Keyboard.is_key_pressed(sfml.Keyboard.L_SHIFT) :
        pass
      if sfml.Keyboard.is_key_pressed(sfml.Keyboard.UP) :
        OnScreenObjs[0].move((0,-4))
      if sfml.Keyboard.is_key_pressed(sfml.Keyboard.DOWN) :
        OnScreenObjs[0].move((0,4))
      if sfml.Keyboard.is_key_pressed(sfml.Keyboard.LEFT) :
        OnScreenObjs[0].move((-4,0))
      if sfml.Keyboard.is_key_pressed(sfml.Keyboard.RIGHT) :
        OnScreenObjs[0].move((4,0))

def main(argv) :
  iGame = Game()
  iGame.PushState(MainMenu(iGame))
  iGame.GameLoop()
  
  return 0

  

if __name__ == "__main__" :
  main(sys.argv)