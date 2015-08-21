from os import *
from signal import *
from thread import *
from threading import *
import time
import random

forks = [allocate_lock() for i in range(5)]

class Semaphore(object):

  def __init__(self, initial):
    self.lock = Condition(Lock())
    self.value = initial

  def up(self):
    with self.lock:
      self.value += 1
      self.lock.notify() # triggers the condition variable

  def down(self):
    with self.lock:
      while self.value == 0:
        self.lock.wait()
      self.value -= 1

class Fork:
  def __init__(self, number):
    self.id = number
    self.user = -1 # which philosopher is using it?
    self.lock = Condition(Lock())
    self.taken = False

  def take(self, user):
    with self.lock:
      while self.taken == True:
        self.lock.wait()
      self.user = user
      self.taken = True
      print "philosopher [",user,"] took chopstick[",self.id,"]"
      self.lock.notifyAll()

  def drop(self, user):         # used for synchronization
    with self.lock:
      while self.taken == False:
          self.lock.wait()
      self.user = -1
      self.taken = False
      print "philosopher [",user,"] dropped chopstick[",self.id,"]"
      self.lock.notifyAll()

class Philosopher(Thread):
  def __init__(self, i, left, right, semaphore):
    Thread.__init__(self) #inheriting the thread class
    self.left = left
    self.right = right
    self.semaphore = semaphore
    self.id = i

  def eat(self):
    self.semaphore.down()
    self.left.take(self.id)
    time.sleep(random.random())
    self.right.take(self.id)
    print "Philosopher #", self.id, " is eating.."
    time.sleep(random.random())
    self.right.drop(self.id)
    self.left.drop(self.id)
    self.semaphore.up()
    print "Philosopher #", self.id, " is done thinking/eating."

  def think(self):
    print "Philosopher #", self.id, " is thinking.."
    time.sleep(random.random())

  def run(self):
    self.think()
    self.eat()

n = 5
butler = Semaphore(n-1)
forks = [Fork(i) for i in range(n)]
philosophers = [Philosopher(i, forks[i], forks[(i+1)%n], butler) for i in range(n)]
for i in range(5):
  philosophers[i].start()
