import sfml
from AnimationHandler import AnimationHandler

class Player (sfml.TransformableDrawable) :
  def __init__(self, Sprite, HitBoxSprite, Offset = (0,0)) :
    self.Sprite = Sprite
    self.HitBoxSprite = HitBoxSprite
    self.x = 100
    self.y = 400
    self.Sprite.origin = (self.Sprite.local_bounds.right / 2, self.Sprite.local_bounds.bottom / 2)
    self.HitBoxSprite.origin = (self.HitBoxSprite.local_bounds.right / 2, self.HitBoxSprite.local_bounds.bottom / 2)
    self.Sprite.position = sfml.Vector2(self.x, self.y) + Offset
    self.HitBoxSprite.position = sfml.Vector2(self.x, self.y) + Offset #+ sfml.Vector2(-18, 40)
    self.CollisionRadius = 4
    self.Focus = False
    self.Offset = Offset
    
  def draw(self, target, states) :
    target.draw(self.Sprite)
    if self.Focus is True :
      target.draw(self.HitBoxSprite)
      
  def Move(self, iX, iY) :
    self.x = self.x + iX
    self.y = self.y + iY
    self.Sprite.position = self.Sprite.position + (iX, iY)
    self.HitBoxSprite.position = self.HitBoxSprite.position + (iX, iY)
  
  def MoveTo(self, Vector) :
    self.MoveCoorTo(Vector[0], Vector[1])
    
  def MoveCoorTo(self, iX, iY) :
    self.x = iX
    self.y = iY
    self.Sprite.position = sfml.Vector2(self.x, self.y) + self.Offset
    self.HitBoxSprite.position = sfml.Vector2(self.x, self.y) + self.Offset
    
