import sfml

class Animation :
  def __init__(self, startFrame, endFrame, duration) :
    self.Start = startFrame
    self.End = endFrame
    self.Duration = duration
  def length(self) :
    return self.End - self.Start + 1
               
class AnimationHandler :
  #def __init__(self) :
    #self.AnimationList = []
    #self.ElapsedTime = 0
    #self.CurrAnimation = None
    #self.FrameSize = None
    #self.Bounds = None
    
  def __init__(self, frameSize) :
    self.AnimationList = []
    self.ElapsedTime = 0
    self.CurrAnimation = None
    self.FrameSize = frameSize
    self.Bounds = sfml.Rectangle((0,0),self.FrameSize)
    
  def AddAnimation(self, newAnim) :
    self.AnimationList.append(newAnim)
    
  def Update(self, dt) :
    if self.CurrAnimation is None or self.CurrAnimation >= len(self.AnimationList) or self.CurrAnimation < 0:
      return
    currDuration = self.AnimationList[CurrAnimation].duration
    if math.floor((self.ElapsedTime + dt) / currDuration) > math.floor(self.ElapsedTime / currDuration) :
      newFrame = math.floor((self.ElapsedTime + dt) / currDuration) % self.AnimationList[CurrAnimation].length()
      newBounds = self.frameSize
      newBounds.left = newBounds.width * newFrame
      newBounds.top = newBounds.height * self.CurrAnimation
      self.Bounds = newBounds
    self.ElapsedTime = self.ElapsedTime + dt
    while self.ElapsedTime > currDuration * self.AnimationList[CurrAnimation].length() :
      self.ElapsedTime = self.ElapsedTime - currDuration * self.AnimationList[CurrAnimation].length() 
      
  def ChangeAnim(self, AnimIndex) :
    if AnimIndex is self.CurrAnimation or AnimIndex < 0 or AnimIndex >= len(self.AnimationList) :
      return
    self.CurrAnimation = AnimIndex
    newBounds = self.frameSize
    newBounds.top = newBounds.height * AnimIndex
    self.Bounds = newBounds
    self.ElapsedTime = 0
  