import sfml
from Nutilities import SpriteCopy

DanTextureStart = 1
DanTextureOffset = 9

class ArtManager :
  def __init__(self) :
    self.Textures = {}
    self.Fonts = {}
    self.Sprites = {}
    self.BulletSprites = {}
  
  def LoadTexture(self, textureName, fileName) :
    try :
      self.Textures[textureName] = sfml.Texture.from_file(fileName)
    except IOError: 
      print("Error loading texture: ", textureName, " from file ", fileName)
  
  def LoadFont(self, fontName, fileName) :
    try :
      self.Fonts[fontName] = sfml.Font.from_file(fileName)
    except IOError: 
      print("Error loading font: ", fontName, " from file ", fileName)
  
  def LoadBullets(self) :
    BulletColorOrder = ["Red", "Orange", "Gold", "Yellow", "Green", "Cyan", "Teal", "Blue", "Purple", "Violet", "Black", "White"]
    for i in range(12) :
      self.BulletSprites["Default_" + BulletColorOrder[i]] = sfml.Sprite(self.Textures["Shots(Negative)"], sfml.Rectangle((DanTextureStart + DanTextureOffset * i, DanTextureStart), (DanTextureOffset, DanTextureOffset)))
  
  def GetBullet(self, name) :
    if name not in self.BulletSprites :
      return None
    return SpriteCopy(self.BulletSprites[name])
  
  def LoadSprites(self) :
    self.Sprites["Steven"] = sfml.Sprite(self.Textures["Humans"], sfml.Rectangle((94, 42), (50,86)) )
  
  def GetSprite(self, name) :
    if name not in self.Sprites :
      return None
    return SpriteCopy(self.Sprites[name])