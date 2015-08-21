import time
class kvStore:
  def __init__(self):
    self.timestamp = {}
    #key -> [(timestamp, val), ... ]

  def put(self, key, value):
    if (key in self.timestamp):
      self.timestamp[key].insert(0, (time.time(), value))
    else: # first time
      self.timestamp[key] = []
      tup = (time.time(), value)
      self.timestamp[key].append(tup)


  def get(self, key, timestamp=None):
    if (timestamp == None):
      return self.timestamp[key][0][1]
    else:
      times = self.timestamp[key]
      for time in times:
        if (timestamp >= time[0]):
          return time[1]
      return None

kv = kvStore()
ta = time.time()
kv.put("apple", "2")
ts = time.time()
kv.put("banna", "1")
kv.put("apple", "3")
print kv.get("apple", ts)
print kv.get("apple", ta)
print kv.get("sdf")
