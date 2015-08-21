# Matt Faus - backend storage engineer at Microsoft (outlook)
# Storage infrastructure to store/retrieve emails
# Current work at Khan: Infrastructure team
# Before: on data science team (automate parameter training)

# Large vs. Small and Profit vs. Non-profit
# Big->Small is what he wanted, old product (codebase was 15 years old - data was not malleable). Deploy cycle was order of months (3-4 chances/year for production). Lot of QA and maintenance things.
# Meeting schedule and work/time flexibility is easier (coordination is easier)
# Compensation standpoint: Stock option was pretty stable at Microsoft. Raw compensation is about the same as just cash. Non-profit in a capital sense, but social capital is for-profit (grabbing that market share!)

# What is important?
# Personalized learning experience (different paths through concepts). Guiding students through content tailored to their needs, some success -> lots more work to be done. More than time, it takes research time to understand how we can measure learning and figure out where the student is and where they need to go. Technology required to implement these experiments (trying different recommendation systems out) and the analysis component (what's working? what's not)

# Khan Academy Interview - 10/24 3:30pm

# High-level approach: 

# newPoint = point_stream.pop(0)
# point_
# euclidian distance
# If there's len(point_stream) < k: return all of point_stream (no zeros)

def euclidian(p1, p2):
    return ((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)
def k_closest_points(k, ref_point, point_stream):
    """Return an array of k-length that contains the k-closests points from
    point_stream to ref_point.
    k - on the order of 100 - you can keep all of these points in memory
    ref_point - (x,y), the "center" which you want to find close points to
    point_stream - on the order of millions, and you only access one at a time

    For example:
        k_closest_points(2, (1,1), [(2,3), (3,4), (5,6)]) # [(2,3), (3,4)]
        k_closest_points(1, (1,1), [(2,3), (3,4), (5,6)]) # [(2,3)]
        k_closest_points(1, (1,1), [(-1,3), (-5,4), (2,2)]) # [(2,2)]
    """
    num_points = 0
    k_closest = []
    threshold_dist = None
    def updateThreshold(arr):
        arr.sort()
        #grab the updated threshold distance value
        return arr[k-1][0]
        
    
    for point in point_stream: #O(n) for n points in point_stream
        dist = euclidian(point, ref_point)
        if (len(k_closest) < k-1):
            k_closest.append((dist, point))
        # we have exactly k-1 points at the beginning
        elif (threshold_dist == None and len(k_closest) == k-1):
            # add the new point and calculate the first threshold distance
            k_closest.append((dist, point))
            threshold_dist = updateThreshold(k_closest)
        #
        elif (dist < threshold_dist):
            #update the threshold and update the k_closest array
            k_closest.pop(k-1)
            k_closest.append((dist, point))
            threshold_dist = updateThreshold(k_closest)
    return [t[1] for t in k_closest] #O(k) traversal

print k_closest_points(1, (1,1), [(2,3), (3,4), (5,6)]) 
            
            
            
    

