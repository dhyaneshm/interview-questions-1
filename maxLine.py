class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __str__(self):
        return "("+str(self.x)+"," + str(self.y)+")"
    def __repr__(self):
        return self.__str__()

EPSILON = 0.001
class Line:
    def __init__(self, p1, p2):
        if (p2.x-p1.x)==0:
            self.slope = "undefined"
            self.intercept = "undefined"
        else:
            self.slope = 1.0*(p2.y-p1.y)/(p2.x-p1.x)
            self.intercept = p1.y - p1.x*self.slope
        self.points = [p1,p2]
        
    def contains(self, p1):
        if (self.slope == "undefined"):
            if (p1.x == self.points[0].x):
                self.points.append(p1)
                return True
        elif (abs((p1.x*self.slope+self.intercept)-p1.y) < EPSILON):
            self.points.append(p1)
            return True
        return False
    def __str__(self):
        return str(self.points)
    def __repr__(self):
        return self.__str__()  
        
def makeFirstLine(points):
        ref = [points[0]]
        for p in points[1:]:
            ref.append(p)
            if not (p.x == ref[0].x and p.y==ref[0].y):
                firstLine = Line(ref[0], p)
                firstLine.points = ref
                return firstLine
        return None        
            
def maxPoints(points):
    if (len(points)<=2): return len(points)
    #take care of duplicate points
    lines = [makeFirstLine(points)]
    # print len(lines[0].points)
    if lines[0] == None:
        return len(points)
    #starting from the third point
    bestLine = lines[0]
    startIndex = len(bestLine.points)
    for p in points[startIndex:]:
        newLines = []
        for line in lines:
            if (line.contains(p)):
                if (len(line.points) > len(bestLine.points)):
                    #update the bestLine
                    bestLine = line
            else:
                for p2 in line.points:
                    newLines.append(Line(p,p2))
        lines += newLines
    return len(bestLine.points)

pointsArr = [(-4,-4),(-8,-582),(-3,3),(-9,-651),(9,591)]
points = [Point(elem[0], elem[1]) for elem in pointsArr]

print maxPoints(points)