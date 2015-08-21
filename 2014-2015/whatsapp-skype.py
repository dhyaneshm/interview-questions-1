# takes an array, and two parameters (thresholds of euclidian and angle)
import random

# this function takes a list of (x,y) tuples and two thresholds for euclidean distance and the difference in slopes
# it will return a list of "simplified" points that uses the thresholds to simplify the array

def simplify_points(pts, distance_threshold, slope_threshold):
  if len(pts)<2: return pts
  prev_x, prev_y = pts[0]
  prev_slope = None
  simplified = [pts[0]]
  for i in range(1, len(pts)-1):
    cur_x, cur_y = pts[i]
    distance = (cur_y-prev_y)**2+(cur_x-prev_x)**2
    cur_slope = float((cur_y-prev_y)/(cur_x-prev_x)) if (cur_x-prev_x) != 0 else 0
    slope = cur_slope if prev_slope == None else cur_slope - prev_slope
    # if we fail either of our thresholds
    if distance > distance_threshold**2 and abs(slope)>slope_threshold:
      simplified.append(pts[i])
      prev_slope = cur_slope
    prev_x = cur_x
    prev_y = cur_y
  simplified.append(pts[len(pts)-1])
  return simplified

print "Testing generic case"
original_list = [(0,0), (2,2), (4,4), (4,8), (5,7), (5,8)]
print original_list
print simplify_points(original_list, 10000, 0)

print "Testing edge case with one element"
original_list = [(0,0)]
print original_list
print simplify_points(original_list, 2, 0.03)

print "Testing randomly generated case"
original_list = []
for i in range(20):
  original_list.append((random.randint(0,100), random.randint(0,100)))
print original_list
print simplify_points(original_list, 2, 0.03)

print "Testing randomly generated stress case"
original_list = []
for i in range(100):
  original_list.append((random.randint(0,100), random.randint(0,100)))
print original_list
print simplify_points(original_list, 2, 0.03)