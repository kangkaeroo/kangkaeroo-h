import sfml
from Entity import Entity

class Bullet (Entity) :
  def __init__(self, Start, Sprite, CollisionRadius) :
    super().__init__(Start, Sprite, CollisionRadius)
  
    
class BulletPatter :
  def __init__ (self) :
    self.BulletList = []
    
    