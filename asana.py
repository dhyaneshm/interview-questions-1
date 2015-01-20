# Deltas for directions: [east, south, west, north]
# 0 = east, 1 = south, etc...
DELTAS = [(0,1), (1,0), (0,-1), (-1,0)]

def inBounds(pos, matrix):
  i, j = pos
  return i<len(matrix) and i>-1 and j<len(matrix[0]) and j>-1

# Maybe somebody from Stanford @Asana will know why it's called Karel!
class SpiralKarel:
  def __init__(self, matrix, start, direction, fn):
    self.matrix = matrix
    self.pos = start
    self.direction = direction
    self.dx, self.dy = DELTAS[self.direction]
    self.fn = fn
    self.visited = set()
    self.turned = False
  
  def turn(self):
    self.direction = (self.direction+1)%len(DELTAS)
    self.dx, self.dy = DELTAS[self.direction]
    self.turned = True

  # Helper function to retrieve the anticipated position
  def getNextPos(self):
    return (self.pos[0]+self.dx, self.pos[1]+self.dy)

  def hasNext(self):
    newPos = self.getNextPos()
    if inBounds(newPos, self.matrix) and newPos not in self.visited:
      self.turned = False
      return True
    # edge case here to prevent infinite looping
    elif self.turned:
      return False
    else:
      self.turn()
      return self.hasNext()  

  def next(self):
    self.visited.add(self.pos)
    self.pos = self.getNextPos()

  def doAction(self):
    i, j = self.pos
    # calls the given function on the matrix's element
    self.fn(self.matrix[i][j])

# To run, put your matrix here and then allow Karel to do his magic
matrix = [[1],[2]]

def callback(elem):
  print elem
karel = SpiralKarel(matrix, (0,0), 0, callback)
while karel.hasNext():
  karel.doAction()
  karel.next()
if inBounds(karel.pos, matrix): karel.doAction()