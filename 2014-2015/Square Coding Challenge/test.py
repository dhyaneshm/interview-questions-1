#helper method to update state
def updateState(newPos, state):
  newState = dict(state)
  newState["s"] = newPos
  return newState


# f = open("input000.txt", 'r')
class squirrelProblem:
  def startState(self):
    state = {}
    s_str = raw_input()
    sPos = (int(s_str.split()[0]),int(s_str.split()[1]))
    t_str = raw_input()
    tPos = (int(t_str.split()[0]),int(t_str.split()[1]))
    nuts = []
    num_nuts = int(raw_input())
    for i in range(num_nuts):
      pos_str = raw_input()
      xPos = int(pos_str.split()[0])
      yPos = int(pos_str.split()[1])
      nuts.append((xPos,yPos))
    state["nuts"] = nuts
    state["s"] = sPos
    state["t"] = tPos
    state["moves"] = 0
    return state

  def isGoal(self, state):
    return (len(state["nuts"])==0 and state["s"]==state["t"])

  #returns list of valid positions for the squirrel in that order
  def move(self, state):
    #check nuts
    if (state["s"] in state["nuts"]):
      state["nuts"].remove(state["s"])
    moves = []
    sPos = state["s"]
    #up down left right
    if (sPos[1] > 0):
      moves.append(updateState((sPos[0], sPos[1]-1), state))
    moves.append(updateState((sPos[0], sPos[1]+1), state))
    if (sPos[0] > 0):
      moves.append(updateState((sPos[0]-1, sPos[1]), state))
    moves.append(updateState((sPos[0]+1, sPos[1]), state))
    return moves

def dynamicProgramming(problem):
  # cache= {} # state -> futureCost, action, newState, cost
  def recurse(state):
      #base case
    if problem.isGoal(state):
      return 0
    # if state not in cache:
    #   cache[state] = 
    best = min((1+recurse(move), move) for move in problem.move(state))
    return best[0]
  totalCost = recurse(problem.startState())
  return totalCost

problem = squirrelProblem()
print dynamicProgramming(problem)



