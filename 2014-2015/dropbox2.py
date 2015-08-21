"""
get_hits() -> returns # hits in past 5 min
log_hit() -> logs a hit

From your 
"""

import time

buckets = {}
buckets_lock = Lock()
def get_hits():
    count = 0
    cur_t_sec = time.time('sec')
    for bucket in buckets:
        # if the timestamp is outdated
        if bucket < cur_ts-60*5:
            del buckets[bucket]
        # update counter
        else:
            count += buckets[bucket]
    return count

def log_hit():
    t_sec = time.time('sec')
    
    if t_sec in buckets:
        buckets[t_sec] += 1
    else:
        buckets[t_sec] = 1
    # prune here as well
    for bucket in buckets:
        # if the timestamp is outdated
        if bucket < cur_ts-60*5:
            del buckets[bucket]
    