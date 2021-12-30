import os
import sfml
from AnimationHandler import AnimationHandler
from ArtManager import ArtManager
from GUI import GUI


CTitle = "Steven Universe Danmaku"

class Game :
  def __init__(self) :
    self.States = []
    self.Window = sfml.RenderWindow(sfml.VideoMode(800,600), CTitle)
    self.Window.framerate_limit = 60
    self.Window.mouse_cursor_visible = False
    self.AssetManager = ArtManager()
    os.chdir("..") #only when script is in src
    os.chdir("res/")
    self.LoadFonts()
    self.LoadTextures()
    self.LoadSprites()
    os.chdir("..")
    self.GUI = GUI(self)
    
  def PushState(self, newState) :
    self.States.append(newState)
    
  def PopState(self) :
    self.States.pop()
    
  def ChangeState(self, newState) :
    if len(self.States) is not 0 :
      self.PopState()
    self.PushState(newState)
    
  def PeekState(self) :
    if len(self.States) is 0 :
      return None
    return self.States[-1]
  
  def GameLoop(self) :
    self.Clock = sfml.Clock()
    while self.Window.is_open :
      dt = (self.Clock.elapsed_time).seconds
      if self.PeekState() is None :
        continue
      self.PeekState().HandleInputs()
      self.PeekState().Update(dt)
      self.Window.clear(sfml.Color.BLACK)
      self.PeekState().Draw()
      self.Window.draw(self.GUI)
      self.Window.display()
      self.Window.view = self.Window.default_view
      
  def LoadFonts(self) :
    self.AssetManager.LoadFont("Crewniverse", "crewniverse_font.ttf")
    self.AssetManager.LoadFont("Cirno", "Cirno.ttf")
    self.AssetManager.LoadFont("Atari", "atari.tff")
    
  def LoadTextures(self) :
    self.AssetManager.LoadTexture("Gems", "Gems.png")
    self.AssetManager.LoadTexture("Humans", "Humans.png")
    self.AssetManager.LoadTexture("Peridot", "Peridot.png")
    self.AssetManager.LoadTexture("Shots(Negative)", "ShotsNegative.png")
    self.AssetManager.LoadTexture("Shots", "Shots.png")
    
  def LoadSprites(self) :
    self.AssetManager.LoadBullets()
    self.AssetManager.LoadSprites()