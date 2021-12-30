import sfml

class GameState :
  def __init__(self, iGame) :
    self.Screen = sfml.View()
    self.Game = iGame
  def Draw(self) :
    pass
  def Update(self, dt) :
    pass
  def HandleInputs(self) :
    pass