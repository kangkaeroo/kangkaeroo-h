import sfml
from GameState import GameState
from Ingame import InGame

class MainMenu(GameState) :
  def __init__(self, iGame) :
    super().__init__(iGame)
    self.CurrSelectorPos = 0
    self.Screen.size = (self.Game.Window.size)
    self.Screen.center = (self.Game.Window.size * 0.5)
    self.SelectorMenuPositions = [sfml.Vector2(180,225), sfml.Vector2(180,275)]
    
    self.TitleText = sfml.Text("Steven Universe", self.Game.AssetManager.Fonts["Crewniverse"], 70)
    self.TitleText.position = (0,0)
    self.TitleText.color = sfml.Color.WHITE
    
    self.SubTitleText = sfml.Text("Danmaku", self.Game.AssetManager.Fonts["Crewniverse"], 45)
    self.SubTitleText.position = (37,80)
    self.SubTitleText.color = sfml.Color.WHITE
    
    self.StartText = sfml.Text("Start Game", self.Game.AssetManager.Fonts["Crewniverse"], 40)
    self.StartText.position = (200,200)
    self.StartText.color = sfml.Color.WHITE
    
    self.QuitText = sfml.Text("Quit", self.Game.AssetManager.Fonts["Crewniverse"], 40)
    self.QuitText.position = (200,250)
    self.QuitText.color = sfml.Color.WHITE
    
    self.Selector = self.Game.AssetManager.GetBullet("Default_Purple")
    self.Selector.position = self.SelectorMenuPositions[0]
    
    self.ObjectList = []
    self.ObjectList.append(self.TitleText)
    self.ObjectList.append(self.SubTitleText)
    self.ObjectList.append(self.StartText)
    self.ObjectList.append(self.QuitText)
    self.ObjectList.append(self.Selector)
    
  def Draw(self) :
    self.Game.Window.view = self.Screen
    self.Game.Window.clear(sfml.Color.BLACK)
    for Obj in self.ObjectList :
      self.Game.Window.draw(Obj)
    
  def HandleInputs(self) :
    for event in self.Game.Window.events :
      if type(event) is sfml.CloseEvent :
        self.Game.Window.close()
        exit(0)
      if type(event) is sfml.KeyEvent and event.pressed :
        if event.code is sfml.Keyboard.Z :
          if self.CurrSelectorPos is 0 :
            self.Game.PopState()
            self.Game.PushState(InGame(self.Game))
            self.Game.GUI.Visible = True
          elif self.CurrSelectorPos is 1 :
            self.Game.Window.close()
            exit(0)
        elif event.code is sfml.Keyboard.UP :
          self.CurrSelectorPos = (self.CurrSelectorPos - 1) % len(self.SelectorMenuPositions)
          self.Selector.position = self.SelectorMenuPositions[self.CurrSelectorPos]
        elif event.code is sfml.Keyboard.DOWN :
          self.CurrSelectorPos = (self.CurrSelectorPos + 1) % len(self.SelectorMenuPositions)
          self.Selector.position = self.SelectorMenuPositions[self.CurrSelectorPos]
