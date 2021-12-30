import sfml

GUI_TEXT_POS = (600,200)

GUI_COLOUR = sfml.Color(20,20,20)
GUI_TOP_BORDER = 30
GUI_LEFT_BORDER = 30
GUI_RIGHT_BORDER = 530
GUI_BOTTOM_BORDER = 580

GUI_LIFE_FONT_SIZE = 20
GUI_BOMB_FONT_SIZE = 20
GUI_SCORETITLE_FONT_SIZE = 20
GUI_SCORE_FONT_SIZE = 12

GUI_LIFE_TEXT_POS = (0,0)
GUI_BOMB_TEXT_POS = (0,40)
GUI_SCORE_TEXT_POS = (0,80)
GUI_SCORE_NUM_POS = (0, 110)

GUI_LIFE_DISTANCE_BET = 12
GUI_BOMB_DISTANCE_BET = 12

GUI_LIFE_DISTANCE_TEXT = 30
GUI_BOMB_DISTANCE_TEXT = 30

LifeSize = (9,9)
BombSize = (9,9)

class GUI (sfml.TransformableDrawable) :
  def __init__(self, iGame, visible = False) :
    sfml.Drawable.__init__(self)
    self.Game = iGame
    #self.Screen = sfml.View()
    #self.Screen.size = self.Game.Window.size
    #self.Screen.center = self.Game.Window.size * 0.5
    #self.Screen.move(self.Game.Window.size.x * -0.75, self.Game.Window.size.y * -0.30)
    self.Visible = visible
    self.TextPosition = GUI_TEXT_POS
    self.ObjectList = []
    self.LifeList = []
    self.BombList = []
    self.Borders = []
    
    BackgroundTop = sfml.RectangleShape((self.Game.Window.size.x, GUI_TOP_BORDER))
    BackgroundTop.fill_color = GUI_COLOUR
    self.Borders.append(BackgroundTop)
    BackgroundLeft = sfml.RectangleShape((GUI_LEFT_BORDER, self.Game.Window.size.y))
    BackgroundLeft.fill_color = GUI_COLOUR
    self.Borders.append(BackgroundLeft)
    BackgroundRight = sfml.RectangleShape((self.Game.Window.size.x - GUI_RIGHT_BORDER, self.Game.Window.size.y))
    BackgroundRight.fill_color = GUI_COLOUR
    BackgroundRight.position = (GUI_RIGHT_BORDER,0)
    self.Borders.append(BackgroundRight)
    BackgroundTop = sfml.RectangleShape((self.Game.Window.size.x ,self.Game.Window.size.y - GUI_BOTTOM_BORDER))
    BackgroundTop.fill_color = GUI_COLOUR
    BackgroundTop.position = (0, GUI_BOTTOM_BORDER)
    self.Borders.append(BackgroundTop)
    
    LifeText = sfml.Text("Life", self.Game.AssetManager.Fonts["Crewniverse"], GUI_LIFE_FONT_SIZE)
    LifeText.position = GUI_LIFE_TEXT_POS
    LifeText.color = sfml.Color.WHITE
    self.ObjectList.append(LifeText)
    
    BombText = sfml.Text("Bomb", self.Game.AssetManager.Fonts["Crewniverse"], GUI_BOMB_FONT_SIZE)
    BombText.position = GUI_BOMB_TEXT_POS
    BombText.color = sfml.Color.WHITE
    self.ObjectList.append(BombText)
    
    ScoreText = sfml.Text("Score", self.Game.AssetManager.Fonts["Crewniverse"], GUI_SCORETITLE_FONT_SIZE)
    ScoreText.position = GUI_SCORE_TEXT_POS
    ScoreText.color = sfml.Color.WHITE
    self.ObjectList.append(ScoreText)
    
    ScoreNum =  sfml.Text("0123456789", self.Game.AssetManager.Fonts["Atari"], GUI_SCORE_FONT_SIZE)
    ScoreNum.position = (ScoreText.local_bounds.center.x - ScoreNum.local_bounds.width / 2 ,GUI_SCORE_NUM_POS[1])
    ScoreNum.color = sfml.Color.WHITE
    self.ObjectList.append(ScoreNum)
    
    for i in range(2) :
      Life = self.Game.AssetManager.GetBullet("Default_Violet")
      Life.position = (LifeText.position.x + i * GUI_LIFE_DISTANCE_BET, LifeText.position.y + GUI_LIFE_DISTANCE_TEXT)
      self.LifeList.append(Life)
      
    for i in range(3) :
      Bomb = self.Game.AssetManager.GetBullet("Default_Violet")
      Bomb.position = (BombText.position.x + i * GUI_BOMB_DISTANCE_BET, BombText.position.y + GUI_BOMB_DISTANCE_TEXT)
      self.BombList.append(Bomb)
      
      
  def draw(self, target, states) :
    if self.Visible is False :
      return
    #self.Game.Window.view = self.Screen
    for Background in self.Borders :
      target.draw(Background, states)
    for Obj in self.ObjectList :
      Obj.position = Obj.position + self.TextPosition
      target.draw(Obj, states)
      Obj.position = Obj.position - self.TextPosition
    for Life in self.LifeList :
      Life.position = Life.position + self.TextPosition
      target.draw(Life, states)
      Life.position = Life.position - self.TextPosition
    for Bomb in self.BombList :
      Bomb.position = Bomb.position + self.TextPosition
      target.draw(Bomb, states)
      Bomb.position = Bomb.position - self.TextPosition
    
  def Draw(self) :
    if self.Visible is False :
      return
    #self.Game.Window.view = self.Screen
    for Obj in self.ObjectList :
      self.Game.Window.draw(Obj)
    for Life in self.LifeList :
      self.Game.Window.draw(Life)
    for Bomb in self.BombList :
      self.Game.Window.draw(Bomb)
  
  def UpdateLife(self, Change) :
    pass
  
  def UpdateBomb(self, Change) :
    pass
  
  def UpdateScore(self, Change) :
    pass
  
    
    